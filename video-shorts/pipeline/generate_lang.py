# -*- coding: utf-8 -*-
"""Language-complete variants of the Redmine MCP short.
Usage: python generate_lang.py ko|en

--- IDE theme v5.2 (2026-07) ----------------------------------------------
S5 (release) was re-authored: the blog block (junstellar.github.io / "To the
Moon" / "Full build story on my blog") is removed and replaced with a
"see description ↓" CTA pointing at the video description. NARR is now
tts_ko_v6 / tts_en_v6 (S5 narration shortened: ko 9.024->7.224s, en
4.944->4.464s; all other scenes byte-identical to v4). Only S5's frame budget
shrinks and every offset/adelay AFTER S5 shifts earlier; S1-S4/S6 artwork,
text and budgets are unchanged. New finished lengths: ko 63.8667s, en 44.4s.
Because S5 narration changed, the audio is FULLY re-mixed (narration adelay +
BGM), not stream-copied from the old v4 track. See render_v6.sh.

--- IDE theme v5 (2026-07) ------------------------------------------------
Artwork was re-skinned to an IDE / terminal design system (source of truth:
scratchpad/mock6.py). ONLY the way each frame is painted changed — colors,
fonts, layout, window chrome. The v4 timeline (scene lengths, frame budgets,
xfade offsets, adelay, subtitle fragments FRAGS / start frames SUB_START, BGM
assembly) is preserved EXACTLY, so the finished A/V lengths are unchanged
(ko 65.6667s, en 44.8667s) — superseded by v5.2 above for S5.

Design system (from mock6.py):
  - Background #0C0D10 + faint dot grid. NO red top/bottom bands.
  - Window tab bar (y250..338): 3 traffic-light dots + a filename label per
    scene (S1 "redmine-mcp  —  main", S2 "server.py", S3 "tools.py",
    S4 "Windows PowerShell", S5 "README.md", S6 "$ build").
  - Fonts: Korean / headlines = NotoSansKR-VF (weights 500/700/800 via
    set_variation_by_axes); code / mono = Consolas; symbol (check) = seguisym;
    emoji (sparkles on the pipx DONE line) = seguiemj.
  - Palette: WHITE / MUT / DIM / GREEN / BLUE / STRING / RED.
  - Panels: radius 24, fill (18,20,27), border (34,39,52).
  - Subtitle bar: cy 1522, translucent black rounded box, NotoSansKR 500 white.
  ! HARD RULE: never put Korean glyphs into Consolas (tofu boxes). All
    code-style text (comments, key=value, tool names, links) is ASCII/English
    in Consolas; Korean only appears in big headlines / section labels /
    subtitle bar / badge, all rendered with NotoSansKR.
  Headlines/subheads/subtitles use NotoSansKR-VF for BOTH ko and en (Latin
  glyphs unified into this face); only code/mono uses Consolas.

Scene animation (timeline fixed; only reveal choreography lives in artwork):
  S1 static; S2 two-stage (panel -> +last panel line + headline);
  S3 badge+comment+"TOOLS = [" then 10 tools reveal one by one (get_my_today
     BLUE + inline "# frequent flow -> own tool") then "]"; S4 keeps the real
     captured-terminal typing animation (command typing -> real pipx output ->
     redmine-mcp-setup -> check), re-skinned to the new chrome; S5 two-stage
     (header+repo -> +blog line + headline); S6 "$ Claude Code" line +
     BLUE second line + divider + Noto sub + blinking Consolas green cursor.

KO v3 timeline (30fps, xfade 0.5s x5):
  scene   frames  dur      start     narr-delay(ms)  narr-len  tail
  s1      305     10.1667   0.0000    300            9.288     0.579
  s2      268      8.9333   9.6667    9967           8.040     0.593
  s3      435     14.5000  18.1000   18400           13.608    0.592
  s4      488     16.2667  32.1000   32400           15.384    0.583
  s5      297      9.9000  47.8667   48167           9.024     0.576
  s6      252      8.4000  57.2667   57567           7.632     0.468
  total video = 2045/30 - 2.5 = 65.6667 s

EN v3 timeline (30fps, xfade 0.5s x5; NARR = tts_en_v3, en-US-AndrewNeural +4%):
  scene   frames  dur      start     narr-delay(ms)  narr-len  tail
  s1      241      8.0333   0.0000    300            7.152     0.581
  s2      227      7.5667   7.5333    7833           6.672     0.595
  s3      284      9.4667  14.6000   14900           8.568     0.599
  s4      320     10.6667  23.5667   23867           9.792     0.575
  s5      175      5.8333  33.7333   34033           4.944     0.589
  s6      174      5.8000  39.0667   39367           5.016     0.484
  total video = 1421/30 - 2.5 = 44.8667 s

Assembly (run from this directory; NARR = tts_ko_v4 / tts_en_v4):
 1) per scene: ffmpeg -framerate 30 -i seq_LL_sN/%05d.png -c:v libx264 -crf 18
      -preset medium -pix_fmt yuv420p -r 30 scene_LL_sN.mp4
 2) xfade chain, offsets
      ko: 9.66667 / 18.1 / 32.1 / 47.86667 / 57.26667
      en: 7.53333 / 14.6 / 23.56667 / 33.73333 / 39.06667
 3) narration: adelay (all=1) ko 300/9967/18400/32400/48167/57567
      en 300/7833/14900/23867/34033/39367, aresample=44100,
      stereo, amix normalize=0, apad to total (ko 65.66667 / en 44.86667), -c:v copy
 4) bgm: -stream_loop -1 -i bgm_pad.wav,
      [1:a]volume=0.15,afade=t=in:d=1.5,atrim=0:DUR,
      afade=t=out:st=DUR-2.53:d=2.5 ; amix normalize=0:duration=first,
      -c:v copy -c:a aac -b:a 128k -movflags +faststart
"""
import os, sys
from PIL import Image, ImageDraw, ImageFont

