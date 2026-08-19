#!/usr/bin/env python
"""1편을 실제로 끝내고 '계속'을 눌렀을 때 2편으로 가는지만 본다.

저장(localStorage)이 남아 있을 때와 없을 때를 나눠서 본다 —
"1편 끝냈는데 에필로그가 떴다"는 저장된 진행도가 원인일 수 있다.
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"
KEY = "gamelab:odyssey"


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


CORE = """() => {
  var C = window.OD && OD.Core;
  return {
    idx: C && C.current && C.current.index,
    id: C && C.current && C.current.stage && C.current.stage.id,
    finished: C && C.finished,
    resume: C && C.resumeIndex,
    len: C && C.stages && C.stages.length
  };
}"""


def run_case(pg, url, preset, label):
    print(f"\n=== {label} ===")
    pg.goto(url)
    pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
    if preset is not None:
        pg.evaluate(f"() => localStorage.setItem('{KEY}', {json.dumps(json.dumps(preset))})")
        pg.goto(url)                      # 저장을 심고 다시 들어간다
        pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
    pg.wait_for_timeout(700)
    print("  진입 시:", pg.evaluate(CORE))

    # 1편을 자동으로 끝낸다
    pg.evaluate("() => __SHOT.auto(['big','mid','sml'], 95)")
    pg.wait_for_timeout(1400)
    print("  1편 종료 후:", pg.evaluate(CORE))
    btns = pg.evaluate("() => [...document.querySelectorAll('.od-scrim .od-btn')]"
                       ".map(b => b.className + '/' + b.textContent)")
    print("  카드 버튼:", btns)

    # '계속'(기본 버튼)을 실제로 누른다
    pg.evaluate("() => { var n=document.querySelector('.od-scrim .od-btn.pri');"
                " if(n) n.click(); }")
    pg.wait_for_timeout(1400)
    after = pg.evaluate(CORE)
    print("  '계속' 누른 뒤:", after)
    txt = pg.evaluate("() => { var e=document.querySelector('.od-scrim');"
                      " return e? e.innerText.replace(/\\n+/g,' | ').slice(0,150):'(카드 없음)'; }")
    print("  화면:", json.dumps(txt, ensure_ascii=False))
    ok = after.get("idx") == 1 and not after.get("finished")
    print("  => 2편으로 갔나:", "OK" if ok else "*** 실패 ***")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    a = ap.parse_args()
    port, httpd = serve(ROOT)
    base = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1"

    from playwright.sync_api import sync_playwright
    results = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        pg = b.new_page(viewport={"width": a.w, "height": a.h})

        results.append(run_case(pg, base + "&fresh=1", None, "저장 없음 (fresh=1)"))
        # 사용자가 겪었을 상태: 예전에 뒤쪽 편까지 건드려 index 가 올라가 있다
        results.append(run_case(pg, base, {
            "v": 1, "index": 5, "crew": 600, "finished": False,
            "results": [None] * 6, "elapsed": 0, "ts": 0
        }, "저장된 index=5 (뒤쪽 편을 건드린 적 있음)"))
        results.append(run_case(pg, base, {
            "v": 1, "index": 3, "crew": 600, "finished": False,
            "results": [None, None, None,
                        {"id": "scylla", "win": False, "lost": 600, "runs": 1, "stars": 0}],
            "elapsed": 0, "ts": 0
        }, "저장된 index=3"))
        # ★ 가장 유력한 원인: 한 번이라도 끝까지 간 적이 있어 finished 가 남아 있다
        results.append(run_case(pg, base, {
            "v": 1, "index": 5, "crew": 600, "finished": True,
            "results": [None] * 6, "elapsed": 0, "ts": 0
        }, "저장된 finished=true (끝까지 간 적 있음)"))

        b.close()
    httpd.shutdown()
    print("\n=== 정리 ===", "모두 OK" if all(results) else "재현됨 — 저장된 진행도가 원인")


if __name__ == "__main__":
    main()
