# -*- coding: utf-8 -*-
"""Re-synthesize ComfyUI-short KO/EN narration WITH WordBoundary marks and
compute scene-local subtitle start frames (SUB_START) for each fragment.

Audio for the final mux uses the pre-generated tts_comfy_{ko,en}/scene*.mp3
(stable path). This script only extracts word timing: it resynthesizes with the
same voice/rate to a temp dir, aligns fragment boundaries to WordBoundary
offsets, and writes subs_comfy.json = {lang: {scene: [start_frame, ...]}}.
Also prints resynth vs existing duration so we can confirm they match.
"""
import asyncio, json, os, subprocess
import edge_tts

ROOT = os.path.dirname(os.path.abspath(__file__))
FPS = 30.0
LEAD = 0.3  # narration adelay lead (seconds)

FRAGS_KO = {
    1: ["클로드의 유일한 아쉬움, 그림을 못 그린다는 거였죠.",
        "노트북 GPU로 도는 오픈웨이트 모델을 붙였더니, 퀄리티가 기대 이상이었어요."],
    2: ["클라우드 API는 돈 들고 워터마크도 박혀요.",
        "그래서 무료에 무제한, 오프라인인 ComfyUI를 골랐습니다."],
    3: ["필요한 건 GPU 메모리 8기가.",
        "요즘 웬만한 그래픽카드면 충분하고, 한 장에 약 30초면 나와요."],
    4: ["받고, 깔고, 모델 내려받아 서버 켜면 끝.",
        "클로드가 호출할 스크립트만 붙이면 됩니다."],
    5: ["스킬 하나 등록하면, '고양이 그려줘' 한마디로 생성까지 알아서.",
        "설치법은 설명란에 있어요."],
    6: ["무료로, 내 PC에서.",
        "여러분도 직접 붙여보세요."],
}
FRAGS_EN = {
    1: ["The one thing Claude couldn't do was draw.",
        "So I ran an open-weight model on my laptop GPU — and the quality blew me away."],
    2: ["Cloud APIs cost money and add watermarks.",
        "So I picked ComfyUI: free, unlimited, offline."],
    3: ["You just need 8 GB of GPU memory.",
        "Most modern cards clear it, and it's about 30 seconds an image."],
    4: ["Clone it, install GPU PyTorch, grab the model, run the server.",
        "Then add a script for Claude to call."],
    5: ["Register one skill, say 'draw a cat', and Claude generates it.",
        "Full setup's in the description."],
    6: ["Free, on your own PC.",
        "Go wire it up yourself."],
}


async def synth_with_marks(text, voice, rate, out_mp3):
    kw = {"rate": rate} if rate else {}
    com = edge_tts.Communicate(text, voice, boundary="WordBoundary", **kw)
    marks = []
    with open(out_mp3, "wb") as f:
        async for chunk in com.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                marks.append((chunk["offset"] / 1e7, chunk["text"]))
    return marks


def dur(p):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                        "-of", "csv=p=0", p], capture_output=True, text=True)
    return float(r.stdout.strip())


def frag_starts(frags, marks, ndur, edur):
    """Return scene-local start frame for each fragment.
    Fragment 0 -> frame 0. Fragment k (k>=1) -> round((offset_k*scale + LEAD)*FPS)
    where offset_k is the WordBoundary offset of the first word of fragment k and
    scale = edur/ndur maps the resynth timeline onto the ACTUAL audio timeline
    (edge-tts durations vary slightly run-to-run). Word index = cumulative
    whitespace-token count of preceding fragments. Falls back to
    proportional-by-char (over the actual audio duration) if marks are too few."""
    counts = [len(f.split()) for f in frags]
    starts = [0]
    total_words = sum(counts)
    use_marks = len(marks) >= total_words - 1  # tolerate 1 missing (e.g. em-dash)
    scale = edur / ndur if ndur else 1.0
    clen = [len(f.replace(" ", "")) for f in frags]
    ctot = sum(clen)
    cum_c = 0
    cum_w = 0
    for k in range(1, len(frags)):
        cum_w += counts[k - 1]
        cum_c += clen[k - 1]
        off = None
        if use_marks and cum_w < len(marks):
            off = marks[cum_w][0] * scale
        if off is None:
            off = (cum_c / ctot) * edur
        fr = max(1, round((off + LEAD) * FPS))
        starts.append(fr)
    return starts, use_marks


async def main():
    out = {}
    tmp = os.path.join(ROOT, "_marktmp")
    os.makedirs(tmp, exist_ok=True)
    for lang, frags, voice, rate in (
            ("ko", FRAGS_KO, "ko-KR-HyunsuMultilingualNeural", None),
            ("en", FRAGS_EN, "en-US-AndrewNeural", "+4%")):
        out[lang] = {}
        for i in range(1, 7):
            text = " ".join(frags[i])
            mp3 = os.path.join(tmp, f"{lang}_s{i}.mp3")
            marks = await synth_with_marks(text, voice, rate, mp3)
            ndur = dur(mp3)
            exist = dur(os.path.join(ROOT, f"tts_comfy_{lang}", f"scene{i}.mp3"))
            starts, used = frag_starts(frags[i], marks, ndur, exist)
            out[lang][str(i)] = starts
            print(f"{lang} s{i}: exist={exist:.3f} resynth={ndur:.3f} "
                  f"diff={ndur-exist:+.3f} marks={len(marks)} "
                  f"starts={starts} {'MARKS' if used else 'PROP'}")
    with open(os.path.join(ROOT, "subs_comfy.json"), "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print("wrote subs_comfy.json")


asyncio.run(main())