LANG = sys.argv[1]
assert LANG in ("ko", "en")

ROOT = os.path.dirname(os.path.abspath(__file__))
FR = os.path.join(ROOT, f"frames_{LANG}")
os.makedirs(FR, exist_ok=True)

W, H = 1080, 1920
FPS = 30.0

# ---------------- IDE theme v5 palette (from mock6.py) ----------------
BG      = (12, 13, 16)
GRID    = (24, 26, 32)
PANEL   = (18, 20, 27)
PBORD   = (34, 39, 52)
TABBAR  = (17, 19, 24)
WHITE   = (233, 237, 243)
MUT     = (122, 132, 147)
DIM     = (90, 99, 112)
GREEN   = (63, 185, 80)
BLUE    = (88, 166, 255)
STRING  = (226, 178, 120)
RED     = (240, 92, 97)
PURPLE  = (188, 140, 255)

NOTO  = "C:/Windows/Fonts/NotoSansKR-VF.ttf"
MONO  = "C:/Windows/Fonts/consola.ttf"
MONOB = "C:/Windows/Fonts/consolab.ttf"
SYM   = "C:/Windows/Fonts/seguisym.ttf"
EMOJI = "C:/Windows/Fonts/seguiemj.ttf"

X = 96  # left margin

_nc = {}
def fnoto(size, wght=700):
    k = (size, wght)
    if k not in _nc:
        f = ImageFont.truetype(NOTO, size)
        try:
            f.set_variation_by_axes([wght])
        except Exception:
            pass
        _nc[k] = f
    return _nc[k]

_mc = {}
def fmono(size, bold=False):
    k = (size, bold)
    if k not in _mc:
        _mc[k] = ImageFont.truetype(MONOB if bold else MONO, size)
    return _mc[k]

_sc = {}
def fother(path, size):
    k = (path, size)
    if k not in _sc:
        _sc[k] = ImageFont.truetype(path, size)
    return _sc[k]


def base(label):
    """Blank IDE canvas: dot grid + window tab bar with traffic lights + label."""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    for gy in range(260, 1650, 46):
        for gx in range(24, W, 46):
            d.point((gx, gy), fill=GRID)
    d.rectangle([0, 250, W, 338], fill=TABBAR)
    d.line([0, 338, W, 338], fill=(28, 31, 40), width=2)
    for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([70 + i * 46, 281, 70 + i * 46 + 26, 307], fill=c)
    d.text((232, 279), label, font=fmono(30), fill=DIM)
    return img, d


def panel(d, x0, y0, x1, y1):
    d.rounded_rectangle([x0, y0, x1, y1], radius=24, fill=PANEL, outline=PBORD, width=2)


