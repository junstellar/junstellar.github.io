#!/usr/bin/env python
"""에필로그의 '처음부터' 와 각 편의 '다시' 가 실제로 판을 되돌리는가."""
import functools, http.server, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"
ST = "() => JSON.parse(JSON.stringify(window.__SHOT.state()))"


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


def main():
    os.makedirs("restart_out", exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"
    from playwright.sync_api import sync_playwright
    errors = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--hide-scrollbars", "--mute-audio"])
        pg = b.new_context(viewport={"width": 1100, "height": 820},
                           device_scale_factor=1).new_page()
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[console] {m.text}")
              if m.type == "error" else None)
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                             timeout=90000)
        pg.wait_for_timeout(700)

        # 1편 '다시' — 잃은 부하가 되돌아오는가
        pg.evaluate("() => window.__SHOT.auto(['big'], 95)"); pg.wait_for_timeout(900)
        a = pg.evaluate(ST)
        print(f"1편 결과: crew={a.get('crew')} (600 에서 줄었어야 한다)")
        pg.wait_for_timeout(450)
        pg.evaluate("() => window.__SHOT.retry()"); pg.wait_for_timeout(1000)
        c = pg.evaluate(ST)
        print(f"  다시 -> engine={c.get('engine')} phase={c.get('phase')} "
              f"crew={c.get('crew')} waiting={c.get('waiting')}")

        # 6편까지 몰아서 -> 에필로그 -> '처음부터'
        for i, arg in [(0, "['big','mid','sml'], 95"), (1, "'gold', 300"),
                       (2, "'smart', 200"), (3, "6, 260"), (4, "'band', 220"),
                       (5, "null, 120")]:
            pg.evaluate(f"() => window.__SHOT.stage({i})"); pg.wait_for_timeout(600)
            pg.evaluate(f"() => window.__SHOT.auto({arg})"); pg.wait_for_timeout(800)
            pg.wait_for_timeout(450)
            pg.evaluate("() => window.__SHOT.next()"); pg.wait_for_timeout(900)
        e = pg.evaluate(ST)
        print(f"에필로그: card={e.get('card')} finished={e.get('finished')} "
              f"crew={e.get('crew')}")
        pg.wait_for_timeout(450)
        pg.keyboard.press(" ")               # '처음부터' 를 스페이스로
        pg.wait_for_timeout(1400)
        r = pg.evaluate(ST)
        pg.screenshot(path=os.path.join("restart_out", "restarted.png"))
        print(f"처음부터 -> {r.get('index')+1}편 {r.get('id')} engine={r.get('engine')} "
              f"phase={r.get('phase')} crew={r.get('crew')} card={r.get('card')}")
        ok = (r.get("id") == "cyclops" and r.get("crew") == 600
              and r.get("phase") == "run" and not r.get("cardOpen"))
        print("처음부터:", "OK" if ok else "실패")
        b.close()
    httpd.shutdown()
    print(f"--- {len(errors)} console error(s) ---")
    for x in errors[:10]:
        print("  ", x[:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
