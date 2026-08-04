#!/usr/bin/env python
"""게임 효과음을 하나의 WAV 로 렌더해서 실제로 들어볼 수 있게 만든다.

  python rendersound.py --out sfx.wav
"""
import argparse, base64, functools, http.server, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass
ROOT = r"C:\Project\Blog\static\games"


def serve(root):
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
        def end_headers(self):
            self.send_header("Cache-Control", "no-store"); super().end_headers()
    s = socket.socket(); s.bind(("127.0.0.1", 0)); port = s.getsockname()[1]; s.close()
    threading.Thread(target=http.server.ThreadingHTTPServer(
        ("127.0.0.1", port), functools.partial(Q, directory=root)).serve_forever,
        daemon=True).start()
    return port


HTML = """<!DOCTYPE html><meta charset=utf-8>
<div id=boot></div><div id=bootBar></div><div id=bootMsg></div><div id=bootErr></div>
<script src="/shunting/vendor/three.min.js"></script>
<script src="/shunting/js/00-util.js"></script>
<script src="/shunting/js/40-audio.js"></script>"""

# 각 소리를 개별 렌더한 뒤 하나의 트랙에 이어 붙이고 WAV 로 인코딩한다.
RENDER = r"""
async (plan) => {
  const SR = 44100;
  const chunks = [];
  for (const item of plan) {
    const secs = item.secs;
    const oc = new OfflineAudioContext(1, Math.ceil(SR * secs), SR);
    try {
      if (SH.Audio.renderOffline) await SH.Audio.renderOffline(oc, item.name, item.opts || {});
      else { SH.Audio.init(oc); SH.Audio.play(item.name); }
      const buf = await oc.startRendering();
      chunks.push({ label: item.label, data: Array.from(buf.getChannelData(0)) });
    } catch (e) {
      chunks.push({ label: item.label + ' (ERR ' + String(e).slice(0, 60) + ')',
                    data: new Array(Math.ceil(SR * 0.2)).fill(0) });
    }
  }
  // 이어 붙이기 (사이에 0.25초 무음)
  const gap = Math.floor(SR * 0.25);
  let total = 0;
  chunks.forEach(c => { total += c.data.length + gap; });
  const out = new Float32Array(total);
  let off = 0; const marks = [];
  chunks.forEach(c => {
    marks.push({ label: c.label, at: +(off / SR).toFixed(2) });
    out.set(c.data, off); off += c.data.length + gap;
  });
  // 16bit PCM WAV 인코딩
  const n = out.length;
  const ab = new ArrayBuffer(44 + n * 2);
  const dv = new DataView(ab);
  const wr = (o, s) => { for (let i = 0; i < s.length; i++) dv.setUint8(o + i, s.charCodeAt(i)); };
  wr(0, 'RIFF'); dv.setUint32(4, 36 + n * 2, true); wr(8, 'WAVE');
  wr(12, 'fmt '); dv.setUint32(16, 16, true); dv.setUint16(20, 1, true);
  dv.setUint16(22, 1, true); dv.setUint32(24, SR, true);
  dv.setUint32(28, SR * 2, true); dv.setUint16(32, 2, true); dv.setUint16(34, 16, true);
  wr(36, 'data'); dv.setUint32(40, n * 2, true);
  let peak = 0;
  for (let i = 0; i < n; i++) peak = Math.max(peak, Math.abs(out[i]));
  const norm = peak > 0.95 ? 0.95 / peak : 1;      // 클리핑 방지만, 음량 밸런스는 유지
  for (let i = 0; i < n; i++) {
    const v = Math.max(-1, Math.min(1, out[i] * norm));
    dv.setInt16(44 + i * 2, v < 0 ? v * 0x8000 : v * 0x7FFF, true);
  }
  let bin = ''; const u8 = new Uint8Array(ab);
  for (let i = 0; i < u8.length; i++) bin += String.fromCharCode(u8[i]);
  return { wav: btoa(bin), marks: marks, seconds: +(n / SR).toFixed(1), peak: +peak.toFixed(3) };
}
"""

PLAN = [
    {"label": "ui — 버튼",            "name": "ui",       "secs": 0.5},
    {"label": "points — 분기기 전환", "name": "points",   "secs": 1.2},
    {"label": "hiss — 브레이크 배기", "name": "hiss",     "secs": 1.5},
    {"label": "clank — 충격",         "name": "clank",    "secs": 1.2},
    {"label": "couple — 연결",        "name": "couple",   "secs": 1.5},
    {"label": "squeal — 차륜 마찰",   "name": "squeal",   "secs": 1.2},
    {"label": "horn — 경적",          "name": "horn",     "secs": 2.0},
    {"label": "fail — 거절",          "name": "fail",     "secs": 1.2},
    {"label": "win — 승리",           "name": "win",      "secs": 2.5},
    {"label": "engine 아이들 (load 0)",   "name": "engine", "secs": 2.5, "opts": {"load": 0.0}},
    {"label": "engine 중간 (load 0.5)",   "name": "engine", "secs": 2.5, "opts": {"load": 0.5}},
    {"label": "engine 최대 (load 1.0)",   "name": "engine", "secs": 2.5, "opts": {"load": 1.0}},
    {"label": "roll 저속 (8 m/s)",    "name": "roll",     "secs": 2.5, "opts": {"speed": 8}},
    {"label": "roll 고속 (28 m/s)",   "name": "roll",     "secs": 2.5, "opts": {"speed": 28}},
    {"label": "ambience — 배경",      "name": "ambience", "secs": 4.0},
]

ap = argparse.ArgumentParser()
ap.add_argument("--out", default="sfx.wav")
a = ap.parse_args()

from playwright.sync_api import sync_playwright
port = serve(ROOT)
with sync_playwright() as p:
    b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                "--autoplay-policy=no-user-gesture-required"])
    pg = b.new_page()
    errs = []
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.route("**/__snd", lambda r: r.fulfill(body=HTML, content_type="text/html"))
    pg.goto(f"http://127.0.0.1:{port}/__snd", wait_until="load", timeout=45000)
    has = pg.evaluate("() => typeof SH.Audio.renderOffline === 'function'")
    print("renderOffline 지원:", has)
    res = pg.evaluate(RENDER, PLAN)
    b.close()

open(a.out, "wb").write(base64.b64decode(res["wav"]))
print(f"저장: {a.out}  ({res['seconds']}초, peak {res['peak']})")
print("\n타임라인:")
for m in res["marks"]:
    print(f"  {m['at']:6.2f}s  {m['label']}")
if errs:
    print("\n--- ERRORS ---")
    for e in errs[:5]:
        print(" ", e[:200])