# ---------------- per-language subtitles: full narration text ----------------
# Each scene's subtitle = the narration transcript, split into fragments.
# Fragments joined with a single space == the exact TTS input text
# (gen_tts_ko_v3.py / gen_tts_en_v3.py). Timing comes from edge-tts
# WordBoundary marks (Communicate(..., boundary="WordBoundary")): fragment k
# is shown from
#   round((first_word_offset_k + 0.3s) * 30) frames  (scene-local; 0.3s = adelay lead)
# until the next fragment's start (last fragment: until scene end).
# Fragment 0 is clamped to frame 0. Cut transitions (no fade). Min display 1.0s.
FRAGS_KO = {
    1: ["레드마인 쓰시는 분들 많으시죠.",
        "클로드 코드가 레드마인 일감을 직접 다룰 수 있게, MCP 서버를 만들어봤습니다."],
    2: ["클라우드 커넥터 없이, 내 PC에서 바로 돌아가게 구현했고",
        "API 키와 주소를 이용해 연동할 수 있습니다."],
    3: ["만드는 데는 일주일이면 충분했는데요, 그 과정을 짧게 소개합니다.",
        "코딩을 시작하기 전에, AI가 뭘 해야 하는지부터 적었고",
        "필요한 도구를 열 개로 정리했습니다."],
    4: ["클로드 코드를 이용해서 기능 구현은 쉽게 했는데",
        "누구나 쉽게 설치할 수 있게 만드는 게 문제였습니다.",
        "고민 끝에 결국 파이썬을 이용한 pipx 방식으로 배포했고,",
        "이제 어느 OS든 두 줄이면 끝입니다."],
    5: ["코드는 깃허브에 공개했습니다.",
        "자세한 내용은 영상 설명란을 참고해주세요."],
    6: ["클로드 코드를 이용하면 금방 만들 수 있을 거예요.",
        "AI 도구를 활용해 직접 만들어보세요."],
}
FRAGS_EN = {
    1: ["If you use Redmine, this one's for you.",
        "I built an MCP server so Claude Code can work your Redmine issues directly."],
    2: ["No cloud connectors. It runs right on your PC,",
        "and connects with just your API key and server address."],
    3: ["It took me just one week — here's the quick build story.",
        "Before writing any code, I listed what the AI should do,",
        "and boiled it down to ten tools."],
    4: ["Building the features with Claude Code was easy.",
        "Making it easy for anyone to install was the hard part.",
        "I settled on pipx — and now it's two commands, on any OS."],
    5: ["The code is public on GitHub.",
        "For the full write-up, check the description below."],
    6: ["With Claude Code, you can build one fast.",
        "Grab an AI tool and build your own."],
}
# scene-local start frames per fragment (30fps), derived from WordBoundary
# marks of the v4 narration synthesis (tts_ko_v4 / tts_en_v4; same voices and
# rates as v3, durations identical to v3 to the millisecond).
SUB_START_KO = {
    1: [0, 96],
    2: [0, 140],
    3: [0, 183, 311],
    4: [0, 101, 239, 368],
    5: [0, 104],
    6: [0, 126],
}
SUB_START_EN = {
    1: [0, 81],
    2: [0, 104],
    3: [0, 107, 209],
    4: [0, 91, 185],
    5: [0, 66],
    6: [0, 90],
}
FRAGS = FRAGS_KO if LANG == "ko" else FRAGS_EN
SUB_START = SUB_START_KO if LANG == "ko" else SUB_START_EN

# ---------------- subtitle bar (mock6 style) ----------------
SUB_CY = 1522
SUB_MAXW = 890

def wrap_sub(text, f):
    words = text.split(" ")
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if f.getlength(t) <= SUB_MAXW:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [text]

