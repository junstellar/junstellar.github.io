#!/usr/bin/env python
"""게이지 캐럿 검증 — 금색 띠에선 "지금", 붉은 구간에선 "늦었다" 인지 확인한다."""
import functools, http.server, json, os, socket, sys, threading

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
    return port, httpd


PROBE = """() => {
  var q = function (s) { return document.querySelector('.st2 ' + s); };
  var load = q('.load'), now = q('.now'), tr = q('.ltrack');
  var R = tr.getBoundingClientRect();
  var px = function (el) { var b = el.getBoundingClientRect();
                           return [+( (b.left-R.left)/R.width ).toFixed(3),
                                   +( (b.right-R.left)/R.width ).toFixed(3)]; };
  var s = window.OD.St2.state();
  return { cls: load.className, caret: now.textContent,
           caretOpacity: getComputedStyle(now).opacity,
           gold: px(q('.gold')), danger: px(q('.danger')),
           fill: px(q('.lfill')), head: px(q('.lhead'))[0],
           load: s.load, band: s.band, kind: s.kind, inGold: s.inGold, inRed: s.inRed };
}"""


def main():
    out = "caret_out"
    os.makedirs(out, exist_ok=True)
    port, httpd = serve(ROOT)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--hide-scrollbars", "--mute-audio"])
        ctx = b.new_context(viewport={"width": 1100, "height": 820}, device_scale_factor=1)
        pg = ctx.new_page()
        pg.goto(f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1",
                wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true", timeout=60000)
        pg.evaluate("() => window.__SHOT.stage(1)")
        pg.wait_for_timeout(400)

        for tag, want in (("gold", "inGold"), ("red", "inRed")):
            for _ in range(400):
                s = pg.evaluate("() => window.OD.St2.state()")
                if s[want]:
                    break
                pg.evaluate("([s,d]) => window.__SHOT.hold(s,d)", [0.04, True])
            pg.wait_for_timeout(260)          # CSS 전환이 끝나도록 (벽시계)
            print(tag.upper(), json.dumps(pg.evaluate(PROBE), ensure_ascii=False))
            pg.screenshot(path=os.path.join(out, f"{tag}.png"),
                          clip={"x": 240, "y": 660, "width": 620, "height": 130})
            print("  shot", os.path.join(out, f"{tag}.png"))
        b.close()
    httpd.shutdown()


if __name__ == "__main__":
    main()
