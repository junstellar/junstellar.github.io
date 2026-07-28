---
title: "Making Games with AI #5 — Tossing Paper into a Trash Can, but Made to *Feel* Like a Game (Build in Public #5)"
description: "The fifth game in the lab is 'Paper Hoop'. This time, instead of adding another game, I focused on polishing one game from 'it works' to 'it actually feels like a game'. Sound, rim physics, an on-fire combo, three-pointers — and the background was painted by the graphics card sitting in my house (ComfyUI). Polish comes from feel, not feature count. Build in Public #5."
slug: "ai-game-lab-build-5"
date: 2026-07-28T09:00:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "game dev", "build in public", "arcade", "physics game", "indie hacker", "AI coding", "ComfyUI"]
---

By [last time](/p/ai-game-lab-build-4/), the game lab had four — 🎨 image quiz, 🟩 Korean Wordle, 🍰 dessert stack, 🕹️ dodge. The fifth is **Paper Hoop**. But this episode is a little different. Instead of adding yet another game, I focused on **taking one game from "it works" all the way to "it actually feels like a game."**

Watching beats reading, so here's the **gameplay clip** first 👇

{{< mp4 src="paper-hoop-play.mp4" poster="paper-hoop-play-poster.webp" >}}

👉 **[Go play Paper Hoop yourself](/games/paper-hoop/)**

## What is it

You'll get it in three seconds:

- **Drag anywhere on the screen and let go** to fling a crumpled paper ball into the trash can (you don't even have to grab the ball)
- **Straight through the middle = swish (2 pts)**; off the rim or backboard = **bank (1 pt)**
- Mind the **wind**! Score in a row and you go **🔥 ON FIRE** (double points)
- Miss three times and it's over. Best score, totals, and daily streak stack up like the other games

## At first it "didn't feel like a game"

Honestly, the first version was weak. The throw was so fast the paper just **blinked out of existence** — zero feel. So:

- Made the flight **2× slower** (same arc, same difficulty, just the visible speed)
- Added a **trailing streak** + a floor shadow + a **bounce off the floor** on a miss

That alone got an "oh, now it's a game" out of me. Turns out **80% of polish is feel.**

## Then I pushed it all the way to "premium"

I could've stopped there, but I got curious how far it could go, so I threw everything in:

- 🔊 **Sound** — **zero asset files**. The whoosh on launch, the "shhk" swish, the "thunk-ding" bank — all **synthesized in code** with WebAudio
- 🏀 **Physics** — a rattling **in-and-out** off the two rims, a **backboard bank shot**, and a **cloth net that swishes** at the mouth
- 🔥 **ON FIRE** — a gauge fills as you score in a row; max it out and the **ball catches fire for 2× points** (an NBA Jam homage)
- 🎯 **Three-point line** — the farther the can, the more it's worth. **Backspin (Magnus)** curves the flight a touch
- ✨ Plus little bits of **juice** — hit-stop, a camera punch-zoom, a ribbon trail

## The graphics card in my house painted the background

My favorite part. I generated the office-interior background **right on the graphics card sitting in my house (ComfyUI/SDXL)** and dropped it in. It's putting to use [the ComfyUI setup I installed on my laptop a while back](/p/claude-local-image-generation/). It's a lightweight game that runs straight in the browser, yet the backdrop looks hand-painted. I even added **day/night themes**.

![Night theme + ON FIRE — the paper ball catches fire](paper-hoop-fire.webp)

## Hooks to keep you coming back

- 📅 **Daily challenge** — seeded by the date, so everyone gets the **same cans and wind** that day. Made for "what'd you get today?"
- 🏅 **Achievements** · 🖼️ **share your result as an image card** · ▶️ **replay your best shot**
- ♿ **Accessibility** — respects reduced-motion (no queasiness) and a colorblind-safe power indicator

## The last lesson: a tiny bit of UX saves the whole game

After building it all, I hit a dealbreaker while playing. The slingshot was anchored to **the ball (down in the bottom-left corner)**, so there was no room to pull back. Switching it to **"press anywhere and pull back relative to that point"** changed everything. That **one-line control fix** mattered far more than any of the twenty flashy features.

## The game lab is now five

| | Game | Vibe |
|---|------|------|
| 🎨 | [Guess the AI Image](/games/guess-image/) | Brain (quiz) |
| 🟩 | [Korean Word Guess](/games/hangul-word/) | Habit (daily) |
| 🍰 | [Dessert Stack](/games/stack-tower/) | Timing (arcade) |
| 🕹️ | [Dodge](/games/dodge/) | Reflex (action) |
| 🗑️ | [Paper Hoop](/games/paper-hoop/) | Aim (physics) |

Brain, habit, timing, reflex, aim — the [game lab](/games/) now has five flavors.

---

**[Play a round of Paper Hoop](/games/paper-hoop/)** and tell me your score. Sink three swishes in a row and you catch fire. 🔥

*Next time: either a sixth game, or a report card on whether anyone actually showed up to play.*
