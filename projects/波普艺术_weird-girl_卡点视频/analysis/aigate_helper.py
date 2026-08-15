#!/usr/bin/env python3
"""Aigate 提交/下载器：幂等提交 H3 分段任务并下载结果。
用法:
  python3 aigate_helper.py submit <url> <workflow> <image> <audio> <outdir> <prefix> [--seed N]
  python3 aigate_helper.py wait-download <url> <outdir> <prefix> [--timeout 3600]
"""
import json, sys, time, urllib.request, urllib.parse, os, uuid, mimetypes

def http(method, url, payload=None, files=None, timeout=60, retries=8, backoff=10):
    last = None
    for i in range(retries):
        try:
            if files:
                boundary = uuid.uuid4().hex
                body = b''
                for name, path in files.items():
                    data = open(path, 'rb').read()
                    body += (f'--{boundary}\r\nContent-Disposition: form-data; name="{name}"; filename="{os.path.basename(path)}"\r\n'
                             f'Content-Type: application/octet-stream\r\n\r\n').encode() + data + b'\r\n'
                body += f'--{boundary}--\r\n'.encode()
                req = urllib.request.Request(url, data=body, method=method,
                                             headers={'Content-Type': f'multipart/form-data; boundary={boundary}'})
            else:
                data = json.dumps(payload).encode() if payload is not None else None
                req = urllib.request.Request(url, data=data, method=method,
                                             headers={'Content-Type': 'application/json'} if data else {})
            with urllib.request.urlopen(req, timeout=timeout) as r:
                raw = r.read()
                try:
                    return json.loads(raw)
                except Exception:
                    return raw
        except Exception as e:
            last = e
            print(f'  [http retry {i+1}/{retries}] {method} {url}: {e}', flush=True)
            time.sleep(backoff * (i + 1))
    raise RuntimeError(f'HTTP failed after retries: {last}')

def find_video_combine(wf):
    for nid, n in wf.items():
        if n.get('class_type') == 'VHS_VideoCombine':
            return nid
    return None

def submit(url, workflow_path, image_path, audio_path, outdir, prefix, seed=None):
    wf = json.load(open(workflow_path))
    # 幂等：若队列/历史中已有同名任务，则直接等待下载
    q = http('GET', url.rstrip('/') + '/queue')
    h = http('GET', url.rstrip('/') + '/history?max_items=50')
    for item in q.get('queue_running', []) + q.get('queue_pending', []):
        for nid, n in item[2].items():
            if n.get('class_type') == 'VHS_VideoCombine' and n['inputs'].get('filename_prefix') == prefix:
                print(f'[idempotent] already queued: {prefix}, waiting for it', flush=True)
                return wait_download(url, outdir, prefix)
    for pid, entry in h.items():
        for nid, n in entry.get('prompt', [None, None, {}])[2].items():
            if n.get('class_type') == 'VHS_VideoCombine' and n['inputs'].get('filename_prefix') == prefix:
                print(f'[idempotent] already done: {prefix}, downloading', flush=True)
                return wait_download(url, outdir, prefix)
    # 上传图片与音频（ComfyUI 通用 input 上传端点，用 curl 保证 multipart 正确）
    import subprocess
    def upload_one(path):
        for i in range(8):
            try:
                r = subprocess.run(
                    ['curl', '-s', '-m', '120', '-F', f'image=@{path}', '-F', 'type=input',
                     url.rstrip('/') + '/upload/image'],
                    capture_output=True, text=True, timeout=150)
                out = r.stdout.strip()
                if r.returncode == 0 and out:
                    return json.loads(out)
                print(f'  [upload retry {i+1}] rc={r.returncode} out={out[:120]}', flush=True)
            except Exception as e:
                print(f'  [upload retry {i+1}] {e}', flush=True)
            time.sleep(10 * (i + 1))
        raise RuntimeError('upload failed')
    print('uploading image...', flush=True)
    up_img = upload_one(image_path)
    img_name = up_img.get('name') or up_img.get('image', {}).get('name') or os.path.basename(image_path)
    print(f'uploaded image as: {img_name}', flush=True)
    print('uploading audio...', flush=True)
    up_aud = upload_one(audio_path)
    aud_name = up_aud.get('name') or up_aud.get('audio', {}).get('name') or os.path.basename(audio_path)
    print(f'uploaded audio as: {aud_name}', flush=True)
    # 改写节点
    img_nodes = [nid for nid, n in wf.items() if n.get('class_type') == 'LoadImage']
    aud_nodes = [nid for nid, n in wf.items() if n.get('class_type') == 'LoadAudio']
    for nid in img_nodes:
        wf[nid]['inputs']['image'] = img_name
    for nid in aud_nodes:
        wf[nid]['inputs']['audio'] = aud_name
    vc = find_video_combine(wf)
    if vc:
        wf[vc]['inputs']['filename_prefix'] = prefix
    if seed is not None:
        for nid, n in wf.items():
            if n.get('class_type') == 'RandomNoise':
                wf[nid]['inputs']['noise_seed'] = seed
    resp = http('POST', url.rstrip('/') + '/prompt', payload={'prompt': wf, 'client_id': 'dsh-' + uuid.uuid4().hex[:8]})
    pid = resp.get('prompt_id')
    if not pid:
        raise RuntimeError(f'submit failed: {resp}')
    print(f'submitted {prefix}: prompt_id={pid}', flush=True)
    return wait_download(url, outdir, prefix, pid=pid)

