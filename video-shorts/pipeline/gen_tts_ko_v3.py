# -*- coding: utf-8 -*-
"""Korean narration v3 (user-approved script), Hyunsu natural rate, 6 scenes."""
import asyncio, json, os, subprocess

import edge_tts

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tts_ko_v3")
os.makedirs(OUT, exist_ok=True)
VOICE = "ko-KR-HyunsuMultilingualNeural"

SCENES = {
    1: "레드마인 쓰시는 분들 많으시죠. 클로드 코드가 레드마인 일감을 직접 다룰 수 있게, MCP 서버를 만들어봤습니다.",
    2: "클라우드 커넥터 없이, 내 PC에서 바로 돌아가게 구현했고 API 키와 주소를 이용해 연동할 수 있습니다.",
    3: "만드는 데는 일주일이면 충분했는데요, 그 과정을 짧게 소개합니다. 코딩을 시작하기 전에, AI가 뭘 해야 하는지부터 적었고 필요한 도구를 열 개로 정리했습니다.",
    4: "클로드 코드를 이용해서 기능 구현은 쉽게 했는데 누구나 쉽게 설치할 수 있게 만드는 게 문제였습니다. 고민 끝에 결국 파이썬을 이용한 pipx 방식으로 배포했고, 이제 어느 OS든 두 줄이면 끝입니다.",
    5: "제가 작성한 코드는 깃허브에 공개했습니다. 자세한 제작기는 제 블로그, 투더문에 정리해뒀습니다.",
    6: "클로드 코드를 이용하면 금방 만들 수 있을 거예요. AI 도구를 활용해 직접 만들어보세요.",
}


async def main():
    await asyncio.gather(*(
        edge_tts.Communicate(t, VOICE).save(os.path.join(OUT, f"scene{i}.mp3"))
        for i, t in SCENES.items()))
    durations = {}
    for i in SCENES:
        p = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", os.path.join(OUT, f"scene{i}.mp3")],
            capture_output=True, text=True)
        durations[i] = round(float(p.stdout.strip()), 2)
    print(json.dumps(durations, indent=1))
    print("total:", round(sum(durations.values()), 2))


asyncio.run(main())
