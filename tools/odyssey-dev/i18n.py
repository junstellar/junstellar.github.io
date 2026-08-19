#!/usr/bin/env python
"""1편 4개국어 검증.

번역은 넣는 것보다 **넘치는지 보는 것**이 일이다. 한국어는 짧고 영어는 길어서
게이지 옆 문구나 결과 카드에서 줄이 깨진다. 그래서 언어마다
  - 문자열이 실제로 그 언어로 나오는지
  - 화면 밖으로 나가거나 부모를 넘치는 요소가 있는지
  - 결과 카드가 몇 줄이 되는지
를 재고 스크린샷을 남긴다.
"""
import argparse, functools, http.server, json, os, socket, sys, threading

try:
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT = r"C:\Project\Blog\static\games"
LANGS = ["ko", "en", "ja", "zh"]


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


# 화면 밖으로 나갔거나 부모를 가로로 넘치는 텍스트 요소를 찾는다
OVERFLOW = """() => {
  const bad = [];
  const W = innerWidth, H = innerHeight;
  document.querySelectorAll('.st1 *, .od-card *, .od-scrim *, .od-lang *').forEach(el => {
    if (!el.textContent || !el.textContent.trim()) return;
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return;
    const r = el.getBoundingClientRect();
    if (r.width === 0 || r.height === 0) return;
    const out = (r.left < -2 || r.right > W + 2);
    const clip = el.scrollWidth > el.clientWidth + 2 && cs.overflow !== 'visible';
    if (out || clip) bad.push({
      cls: el.className && el.className.toString().slice(0, 40),
      txt: el.textContent.trim().slice(0, 46),
      left: Math.round(r.left), right: Math.round(r.right), W,
      scrollW: el.scrollWidth, clientW: el.clientWidth
    });
  });
  return bad;
}"""

TEXTS = """() => {
  const g = s => { const e = document.querySelector(s); return e ? e.textContent.trim() : null; };
  return {
    cue:  g('.st1 .cue'),
    hint: g('.st1 .hint'),
    crewCap: g('.od-cap'),
    lang: window.OD && OD.I18N && OD.I18N.lang,
    stats: window.OD && OD.I18N && OD.I18N.stats()
  };
}"""

CARD = """() => {
  const e = document.querySelector('.od-scrim');
  if (!e) return null;
  const r = e.getBoundingClientRect();
  return { text: e.innerText.replace(/\\n+/g, ' | '),
           lines: e.innerText.split('\\n').filter(Boolean).length,
           h: Math.round(r.height), winH: innerHeight };
}"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="i18n_out")
    ap.add_argument("--w", type=int, default=1100)
    ap.add_argument("--h", type=int, default=820)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    port, httpd = serve(ROOT)

    from playwright.sync_api import sync_playwright
    problems, errs = [], []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist",
                                    "--enable-unsafe-swiftshader"])
        for L in LANGS:
            pg = b.new_page(viewport={"width": a.w, "height": a.h})
            pg.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
            pg.on("pageerror", lambda e: errs.append(str(e)))
            url = (f"http://127.0.0.1:{port}/odyssey/index.html"
                   f"?debug=1&fresh=1&lang={L}")
            pg.goto(url)
            pg.wait_for_function("window.__SHOT && __SHOT.ready", timeout=60000)
            pg.wait_for_timeout(900)

            print(f"\n=== {L} ===")
            t = pg.evaluate(TEXTS)
            print(f"  lang={t['lang']}  등록수={t['stats']}")
            print(f"  cue  : {t['cue']!r}")
            print(f"  hint : {t['hint']!r}")
            pg.screenshot(path=os.path.join(a.out, f"{L}_play.png"))

            ov = pg.evaluate(OVERFLOW)
            if ov:
                problems.append((L, "play", ov))
                for o in ov: print(f"  *** 넘침: {o}")
            else:
                print("  넘침 없음 (게임 화면)")

            # 1편을 끝내고 결과 카드를 본다 — 여기가 제일 길다
            pg.evaluate("() => __SHOT.auto(['big','mid','sml'], 95)")
            pg.wait_for_timeout(1600)
            c = pg.evaluate(CARD)
            if c:
                print(f"  카드 {c['lines']}줄 h={c['h']}/{c['winH']}")
                print(f"    {c['text'][:170]}")
                if c["h"] > c["winH"]:
                    problems.append((L, "card-height", c))
                    print("  *** 카드가 화면보다 높다")
            else:
                print("  *** 결과 카드가 안 떴다")
                problems.append((L, "no-card", None))
            pg.screenshot(path=os.path.join(a.out, f"{L}_card.png"))
            ov2 = pg.evaluate(OVERFLOW)
            if ov2:
                problems.append((L, "card", ov2))
                for o in ov2: print(f"  *** 카드 넘침: {o}")
            pg.close()
        b.close()
    httpd.shutdown()

    print(f"\n--- console errors: {len(errs)} ---")
    for e in errs[:6]: print("  ", e[:160])
    print("RESULT:", "OK" if not problems and not errs else f"*** 문제 {len(problems)}건 ***")


if __name__ == "__main__":
    main()
