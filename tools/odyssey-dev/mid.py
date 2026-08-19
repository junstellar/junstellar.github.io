#!/usr/bin/env python
"""편마다 '절정의 순간' 한 장씩 — 등장인물이 알아볼 수 있게 보이는가.

__SHOT.stage(i) 로 판을 열고 __SHOT.skipTo() 로 장면 한복판까지 민 뒤 찍는다.
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"

# (편 index, 파일이름, skipTo 인자)
SHOTS = [
    (0, "1_cyclops", "22, undefined"),        # 손이 입구를 훑는 순간
    (1, "2_windbag", "16, true"),             # 자루를 열고 밀고 있는 중
    (2, "3_sirens",  "16, true"),             # 노래가 밀려오는 파도 한복판
    (2, "3_sirens_rock", "58, (g)=>g.song>0.22"),   # 바위가 가장 가까운 5·6파도
    (3, "4_scylla",  "16, true"),             # 머리가 내려온 해협 한가운데
    (4, "5_cattle",  "70, 'band'"),           # 굶주림이 붉어진 사흘째
    (5, "6_bow",     "0.95, true"),           # 시위를 얹는 1막
    (5, "6_bow_aim", "3.4, (s)=>s.gp==='string' ? s.bend<0.58 : s.t<0.62"),  # 조준
]


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
    ap.add_argument("--out", default="mid_out")
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    ap.add_argument("--touch", action="store_true")
    a = ap.parse_args()

    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)
    url = f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1"

    from playwright.sync_api import sync_playwright
    errors = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--hide-scrollbars", "--mute-audio"])
        kw = dict(viewport={"width": a.w, "height": a.h}, device_scale_factor=1)
        if a.touch:
            kw.update(has_touch=True, is_mobile=True)
        pg = b.new_context(**kw).new_page()
        pg.on("pageerror", lambda e: errors.append(f"[pageerror] {e}"))
        pg.on("console", lambda m: errors.append(f"[console] {m.text}")
              if m.type == "error" else None)
        pg.goto(url, wait_until="domcontentloaded", timeout=60000)
        pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true",
                             timeout=90000)
        pg.wait_for_timeout(800)

        for i, name, arg in SHOTS:
            pg.evaluate(f"() => window.__SHOT.stage({i})")
            pg.wait_for_timeout(900)
            st = pg.evaluate(f"() => JSON.parse(JSON.stringify("
                             f"window.__SHOT.skipTo({arg})))")
            pg.wait_for_timeout(500)
            path = os.path.join(a.out, f"{name}.png")
            pg.screenshot(path=path)
            print(f"{path}  engine={st.get('engine')} phase={st.get('phase')} "
                  f"t={st.get('t', st.get('gt'))} crew={st.get('crew')}")
        b.close()
    httpd.shutdown()
    print(f"--- {len(errors)} console error(s) ---")
    for e in errors[:12]:
        print("  ", e[:400])
    return 0


if __name__ == "__main__":
    sys.exit(main())
