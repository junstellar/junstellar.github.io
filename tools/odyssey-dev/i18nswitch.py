#!/usr/bin/env python
"""실행 중 언어 전환 + 모바일 세로 확인."""
import functools, http.server, os, socket, sys, threading
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass
ROOT = r"C:\Project\Blog\static\games"

def serve(root):
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self,*a): pass
        def end_headers(self):
            self.send_header("Cache-Control","no-store"); super().end_headers()
    s=socket.socket(); s.bind(("127.0.0.1",0)); port=s.getsockname()[1]; s.close()
    h=http.server.ThreadingHTTPServer(("127.0.0.1",port), functools.partial(Q,directory=root))
    threading.Thread(target=h.serve_forever,daemon=True).start(); return port,h

def main():
    os.makedirs("switch_out", exist_ok=True)
    port,h = serve(ROOT)
    from playwright.sync_api import sync_playwright
    errs=[]; ok=True
    with sync_playwright() as p:
        b=p.chromium.launch(args=["--use-angle=d3d11","--ignore-gpu-blocklist","--enable-unsafe-swiftshader"])

        # --- 실행 중 전환 ---
        pg=b.new_page(viewport={"width":1100,"height":820})
        pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(f"http://127.0.0.1:{port}/odyssey/index.html?debug=1&fresh=1")
        pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
        pg.wait_for_timeout(800)
        print("=== 실행 중 언어 전환 ===")
        for L,expect in [("en","Press space"),("ja","スペース"),("zh","按空格"),("ko","스페이스")]:
            pg.click(f".od-lang button[data-l='{L}']")
            pg.wait_for_timeout(1300)
            hint = pg.evaluate("() => { var e=document.querySelector('.st1 .hint'); return e?e.textContent.trim():''; }")
            eng  = pg.evaluate("() => __SHOT.state().engine")
            good = expect in hint and eng=="st1"
            print(f"  -> {L}: hint={hint[:34]!r} engine={eng} {'OK' if good else '*** 실패 ***'}")
            ok &= good
        pg.close()

        # --- 모바일 세로 ---
        print("\n=== 모바일 세로 430x932 (en) ===")
        pg=b.new_page(viewport={"width":430,"height":932})
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(f"http://127.0.0.1:{port}/odyssey/index.html?fresh=1&lang=en")
        pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
        pg.wait_for_timeout(900)
        pg.screenshot(path="switch_out/mobile_en.png")
        ov = pg.evaluate("""() => {
          const bad=[]; const W=innerWidth;
          document.querySelectorAll('.st1 *, .od-lang *').forEach(el=>{
            if(!el.textContent||!el.textContent.trim())return;
            const cs=getComputedStyle(el);
            if(cs.display==='none'||cs.visibility==='hidden'||+cs.opacity===0)return;
            const r=el.getBoundingClientRect(); if(!r.width)return;
            if(r.left<-2||r.right>W+2) bad.push({t:el.textContent.trim().slice(0,30),
                                                 l:Math.round(r.left),r:Math.round(r.right),W});
          }); return bad; }""")
        print("  넘침:", ov if ov else "없음")
        ok &= not ov
        pg.close(); b.close()
    h.shutdown()
    print(f"\nconsole errors: {len(errs)}")
    for e in errs[:4]: print("  ", e[:150])
    print("RESULT:", "OK" if ok and not errs else "*** 실패 ***")

main()
