#!/usr/bin/env python
"""입력 반응성 계측 — 애니메이션 중 입력이 버려지는지, 코치 카드가 얼마나 늦는지 잰다."""
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
  const card = () => {
    const el = document.querySelector('[class*=tut],[class*=coach]');
    if (!el) return { text: null, visible: false, opacity: null };
    const cs = getComputedStyle(el);
    return { text: (el.innerText || '').replace(/\s+/g, ' ').trim().slice(0, 60),
             visible: cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity > 0.5,
             opacity: +cs.opacity };
  };
  const S = () => ({ moves: SH.Game.state.moves, at: SH.Game.state.at,
                     consist: SH.Game.state.consist.slice(), busy: !!SH.Motion.isBusy });
  const key = k => { window.dispatchEvent(new KeyboardEvent('keydown',
      { key: k, code: 'Digit' + k, bubbles: true }));
    window.dispatchEvent(new KeyboardEvent('keyup',
      { key: k, code: 'Digit' + k, bubbles: true })); };

  const out = { timeline: [], tests: {} };

  // ── 1. 부팅 후 코치 카드가 화면에 뜨기까지 ──
  const t0 = performance.now();
  let firstVisible = null;
  for (let i = 0; i < 120; i++) {
    const c = card();
    if (c.visible && firstVisible === null) { firstVisible = performance.now() - t0; break; }
    await sleep(100);
  }
  out.tests.cardFirstVisibleMs = firstVisible === null ? 'NEVER' : Math.round(firstVisible);
  out.tests.cardTextAtStart = card().text;

  // ── 2. 이동 중 입력이 버려지는가 ──
  const before = S();
  key('1');
  await sleep(700);                                   // 애니메이션 한창일 때
  const mid = S();
  key('4');                                           // ← 이 입력이 살아남는가?
  const tKey2 = performance.now();
  let honored = false, settleMs = null;
  for (let i = 0; i < 200; i++) {
    await sleep(100);
    const s = S();
    if (!s.busy && settleMs === null) settleMs = Math.round(performance.now() - tKey2);
    if (s.at === 'EXIT') { honored = true; break; }
    if (settleMs !== null && performance.now() - tKey2 > settleMs + 4000) break;
  }
  out.tests.inputDuringAnim = {
    firedWhileBusy: mid.busy, honored: honored,
    movesBefore: before.moves, movesAfter: S().moves,
    settleAfterKeyMs: settleMs, finalAt: S().at,
  };

  // ── 3. 상태 변화 → 카드 문구 갱신 지연 ──
  const textBefore = card().text;
  const mv = S().moves;
  const tAct = performance.now();
  let stateChangedMs = null, cardChangedMs = null;
  key('1');
  for (let i = 0; i < 250; i++) {
    await sleep(80);
    if (stateChangedMs === null && S().moves !== mv) stateChangedMs = Math.round(performance.now() - tAct);
    if (cardChangedMs === null && card().text !== textBefore) cardChangedMs = Math.round(performance.now() - tAct);
    if (stateChangedMs !== null && cardChangedMs !== null) break;
  }
  out.tests.cardLag = {
    stateChangedMs, cardChangedMs,
    lagMs: (stateChangedMs !== null && cardChangedMs !== null) ? cardChangedMs - stateChangedMs : null,
    textBefore, textAfter: card().text,
  };

  // ── 4. 존재하지 않는 번호키를 눌렀을 때 피드백이 있는가 ──
  const toastsBefore = document.querySelectorAll('[class*=toast]').length;
  const m2 = S().moves;
  key('3');                                            // LV01 엔 S3 가 없다
  await sleep(700);
  out.tests.emptyKeySlot = {
    movesChanged: S().moves !== m2,
    toastAppeared: document.querySelectorAll('[class*=toast]').length > toastsBefore,
  };
  return out;
}
"""

from playwright.sync_api import sync_playwright
port = serve(ROOT)
errs = []
with sync_playwright() as p:
    b = p.chromium.launch(args=["--use-angle=d3d11", "--ignore-gpu-blocklist", "--mute-audio"])
    pg = b.new_page(viewport={"width": 1100, "height": 820})
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto(f"http://127.0.0.1:{port}/shunting/index.html?debug=1&fresh=1",
            wait_until="domcontentloaded", timeout=60000)
    pg.wait_for_function("() => window.__SHOT && window.__SHOT.ready === true", timeout=180000)
    print(json.dumps(pg.evaluate(PROBE), ensure_ascii=False, indent=1))
    b.close()
if errs:
    print("--- ERRORS ---")
    for e in errs[:6]:
        print(" ", e[:300])
