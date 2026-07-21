---
title: "Making Games with AI #4 — 'Dodge the Falling Stuff', Now With a Gameplay Clip (Build in Public #4)"
description: "The fourth game in the lab is a one-hand action game, 'Dodge'. Slide left and right to avoid falling meteors and bombs, and grab stars for a score burst! This episode also has my first 10-second gameplay clip — including how I made the game play itself and recorded it. Build in Public #4."
slug: "ai-game-lab-build-4"
date: 2026-07-21T09:00:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "game dev", "build in public", "arcade", "action", "indie hacker", "AI coding"]
---

By [last time](/p/ai-game-lab-build-3/), the game lab had three games — 🎨 a picture quiz (brains), 🟩 a Korean Wordle (habit), 🍰 a dessert stacker (hand-feel). The one slot still empty was **pure action**. So the fourth is a reflex game — **Dodge**.

Watching beats reading, so this time I'm leading with a **10-second gameplay clip** 👇

{{< mp4 src="dodge-play.mp4" poster="dodge-play-poster.webp" >}}

👉 **[Go play Dodge yourself](/games/dodge/)**

## What the game is

You learn it in three seconds:

- Move the 🚀 rocket **left/right by dragging** (or ← → on PC)
- **Avoid the falling 🪨 meteors and 💣 bombs**
- Grab a **⭐ star** for a score burst; grab a **💗 heart** to restore a life (max 5)
- Start with 3 hearts; each hit costs one, and it's over at zero
- **It gets faster the longer you last.** Score = how long you survive + stars

Results share as `🕹️ Dodge — N points!`, and your best score and daily streak stack up like in the other games. It's one-handed, so it feels great on a phone.

## What's new this episode — making the game play itself

That clip up top? I didn't play it — the **game played itself, and I recorded that**. It was my first time doing this, and the method was fun:

1. I bolted a **simple dodge AI** onto the game — every moment it steers the rocket "if the nearest bomb is on the left, go right; if there's no danger, drift toward a nearby star"
2. I let it run while **recording the canvas** (the browser's screen-capture)
3. Then turned that into a **10-second mp4** and embedded it here

So I basically got the game to demo *itself*. Attaching a short clip like this to every game makes these posts way more alive.

## And a difficulty tweak

At first it was a bit easy ("wait, I'm not dying?"). So I nudged the **fall speed and spawn rate up a touch**, so it's relaxed early and tightens up from the middle. These little feel adjustments matter more than you'd think in an action game.

## The game lab now has four flavors

| | Game | Flavor |
|---|------|--------|
| 🎨 | [Guess the AI Picture](/games/guess-image/) | Brains (quiz) |
| 🟩 | [Guess the Korean Word](/games/hangul-word/) | Habit (daily) |
| 🍰 | [Dessert Tower](/games/stack-tower/) | Hand-feel (arcade) |
| 🕹️ | [Dodge](/games/dodge/) | Reflex (action) |

Brains, habit, hand-feel, reflex — whatever mood you show up in, the [game lab](/games/) now has something for it.

---

**[Play a round of Dodge](/games/dodge/)** and tell me your score. For the record, I keep flying into bombs while reaching for stars. 🚀

*Next time: a fifth game, or maybe the report card on whether anyone actually came to play.*
