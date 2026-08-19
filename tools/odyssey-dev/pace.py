#!/usr/bin/env python
"""2·3·4편 길이와 난이도를 함께 잰다.

길이만 줄이고 난이도가 같이 내려가면 실패다. 그래서 길이(초)와 함께
- 3편: 파도마다 '끝까지 붙잡는 데 드는 악력'(tuning 표)
- 2편: 여러 정책의 도달률
을 같이 찍는다.
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    a = ap.parse_args()
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"

    from playwright.sync_api import sync_playwright
    errs = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width": a.w, "height": a.h})
        pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(url); pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)

        # ── 3편 난이도 표 (파도별 필요 악력) ────────────────────────────────
        print("=== 3편 파도별 '끝까지 붙잡는 데 드는 악력' (1.0 = 악력 전부) ===")
        pg.evaluate("() => __SHOT.stage(2)")
        pg.wait_for_function("() => __SHOT.state().engine==='st3'", timeout=20000)
        pg.wait_for_timeout(400)
        tun = pg.evaluate("() => JSON.parse(JSON.stringify(OD.St3.costTable()))")
        print(" ", json.dumps(tun, ensure_ascii=False)[:900])

        # ── 길이 + 정책별 결과 ─────────────────────────────────────────────
        print("\n=== 길이 · 정책별 결과 ===")
        runs = [
            ("2편 windbag", 1, "St2", ["'gold'", "'timid'", "'hold'"]),
            ("3편 sirens",  2, "St3", ["'smart'", "'plain'"]),
            ("4편 scylla",  3, "St4", ["6"]),
        ]
        for name, idx, eng, pols in runs:
            for pol in pols:
                pg.evaluate(f"() => __SHOT.stage({idx})")
                pg.wait_for_function(f"() => __SHOT.state().engine==='{eng.lower()}'",
                                     timeout=20000)
                pg.wait_for_timeout(350)
                r = pg.evaluate(
                    f"() => {{ var s=OD.{eng}.auto({pol}, 400);"
                    " return JSON.parse(JSON.stringify(s)); }")
                res = r.get("result") or {}
                print(f"  {name:12s} {pol:9s} t={r.get('t'):6}초  "
                      f"win={res.get('win')} prog={res.get('prog')} "
                      f"lost={res.get('crewLost', res.get('lost'))} "
                      f"taken={res.get('taken')}")

        b.close()
    httpd.shutdown()
    print(f"\n--- console errors: {len(errs)} ---")
    for e in errs[:6]:
        print("  ", e[:200])


if __name__ == "__main__":
    main()
