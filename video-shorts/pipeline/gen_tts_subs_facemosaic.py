# -*- coding: utf-8 -*-
"""Face-mosaic short: regenerate narration (KO Hyunsu / EN Andrew) into
tts_facemosaic_{lang}/scene*.mp3 AND capture WordBoundary timing to write
subs_facemosaic.json = {lang: {scene: [0, frag2_start_frame]}} (30fps)."""
import asyncio, json, os, subprocess
import edge_tts

ROOT = os.path.dirname(os.path.abspath(__file__))
FPS = 30.0

FRAGS_KO = {
    1: ["사진 올릴 때 같이 찍힌 사람 얼굴, 가려야 할 때 있죠.",
        "서버에 안 올리고 브라우저 안에서만 가리는 도구를 만들었어요."],
    2: ["보통은 모르는 사이트에 얼굴 사진을 올려야 하는데,",
        "이건 사진이 브라우저 밖으로 아예 안 나갑니다."],
    3: ["비결은 온디바이스 AI.",
        "구글 MediaPipe로 얼굴 찾는 것부터 가리는 것까지 전부 내 컴퓨터 안에서 끝나요."],
    4: ["가리는 방식은 넷 — 모자이크, 블러, 검은 박스, 이모지.",
        "놓친 얼굴은 직접 드래그로 추가하면 됩니다."],
    5: ["이것도 Claude Code로 만들었어요.",
        "도구랑 자세한 설명은 설명란에."],
    6: ["보안은 직접 만드는 게 제일 확실하죠.",
        "귀찮으면 제가 만든 거 써보세요."],
}
FRAGS_EN = {
    1: ["When you post a photo, sometimes you need to hide a bystander's face.",
        "So I built a tool that does it entirely in your browser — nothing goes to a server."],
    2: ["Usually you'd upload the face to some random site.",
        "Here, the photo never leaves your browser at all."],
    3: ["The trick is on-device AI.",
        "Google's MediaPipe finds the faces and masks them, all on your own computer."],
    4: ["Four ways to hide: mosaic, blur, black box, or emoji.",
        "Missed a face? Just drag to add it."],
    5: ["I built this with Claude Code too.",
        "The tool and the full write-up are in the description."],
    6: ["For privacy, building your own is the surest bet.",
        "Too much hassle? Just use mine."],
}
JOBS = [("tts_facemosaic_ko", "ko-KR-HyunsuMultilingualNeural", None, FRAGS_KO),
        ("tts_facemosaic_en", "en-US-AndrewNeural", "+4%", FRAGS_EN)]


async def one(folder, voice, rate, idx, frag1, frag2):
    full = frag1 + " " + frag2
    kw = {"rate": rate} if rate else {}
    comm = edge_tts.Communicate(full, voice, **kw)
    offs = []   # SentenceBoundary start offsets (seconds), in order
    with open(os.path.join(ROOT, folder, f"scene{idx}.mp3"), "wb") as fo:
        async for ch in comm.stream():
            if ch["type"] == "audio":
                fo.write(ch["data"])
            elif ch["type"] == "SentenceBoundary":
                offs.append(ch["offset"] / 1e7)
    # frag2 begins after all sentence-terminators contained in frag1.
    n_frag1_sent = sum(frag1.count(c) for c in ".?!")
    if 1 <= n_frag1_sent < len(offs):
        t2 = offs[n_frag1_sent]      # exact boundary
    else:
        t2 = None                    # mid-sentence split -> proportional fallback
    return idx, t2


async def main():
    subs = {}
    for folder, voice, rate, frags in JOBS:
        os.makedirs(os.path.join(ROOT, folder), exist_ok=True)
        lang = "ko" if folder.endswith("ko") else "en"
        res = await asyncio.gather(*[one(folder, voice, rate, i, f[0], f[1])
                                     for i, f in frags.items()])
        d = {}
        for idx, t2 in res:
            dur = float(subprocess.run(
                ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
                 "-of", "csv=p=0", os.path.join(ROOT, folder, f"scene{idx}.mp3")],
                capture_output=True, text=True).stdout.strip())
            if t2 is None:   # char-proportional fallback (mid-sentence split)
                f1, f2 = frags[idx]
                t2 = dur * (len(f1) + 1) / (len(f1) + 1 + len(f2))
            d[str(idx)] = [0, int(round(t2 * FPS))]
            print(f"{lang} s{idx}: dur={dur:.3f}s frag2@{t2:.3f}s -> frame {d[str(idx)][1]}")
        subs[lang] = d
    with open(os.path.join(ROOT, "subs_facemosaic.json"), "w", encoding="utf-8") as f:
        json.dump(subs, f, indent=1)
    print("wrote subs_facemosaic.json")


asyncio.run(main())
