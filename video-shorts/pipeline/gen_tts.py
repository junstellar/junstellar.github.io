# -*- coding: utf-8 -*-
"""Generate English narration audio per scene using edge-tts."""
import asyncio, json, os, subprocess, sys

import edge_tts

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tts")
os.makedirs(OUT, exist_ok=True)

VOICE = "en-US-AndrewNeural"

SCENES = {
    1: "I made Claude Code talk directly to our company's Redmine. Here's my one-week build log.",
    2: "Our Redmine sits on a private network, so cloud connectors won't work. So I built a local MCP server that runs right on my PC, over stdio.",
    3: "Before writing any code, I listed what the AI should actually do, and boiled it down to just ten tools, like get-my-today for daily tasks.",
    4: "The code was the easy part. Deployment wasn't. After fighting PEP six sixty-eight, I repackaged everything for pipx. Now it installs with one command, on any OS.",
    5: "Three hard-earned lessons: use pipx, pin absolute paths, and always back up your config before touching it.",
    6: "The server itself is just four hundred lines of Python. The real work is deployment, key management, and tuning your tool descriptions.",
    7: "The code's on GitHub, MIT licensed. But honestly, build your own. You'll learn a lot more.",
}


async def gen(idx: int, text: str) -> None:
    mp3 = os.path.join(OUT, f"scene{idx}.mp3")
    await edge_tts.Communicate(text, VOICE, rate="+4%").save(mp3)


async def main() -> None:
    await asyncio.gather(*(gen(i, t) for i, t in SCENES.items()))
    durations = {}
    for i in SCENES:
        mp3 = os.path.join(OUT, f"scene{i}.mp3")
        p = subprocess.run(
            ["ffprobe", "-v", "quiet", "-show_entries", "format=duration",
             "-of", "csv=p=0", mp3],
            capture_output=True, text=True)
        durations[i] = round(float(p.stdout.strip()), 2)
    print(json.dumps(durations, indent=1))
    print("total:", round(sum(durations.values()), 2))


asyncio.run(main())
