# -*- coding: utf-8 -*-
"""Re-synthesize KO/EN v3 narration with WordBoundary marks -> tts_{ko,en}_v4 + marks JSON."""
import asyncio, json, os, subprocess

import edge_tts

ROOT = os.path.dirname(os.path.abspath(__file__))

SCENES_KO = {
    1: "레드마인 쓰시는 분들 많으시죠. 클로드 코드가 레드마인 일감을 직접 다룰 수 있게, MCP 서버를 만들어봤습니다.",
    2: "클라우드 커넥터 없이, 내 PC에서 바로 돌아가게 구현했고 API 키와 주소를 이용해 연동할 수 있습니다.",
    3: "만드는 데는 일주일이면 충분했는데요, 그 과정을 짧게 소개합니다. 코딩을 시작하기 전에, AI가 뭘 해야 하는지부터 적었고 필요한 도구를 열 개로 정리했습니다.",
    4: "클로드 코드를 이용해서 기능 구현은 쉽게 했는데 누구나 쉽게 설치할 수 있게 만드는 게 문제였습니다. 고민 끝에 결국 파이썬을 이용한 pipx 방식으로 배포했고, 이제 어느 OS든 두 줄이면 끝입니다.",
    5: "제가 작성한 코드는 깃허브에 공개했습니다. 자세한 제작기는 제 블로그, 투더문에 정리해뒀습니다.",
    6: "클로드 코드를 이용하면 금방 만들 수 있을 거예요. AI 도구를 활용해 직접 만들어보세요.",
}
SCENES_EN = {
    1: "If you use Redmine, this one's for you. I built an MCP server so Claude Code can work your Redmine issues directly.",
    2: "No cloud connectors. It runs right on your PC, and connects with just your API key and server address.",
    3: "It took me just one week — here's the quick build story. Before writing any code, I listed what the AI should do, and boiled it down to ten tools.",
    4: "Building the features with Claude Code was easy. Making it easy for anyone to install was the hard part. I settled on pipx — and now it's two commands, on any OS.",
    5: "The code is public on GitHub, and the full build story is on my blog, To the Moon.",
    6: "With Claude Code, you can build one fast. Grab an AI tool and build your own.",
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


async def main():
    for lang, scenes, voice, rate in (
            ("ko", SCENES_KO, "ko-KR-HyunsuMultilingualNeural", None),
            ("en", SCENES_EN, "en-US-AndrewNeural", "+4%")):
        out = os.path.join(ROOT, f"tts_{lang}_v4")
        os.makedirs(out, exist_ok=True)
        data = {}
        for i, t in scenes.items():
            mp3 = os.path.join(out, f"scene{i}.mp3")
            marks = await synth_with_marks(t, voice, rate, mp3)
            old = dur(os.path.join(ROOT, f"tts_{lang}_v3", f"scene{i}.mp3"))
            new = dur(mp3)
            data[str(i)] = {"duration": new, "old_duration": old, "marks": marks}
            print(f"{lang} s{i}: old={old:.3f} new={new:.3f} diff={new-old:+.3f} "
                  f"marks={len(marks)} first={marks[0][0]:.3f} last={marks[-1][0]:.3f}")
        with open(os.path.join(ROOT, f"marks_{lang}.json"), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)


asyncio.run(main())
