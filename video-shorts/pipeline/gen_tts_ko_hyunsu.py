# -*- coding: utf-8 -*-
"""Regenerate all Korean narration with Hyunsu voice at natural rate."""
import asyncio, json, os, subprocess

import edge_tts

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tts_ko")
VOICE = "ko-KR-HyunsuMultilingualNeural"

SCENES = {
    1: "레드마인을 클로드 코드가 직접 다루게 해봤습니다. 일주일의 기록입니다.",
    2: "클라우드 커넥터 없이, 내 PC에서 도는 로컬 MCP 서버입니다. 어떤 레드마인이든 붙습니다.",
    3: "코드보다 먼저, AI가 뭘 해야 하는지부터 적었습니다. 도구 딱 열 개로 정리됐죠.",
    4: "코드는 쉬웠는데 배포가 문제였습니다. PEP 668과 싸운 끝에 pipx로 갈아엎었고, 이제 어느 OS든 두 줄이면 끝.",
    5: "교훈 셋. pipx 쓰기, 절대경로 고정, 그리고 설정 수정 전 무조건 백업.",
    6: "서버는 파이썬 사백 줄. 진짜 일은 배포와 키 관리, 그리고 설명 튜닝입니다.",
    7: "코드는 깃허브에 공개했습니다. 그래도 직접 만들어 보세요. 훨씬 많이 남습니다.",
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
