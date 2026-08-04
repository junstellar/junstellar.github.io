#!/usr/bin/env python
"""열차 속도/가감속 프로파일 계측 — 이동 한 번의 속도 곡선과 실제 이동 거리를 잰다."""
import functools, http.server, json, socket, sys, threading

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


PROBE = r"""
async () => {
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const loco = () => {
    const w = SH.Game.world;
    const g = w && w.loco ? w.loco.group : null;
    return g ? g.position.clone() : null;
  };
  const out = { samples: [], summary: {} };

  const p0 = loco();
  const t0 = performance.now();
  let prev = p0, prevT = t0, dist = 0, peak = 0;

  window.dispatchEvent(new KeyboardEvent('keydown', { key: '1', code: 'Digit1', bubbles: true }));
  window.dispatchEvent(new KeyboardEvent('keyup',   { key: '1', code: 'Digit1', bubbles: true }));

  for (let i = 0; i < 400; i++) {
    await sleep(50);
    const p = loco(); const t = performance.now();
    if (!p) break;
    const d = p.distanceTo(prev);
    const dt = (t - prevT) / 1000;
    const v = dt > 0 ? d / dt : 0;
    dist += d;
    if (v > peak) peak = v;
    out.samples.push({ t: +((t - t0) / 1000).toFixed(2), v: +v.toFixed(2),
                       rep: +(SH.Motion.speed || 0).toFixed(1) });
    prev = p; prevT = t;
    if (i > 8 && !SH.Motion.isBusy) break;
  }

  const tot = (performance.now() - t0) / 1000;
  out.summary = {
    durationSec: +tot.toFixed(2),
    distanceUnits: +dist.toFixed(1),
    peakMeasured_mps: +peak.toFixed(2),
    avgMeasured_mps: +(dist / tot).toFixed(2),
    peakReported_MotionSpeed: +Math.max(...out.samples.map(s => s.rep)).toFixed(1),
    wagonLenUnits: 12, note: '1 unit = 1 m (SPEC §5)',
  };
  // 속도 곡선을 20구간으로 요약
  const n = out.samples.length, step = Math.max(1, Math.floor(n / 20));
  out.curve = out.samples.filter((_, i) => i % step === 0).map(s => `${s.t}s:${s.v}`);
  delete out.samples;
  return out;
}
"""

from playwright.sync_api import sync_playwright
port = serve(ROOT)
with sync_playwright() as p:
    b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist", "--mute-audio"])
    pg = b.new_page(viewport={"width": 1100, "height": 820})
    pg.goto(f"http://127.0.0.1:{port}/shunting/index.html?debug=1&fresh=1",
            wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true", timeout=180000)
    pg.wait_for_timeout(1500)
    print(json.dumps(pg.evaluate(PROBE), ensure_ascii=False, indent=1))
    b.close()
