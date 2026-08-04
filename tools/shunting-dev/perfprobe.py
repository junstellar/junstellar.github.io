#!/usr/bin/env python
"""모바일 성능 여유 계측 — 뷰포트 + CPU 스로틀링으로 중저가 폰을 흉내낸다.

  python perfprobe.py                 # 데스크톱 / 4x / 6x 전부
  python perfprobe.py --throttle 6    # 특정 배율만

CPU 스로틀링 기준(대략):
  1x = 이 PC   4x ≈ 중급 안드로이드   6x ≈ 저가 안드로이드
"""
import argparse, functools, http.server, json, socket, sys, threading

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
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", port),
                                            functools.partial(Q, directory=root))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return port


# 60프레임을 실제로 세어 fps 를 낸다 (게임 내부 카운터를 믿지 않는다)
MEASURE = r"""
async (secs) => {
  const t0 = performance.now();
  let frames = 0, worst = 0, last = t0;
  await new Promise(res => {
    function tick(t) {
      const dt = t - last; last = t;
      if (frames > 2 && dt > worst) worst = dt;
      frames++;
      if (t - t0 < secs * 1000) requestAnimationFrame(tick); else res();
    }
    requestAnimationFrame(tick);
  });
  const el = (performance.now() - t0) / 1000;
  const i = window.__SHOT && window.__SHOT.info ? window.__SHOT.info() : {};
  return { fps: +(frames / el).toFixed(1), worstFrameMs: Math.round(worst),
           quality: i.quality, tris: i.tris, calls: i.calls, errors: i.errors };
}
"""

ap = argparse.ArgumentParser()
ap.add_argument("--throttle", type=int, default=0)
ap.add_argument("--secs", type=float, default=6.0)
a = ap.parse_args()

rates = [a.throttle] if a.throttle else [1, 4, 6]
from playwright.sync_api import sync_playwright

port = serve(ROOT)
print(f"{'조건':<26} {'부팅':>7} {'품질':>5} {'idle fps':>9} {'이동중 fps':>11} "
      f"{'최악프레임':>10} {'tris':>9} {'calls':>7}")
print("-" * 92)

for rate in rates:
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--mute-audio", "--hide-scrollbars"])
        pg = b.new_page(viewport={"width": 430, "height": 932}, device_scale_factor=2,
                        is_mobile=True, has_touch=True)
        cdp = pg.context.new_cdp_session(pg)
        if rate > 1:
            cdp.send("Emulation.setCPUThrottlingRate", {"rate": rate})
        import time
        t0 = time.time()
        pg.goto(f"http://127.0.0.1:{port}/shunting/index.html?debug=1&fresh=1",
                wait_until="domcontentloaded", timeout=90000)
        try:
            pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                                 timeout=300000)
            boot = time.time() - t0
        except Exception:
            print(f"{'CPU ' + str(rate) + 'x (430x932@2)':<26}  부팅 실패/타임아웃")
            b.close(); continue
        pg.wait_for_timeout(1200)

        idle = pg.evaluate(MEASURE, a.secs)
        # 이동 애니메이션 중 (가장 무거운 구간)
        pg.evaluate("""() => { window.dispatchEvent(new KeyboardEvent('keydown',
            {key:'1',code:'Digit1',bubbles:true})); }""")
        pg.wait_for_timeout(400)
        moving = pg.evaluate(MEASURE, min(a.secs, 3.0))
        b.close()

    label = f"CPU {rate}x (430x932@2)"
    print(f"{label:<26} {boot:>6.1f}s {idle['quality']:>5} {idle['fps']:>9.1f} "
          f"{moving['fps']:>11.1f} {idle['worstFrameMs']:>9}ms "
          f"{idle['tris']:>9,} {idle['calls']:>7,}")
    if idle.get("errors"):
        print(f"    ! 콘솔 에러 {idle['errors']}건")