def draw_subtitle(img, text):
    f = fnoto(43, 500)
    lines = wrap_sub(text, f)
    lh = 57
    box_h = lh * len(lines) + 42
    by0 = SUB_CY - box_h // 2
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle(
        [88, by0, W - 88, by0 + box_h], radius=20, fill=(0, 0, 0, 165))
    img2 = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
    d = ImageDraw.Draw(img2)
    ty = by0 + 21 + lh // 2
    for ln in lines:
        d.text((W // 2, ty), ln, font=f, fill=WHITE, anchor="mm")
        ty += lh
    return img2

scenes = {}
def save(img, scene_no, name, frames, sub=None):
    # Subtitles are composited at hardlink time, driven by SUB_START;
    # the legacy per-image `sub` argument is accepted but ignored.
    p = os.path.join(FR, f"s{scene_no}_{name}.png")
    img.save(p)
    scenes.setdefault(f"s{scene_no}", []).append((p, frames))

KO = LANG == "ko"

# ================================================================
# per-language text pieces
# ================================================================
if KO:
    S1_HEAD1  = "Redmine 일감,"
    S1_H_MID  = "가 직접"          # after "Claude Code" (BLUE)
    S1_HEAD3  = "다룬다"
    S1_SUB    = "MCP 서버 직접 제작기"
    S2_HEAD   = "API 키 + 주소만 넣으면 연동"
    S3_BADGE  = "제작 기간 1주일"
    S5_HEAD   = "자세한 내용은 설명란에"
    S6_L1     = "Claude Code면"
    S6_L2     = "금방 만듭니다"
    S6_SUB    = "AI 도구로, 직접 만들어보세요"
    CAP4      = "어느 OS든 두 줄이면 끝"
    FOOT4     = "* 설치 출력은 실제 캡처, setup 입력값은 예시"
else:
    S1_HEAD1  = "Redmine issues,"
    S1_H_MID  = ""                 # en: "Claude Code" alone (BLUE), may wrap
    S1_HEAD3  = ""
    S1_SUB    = "How I built an MCP server"
    S2_HEAD   = "Just an API key + URL"
    S3_BADGE  = "Built in 1 week"
    S5_HEAD   = "Full details in the description"
    S6_L1     = "Claude Code"
    S6_L2     = "builds it fast"
    S6_SUB    = "Build your own, with AI tools"
    CAP4      = "Two commands, any OS"
    FOOT4     = "* Install output is a real capture; setup values are examples"

# comments/labels are ASCII -> Consolas (identical for both langs)
S1_COMMENT = "# redmine × mcp"
S2_COMMENT = "# no cloud connectors — runs on your PC"
S3_COMMENT = "# before code: what should the AI do?"
S3_HL_NOTE = "# frequent flow → own tool"

# ================================================================
# per-language frame budgets (UNCHANGED from v4 timeline)
# ================================================================
if KO:
    B = dict(s1=305, s2a=138, s2b=130, s3base=69, s3tool=24, s3fin=126,
             s4total=488, s4switch=225, s5a=104, s5b=139, s6a=130, s6b=122)
else:
    B = dict(s1=241, s2a=112, s2b=115, s3base=30, s3tool=16, s3fin=94,
             s4total=320, s4switch=165, s5a=66, s5b=95, s6a=55, s6b=119)


# ---------------- Scene 1 : hook (static, cover-art card) ----------------
# v5.1: hook re-designed to embed the blog cover art inside a rounded IDE
# preview card. Source of truth: scratchpad/mock_s1cover.py. The card shows
# cover-art/redmine_v4.png cover-cropped with a rounded mask + PBORD border.
# The old "> MCP 서버 직접 제작기" prompt subhead is dropped (the card takes
# that space). S1 is still a single static still; subtitles are composited
# later from FRAGS/SUB_START exactly as before, so DO NOT draw a subtitle bar
# here. Frame budget B["s1"] (ko 305 / en 241) is unchanged.
S1_ART = os.path.join(ROOT, os.pardir, "cover-art", "redmine_v4.png")

def _cover_crop(im, tw, th, yoff_frac=0.42):
    iw, ih = im.size
    s = max(tw / iw, th / ih)
    nw, nh = int(iw * s), int(ih * s)
    im = im.resize((nw, nh))
    left = (nw - tw) // 2
    top = int((nh - th) * yoff_frac)
    return im.crop((left, top, left + tw, top + th))

def _art_card(img, x0, y0, x1, y1, radius=26):
    cw, ch = x1 - x0, y1 - y0
    art = Image.open(S1_ART).convert("RGB")
    art = _cover_crop(art, cw, ch)
    mask = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, cw, ch], radius=radius, fill=255)
    img.paste(art, (x0, y0), mask)
    ImageDraw.Draw(img).rounded_rectangle(
        [x0, y0, x1, y1], radius=radius, outline=PBORD, width=2)