def wait_download(url, outdir, prefix, pid=None, timeout=3600, poll=20):
    base = url.rstrip('/')
    deadline = time.time() + timeout
    seen = set()
    while time.time() < deadline:
        h = http('GET', base + '/history?max_items=50')
        for hpid, entry in h.items():
            wf = entry.get('prompt', [None, None, {}])[2]
            for nid, n in wf.items():
                if n.get('class_type') == 'VHS_VideoCombine' and n['inputs'].get('filename_prefix') == prefix:
                    st = entry.get('status', {})
                    if st.get('status_str') == 'success':
                        os.makedirs(outdir, exist_ok=True)
                        got = []
                        for node_out in entry.get('outputs', {}).values():
                            for key in ('videos', 'images', 'gifs', 'audio', 'files'):
                                for f in node_out.get(key, []):
                                    fn = f.get('filename')
                                    if not fn or fn in seen:
                                        continue
                                    seen.add(fn)
                                    params = urllib.parse.urlencode({'filename': fn, 'subfolder': f.get('subfolder', ''), 'type': f.get('type', 'output')})
                                    dest = os.path.join(outdir, fn)
                                    print(f'downloading {fn} ...', flush=True)
                                    http('GET', base + '/view?' + params, timeout=300)
                                    # http() 是 json 模式，这里直接取文件
                                    urllib.request.urlretrieve(base + '/view?' + params, dest)
                                    got.append(dest)
                        return got
                    elif st.get('status_str') in ('error', 'failed'):
                        raise RuntimeError(f'task failed: {hpid} msgs={st.get("messages", [])[:2]}')
                    else:
                        print(f'  [{prefix}] status={st.get("status_str")} waiting...', flush=True)
        if pid:
            # 该任务尚未出现在 history 中
            print(f'  [{prefix}] not in history yet, waiting...', flush=True)
        time.sleep(poll)
    raise RuntimeError(f'timeout waiting for {prefix}')

if __name__ == '__main__':
    args = sys.argv[1:]
    mode = args[0]
    if mode == 'submit':
        url, wf, img, aud, out, prefix = args[1:7]
        seed = None
        if '--seed' in args:
            seed = int(args[args.index('--seed') + 1])
        print(json.dumps(submit(url, wf, img, aud, out, prefix, seed), ensure_ascii=False, indent=1))
    elif mode == 'wait-download':
        url, out, prefix = args[1:4]
        timeout = 3600
        if '--timeout' in args:
            timeout = int(args[args.index('--timeout') + 1])
        print(json.dumps(wait_download(url, out, prefix, timeout=timeout), ensure_ascii=False, indent=1))