def scene1():
    img, d = base("redmine-mcp  —  main")
    _art_card(img, X, 372, W - X, 952)   # preview card holding redmine_v4.png
    d = ImageDraw.Draw(img)
    d.text((X, 1006), S1_COMMENT, font=fmono(32), fill=GREEN)
    fh = fnoto(71, 800)   # sized so the widest line stays within the card (x<=984)
    d.text((X, 1074), S1_HEAD1, font=fh, fill=WHITE)
    if KO:
        d.text((X, 1176), "Claude Code", font=fh, fill=BLUE)
        xw = d.textlength("Claude Code", font=fh)
        d.text((X + xw + 16, 1176), "가 직접 다룬다", font=fh, fill=WHITE)
    else:
        d.text((X, 1176), "handled by ", font=fh, fill=WHITE)
        xw = d.textlength("handled by ", font=fh)
        d.text((X + xw, 1176), "Claude Code", font=fh, fill=BLUE)
    return img

save(scene1(), 1, "a", B["s1"])


# ---------------- Scene 2 : local + hookup (two-stage) ----------------
def scene2(full):
    img, d = base("server.py")
    d.text((X, 470), S2_COMMENT, font=fmono(34), fill=GREEN)
    panel(d, X, 560, W - X, 1060)
    fm = fmono(40)
    lx, ly = X + 44, 610
    def line(tokens, y):
        cx = lx
        for txt, col in tokens:
            d.text((cx, y), txt, font=fm, fill=col)
            cx += d.textlength(txt, font=fm)
    line([("transport ", WHITE), ("= ", MUT), ('"stdio"', STRING), ("   # local", DIM)], ly)
    line([("REDMINE_URL ", BLUE), ("= ", MUT), ('"https://…"', STRING)], ly + 78)
    line([("API_KEY ", BLUE), ("= ", MUT), ('"••••••••"', STRING)], ly + 156)
    if full:
        d.line([lx, ly + 250, W - X - 44, ly + 250], fill=PBORD, width=2)
        line([("→ ", GREEN), ("works with ", WHITE), ("any", GREEN), (" Redmine", WHITE)], ly + 300)
        d.text((X, 1150), S2_HEAD, font=fnoto(52, 700), fill=WHITE)
    return img

save(scene2(False), 2, "a", B["s2a"])
save(scene2(True),  2, "b", B["s2b"])


# ---------------- Scene 3 : one week + tool design (sequential reveal) ----------------
TOOLS = ["list_projects", "list_issues", "get_issue", "create_issue", "add_comment",
         "list_wiki_pages", "get_wiki", "update_wiki", "get_my_today", "list_enumerations"]
HL = TOOLS.index("get_my_today")

def scene3(n, final=False):
    """n = number of tools revealed; final adds the closing ']'."""
    img, d = base("tools.py")
    # badge (Korean text -> NotoSansKR, not mono)
    ft = fnoto(30, 700)
    bw = d.textlength(S3_BADGE, font=ft) + 52
    d.rounded_rectangle([X, 400, X + bw, 458], radius=29, outline=RED, width=2)
    d.text((X + 26, 414), S3_BADGE, font=ft, fill=(240, 150, 150))
    d.text((X, 494), S3_COMMENT, font=fmono(33), fill=GREEN)
    d.text((X, 556), "TOOLS = [", font=fmono(38), fill=MUT)
    fm = fmono(37)
    y = 626
    for i in range(n):
        t = TOOLS[i]
        hl = (i == HL)
        col = BLUE if hl else STRING
        d.text((X + 60, y), f'"{t}"', font=fm, fill=col)
        d.text((X + 60 + d.textlength(f'"{t}"', font=fm), y), ",", font=fm, fill=MUT)
        if hl:
            tx = X + 60 + d.textlength(f'"{t}",', font=fm) + 24
            d.text((tx, y), S3_HL_NOTE, font=fm, fill=DIM)
        y += 62
    if final:
        d.text((X, y + 4), "]", font=fmono(38), fill=MUT)
    return img

# base = badge + comment + "TOOLS = [" (no tools yet); then reveal tools 1..10;
# final adds "]".  Same reveal cadence as v4 (s3base / 10 x s3tool / s3fin).
save(scene3(0), 3, "base", B["s3base"])
for i in range(1, 11):
    save(scene3(i), 3, f"t{i:02d}", B["s3tool"])
save(scene3(10, final=True), 3, "final", B["s3fin"])


# ============ Scene 4 : terminal typing animation (kept), re-skinned ============
PROMPT = r"PS C:\Users\jun> "
CMD1 = "pipx install git+https://github.com/junstellar/redmine-mcp-jun.git"
CMD2 = "redmine-mcp-setup"
PIPX_OUT = [
    ("creating virtual environment...", MUT),
    ("determining package name from 'git+https://github.com/junstellar/redmine-mcp-jun.git'...", MUT),
    ("creating virtual environment...", MUT),
    ("installing redmine-mcp from spec 'git+https://github.com/junstellar/redmine-mcp-jun.git'...", MUT),
    ("DONE_LINE", None),
    ("  installed package redmine-mcp 0.3.0, installed using Python 3.12.10", BLUE),
    ("  These apps are now available", MUT),
    ("    - redmine-mcp-setup.exe", WHITE),
    ("    - redmine-mcp-uninstall.exe", WHITE),
    ("    - redmine-mcp.exe", WHITE),
]
MAXROWS = 16
SETUP_OUT = [
    ("CHK", " backed up ~/.claude.json"),
    ("Q",   " Redmine URL: https://redmine.internal.example"),
    ("Q",   " API key: ****************"),
    ("CHK", " registered mcpServers.redmine"),
]
# terminal body panel geometry (inside the IDE window, below the tab bar)
TX0, TX1 = 60, W - 60
TY0 = 380              # panel top
TPAD = 30
TLH = 44
tmono = fmono(30)
CHW = tmono.getlength("x")
COLS = int((TX1 - TX0 - 2 * TPAD) // CHW)
TBODY_H = MAXROWS * TLH + 2 * TPAD
TY1 = TY0 + TBODY_H

def wrapc(s):
    if not s:
        return [""]
    return [s[i:i + COLS] for i in range(0, len(s), COLS)]

def term_frame(typed1, out1=0, typed2=None, out2=0, caption=False, cursor=True):
    img, d = base("Windows PowerShell")
    panel(d, TX0, TY0, TX1, TY1)
    rows = []
    def add_plain(s, col):
        for ln in wrapc(s):
            rows.append([(ln, col, "mono")])
    cur_row_cursor = None
    wl = wrapc(PROMPT + CMD1[:typed1])
    for ln in wl:
        rows.append([(ln, WHITE, "mono")])
    if typed1 < len(CMD1) and cursor:
        cur_row_cursor = (len(rows) - 1, len(wl[-1]))
    for i in range(out1):
        txt, col = PIPX_OUT[i]
        if txt == "DONE_LINE":
            rows.append([("done! ", MUT, "mono"), ("✨ ", None, "emoji"),
                         ("\U0001F31F ", None, "emoji"), ("✨", None, "emoji")])
        else:
            add_plain(txt, col)
    if typed2 is not None:
        rows.append([("", WHITE, "mono")])
        l2 = PROMPT + CMD2[:typed2]
        rows.append([(l2, WHITE, "mono")])
        if typed2 < len(CMD2) and cursor:
            cur_row_cursor = (len(rows) - 1, len(l2))
        for k in range(out2):
            kind, body = SETUP_OUT[k]
            if kind == "CHK":
                rows.append([("✓", GREEN, "sym"), (body, WHITE, "mono")])
            else:
                rows.append([("?", GREEN, "mono"), (body, WHITE, "mono")])
        if out2 == len(SETUP_OUT):
            rows.append([("", WHITE, "mono")])
            rows.append([(PROMPT, WHITE, "mono")])
            if cursor:
                cur_row_cursor = (len(rows) - 1, len(PROMPT))
    scroll = max(0, len(rows) - MAXROWS)
    rows = rows[scroll:]
    if cur_row_cursor is not None:
        cur_row_cursor = (cur_row_cursor[0] - scroll, cur_row_cursor[1])
        if cur_row_cursor[0] < 0:
            cur_row_cursor = None
    x0 = TX0 + TPAD
    y = TY0 + TPAD + TLH // 2
    for ri, segs in enumerate(rows):
        x = x0
        for text, col, kind in segs:
            if kind == "mono":
                d.text((x, y + ri * TLH), text, font=tmono, fill=col, anchor="lm")
                x += tmono.getlength(text)
            elif kind == "sym":
                f = fother(SYM, 30)
                d.text((x, y + ri * TLH), text, font=f, fill=col, anchor="lm")
                x += f.getlength(text)
            else:
                f = fother(EMOJI, 30)
                try:
                    d.text((x, y + ri * TLH), text, font=f, anchor="lm",
                           embedded_color=True)
                except Exception:
                    d.text((x, y + ri * TLH), "*", font=tmono, fill=GREEN, anchor="lm")
                x += f.getlength(text)
    if cur_row_cursor is not None:
        ri, ci = cur_row_cursor
        cx = x0 + CHW * ci
        d.rectangle([cx + 2, y + ri * TLH - 17, cx + 2 + CHW, y + ri * TLH + 17], fill=WHITE)
    if caption:
        d.text((W // 2, TY1 + 74), CAP4, font=fnoto(50, 700), fill=WHITE, anchor="mm")
        d.text((W // 2, TY1 + 150), FOOT4, font=fnoto(28, 400), fill=DIM, anchor="mm")
    return img

# --- S4 animation choreography (identical frame budgets to v4) ---
fn = 0
def s4(img, frames):
    global fn
    save(img, 4, f"f{fn:03d}", frames)
    fn += 1

NOUT = len(PIPX_OUT)
if KO:
    TYPE_FR = 4
    s4(term_frame(0), 12)
    ks = list(range(2, len(CMD1) + 1, 2))
    if ks[-1] != len(CMD1):
        ks.append(len(CMD1))
    for k in ks:
        s4(term_frame(k), TYPE_FR)
    used = 12 + TYPE_FR * len(ks)
    room = B["s4switch"] - used
    six = [room // 6] * 6
    for i in range(room - sum(six)):
        six[i] += 1
    out_fr = six + [10, 8, 8, 8]
    for n, fr in zip(range(1, NOUT + 1), out_fr):
        s4(term_frame(len(CMD1), out1=n, cursor=False), fr)
    ks2 = list(range(2, len(CMD2) + 1, 2))
    if ks2[-1] != len(CMD2):
        ks2.append(len(CMD2))
    for k in ks2:
        s4(term_frame(len(CMD1), out1=NOUT, typed2=k), TYPE_FR)
    for n in range(1, 5):
        s4(term_frame(len(CMD1), out1=NOUT, typed2=len(CMD2), out2=n, cursor=False), 16)
    spent = B["s4switch"] + sum(out_fr[6:]) + TYPE_FR * len(ks2) + 64
    hold = B["s4total"] - spent
    chunks = [hold // 8] * 8
    for i in range(hold - sum(chunks)):
        chunks[i] += 1
    for j, fr in enumerate(chunks):
        s4(term_frame(len(CMD1), out1=NOUT, typed2=len(CMD2), out2=4,
                      caption=True, cursor=(j % 2 == 0)), fr)
else:
    TYPE_FR = 3
    SETUP_FR = 9
    s4(term_frame(0), 10)
    ks = list(range(2, len(CMD1) + 1, 2))
    if ks[-1] != len(CMD1):
        ks.append(len(CMD1))
    for k in ks:
        s4(term_frame(k), TYPE_FR)
    used = 10 + TYPE_FR * len(ks)
    room = B["s4switch"] - used
    six = [room // 6] * 6
    for i in range(room - sum(six)):
        six[i] += 1
    out_fr = six + [8, 6, 6, 6]
    for n, fr in zip(range(1, NOUT + 1), out_fr):
        s4(term_frame(len(CMD1), out1=n, cursor=False), fr)
    ks2 = list(range(2, len(CMD2) + 1, 2))
    if ks2[-1] != len(CMD2):
        ks2.append(len(CMD2))
    for k in ks2:
        s4(term_frame(len(CMD1), out1=NOUT, typed2=k), TYPE_FR)
    for n in range(1, 5):
        s4(term_frame(len(CMD1), out1=NOUT, typed2=len(CMD2), out2=n, cursor=False),
           SETUP_FR)
    spent = B["s4switch"] + sum(out_fr[6:]) + TYPE_FR * len(ks2) + 4 * SETUP_FR
    hold = B["s4total"] - spent
    chunks = [hold // 8] * 8
    for i in range(hold - sum(chunks)):
        chunks[i] += 1
    for j, fr in enumerate(chunks):
        s4(term_frame(len(CMD1), out1=NOUT, typed2=len(CMD2), out2=4,
                      caption=True, cursor=(j % 2 == 0)), fr)


# ---------------- Scene 5 : release github + see-description CTA (two-stage) ----------------
# v5.2: the old blog row (junstellar.github.io / "To the Moon") is gone. Stage b
# now reveals a "more -> see description ↓" line (ASCII/English in Consolas — no
# Korean glyphs in the mono face; Consolas covers U+2193 ↓) plus the headline.
def scene5(full):
    img, d = base("README.md")
    fh = fnoto(60, 800)
    d.text((X, 470), "## redmine-mcp", font=fh, fill=WHITE)
    tx = X + d.textlength("## redmine-mcp", font=fh) + 28
    d.rounded_rectangle([tx, 486, tx + 118, 540], radius=27, outline=GREEN, width=2)
    d.text((tx + 24, 496), "MIT", font=fmono(30, True), fill=GREEN)
    panel(d, X, 620, W - X, 1120)
    fm = fmono(36)
    lx, ly = X + 44, 680
    d.text((lx, ly), "repo", font=fm, fill=MUT)
    d.text((lx + 180, ly), "→", font=fm, fill=DIM)
    d.text((lx + 240, ly), "github.com/junstellar/", font=fm, fill=BLUE)
    d.text((lx + 240, ly + 46), "redmine-mcp-jun", font=fmono(36, True), fill=BLUE)
    if full:
        d.line([lx, ly + 130, W - X - 44, ly + 130], fill=PBORD, width=2)
        d.text((lx, ly + 170), "more", font=fm, fill=MUT)
        d.text((lx + 180, ly + 170), "→", font=fm, fill=DIM)
        d.text((lx + 240, ly + 170), "see description ↓", font=fmono(36, True), fill=GREEN)
        d.text((X, 1180), S5_HEAD, font=fnoto(50, 700), fill=WHITE)
    return img

save(scene5(False), 5, "a", B["s5a"])
save(scene5(True),  5, "b", B["s5b"])


# ---------------- Scene 6 : CTA outro (two-stage + blinking cursor) ----------------
def scene6(full, cursor_on=True):
    img, d = base("$ build")
    d.text((X, 600), "$", font=fmono(64), fill=GREEN)
    d.text((X + 70, 604), S6_L1, font=fnoto(96, 800), fill=WHITE)
    d.text((X, 744), S6_L2, font=fnoto(96, 800), fill=BLUE)
    if full:
        d.line([X, 900, W - X, 900], fill=PBORD, width=2)
        d.text((X, 950), S6_SUB, font=fnoto(50, 500), fill=MUT)
        d.text((X, 1060), "build your own", font=fmono(46), fill=GREEN)
        if cursor_on:
            cx = X + d.textlength("build your own", font=fmono(46)) + 14
            d.rectangle([cx, 1058, cx + 22, 1108], fill=GREEN)
    return img

save(scene6(False), 6, "a", B["s6a"])
# second half: blinking cursor. split s6b into alternating on/off chunks.
def emit_s6b(total):
    chunks, per = [], 15  # ~0.5s blink
    t = total
    on = True
    while t > 0:
        f = min(per, t)
        chunks.append((f, on))
        t -= f
        on = not on
    return chunks
for idx, (fr, on) in enumerate(emit_s6b(B["s6b"])):
    save(scene6(True, cursor_on=on), 6, f"b{idx:02d}", fr)


# ============ composite timed subtitles + hardlink frame sequences ============
total = 0
for name, items in scenes.items():
    sc = int(name[1:])
    starts, frags = SUB_START[sc], FRAGS[sc]
    seq = os.path.join(ROOT, f"seq_{LANG}_{name}")
    if os.path.isdir(seq):
        for fname in os.listdir(seq):
            os.remove(os.path.join(seq, fname))
    else:
        os.makedirs(seq)
    n = 0
    cache = {}  # (base_path, frag_idx) -> composited png path
    for p, fr in items:
        for _ in range(fr):
            k = sum(1 for s in starts if n >= s) - 1  # active fragment index
            key = (p, k)
            if key not in cache:
                sub_p = p[:-4] + f"_sub{k}.png"
                draw_subtitle(Image.open(p), frags[k]).save(sub_p)
                cache[key] = sub_p
            os.link(cache[key], os.path.join(seq, f"{n:05d}.png"))
            n += 1
    total += n
    print(f"{LANG} {name}: {n} frames = {n / FPS:.4f}s, "
          f"sub cuts at {starts} -> {len(cache)} composited stills")
print(f"total {total} frames, video = {total / FPS - 0.5 * (len(scenes) - 1):.4f}s")
print("done", LANG)
