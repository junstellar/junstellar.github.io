---
title: "Making Games with AI #8 — Dropping to 1,200m to Fill a 27-Fish Encyclopedia (Build in Public #8)"
description: "The eighth game in the lab is 'Deep Fishing'. Drop from the surface down to the 1,200m abyss, land fish, and fill a 27-species encyclopedia. All 27 fish were painted with my local ComfyUI, and the 'something feels off' problems weren't fixed by feel — I found each cause in the code. Build in Public #8."
slug: "ai-game-lab-build-8"
date: 2026-08-10T09:00:00+09:00
draft: false
image: "deep-fishing-poster.webp"
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "game dev", "build in public", "fishing game", "collection", "indie hacker", "AI coding", "ComfyUI"]
---

After the shunting yard in [the last post](/p/ai-game-lab-build-7/), game number eight is **Deep Fishing**. You drop from the surface down to the **1,200m abyss**, land fish, and fill a **27-species encyclopedia**.

It's the first game in the lab with **collecting** in it. The others leave only a score when the run ends; here the fish you catch **stay with you forever.**

{{< mp4 src="deep-fishing-play.mp4" poster="deep-fishing-poster.webp" >}}

👉 **[Go play Deep Fishing yourself](/games/deep-fishing/)**

## What it is

Three taps and you've got one.

- ① **Pick your depth** — tap the moving bar. Deeper means rarer and harder
- ② **Set the hook** — the fish swims up and **nibbles at the bait** (fake), then tap the instant it **actually bites**
- ③ **Fight** — hold to reel in, release to give line. Keep the **tension in the green band**

A run is 12 casts. There are **27 species, from an anchovy to a 🐉kraken**, and the better you keep the tension centered, the bigger your **accuracy bonus** (up to +85%).

![The encyclopedia — caught fish in color, the rest in silhouette](deep-fishing-dex.webp)

## All 27 fish were painted with ComfyUI

I generated every one of them with [the **ComfyUI** I installed on my laptop a while back](/p/claude-local-image-generation/). And once again, generating was only half the job — the whale shark came with a white background box, the stingray dragged the seabed along with it, and the yellowtail showed up as two overlapping fish.

I auto-detected the background color and made it transparent, re-cropped tight to the subject, and re-generated with different prompts when that wasn't enough. **Reshaping what ComfyUI gives you to fit the game is half the work** — confirmed again.

## The first version felt like setting the hook into thin air

I got it running and played it myself, and it felt wrong. The screen had **nothing but a line**, and with nothing visible the words "Tap now!" would just appear. There was no way to know what you were reacting to.

So I decided to **actually show the fish.**

- The fish **swims in from the side**
- It **nibbles at the bait** (the float twitches slightly = a fake bite)
- The moment it **really bites**, the float plunges and a splash bursts out

That turned "tap too early and you lose it" into a rule **your eyes can understand.** Telling fakes from the real thing became the skill.

## The fish looked like they had black backgrounds — but measuring said otherwise

Playing on, some fish looked like they had **a black background stuck to them.** I figured the background removal had failed. So I measured all 27 sprites.

**Not a single one had leftover background.** The cause I'd guessed was wrong.

The real cause was elsewhere: **the fish and the water were nearly the same brightness.**

| Fish | Fish brightness | Water at that depth | Difference |
|---|---|---|---|
| Sea turtle | 127 | 130 | **3** |
| Vampire squid | 45 | 20 | 25 |

Below 700m the water sits under brightness 20, and deep-sea fish are dark too. It was **a dark object on a dark background.**

So I put a **deep-sea lamp on the hook.** It lights the area around the bait, the fish becomes visible, and it fits the deep-sea mood. I added a soft glowing rim around the hooked fish too.

> If I'd gone with my gut and re-generated the sprites, I'd have burned the time for nothing. Measuring showed the problem was somewhere else entirely.

## The line stayed put while only the fish moved up

Reeling in felt disconnected, so I opened the code: the end of the line was **pinned to the center of the screen.** Only the fish moved up, so the two looked detached.

- I **anchored the line to the fish's mouth.** As it rises, the line shortens with it
- **The line's shape now reflects tension** — straight when taut, a sagging curve when slack, and **red and thicker** near the breaking point
- The **depth counter drops** as you reel, and the water brightens on the way up

![The moment of the catch — with the accuracy bonus](deep-fishing-catch.webp)

## It still felt lacking — the third diagnosis

Even after all that, something still nagged at me. This time I didn't guess; I **went straight into the code.** Three things came out.

**① The fish wasn't swimming.** There was **not a single rotation anywhere in the code.** A still image was sliding around. Just tilting the body while swimming and twisting it hard during a struggle changed everything.

**② There was no journey down to the deep.** The descent code read:

```js
curDepth += Math.max(3, targetDepth*0.012)   // always 1.4 seconds
```

**100m and 1,200m took exactly the same time.** A deep-sea fishing game with zero sense of going deep. I made the descent proportional to depth (up to 3.5s), made the background stream upward, and had **`200m Twilight` `500m Midnight` `900m Abyss`** markers sweep past.

**③ The line started in mid-air.** No boat, no surface. I added **a boat and waves** and had the line come down from it. Go deep and the surface fades into the dark; reel up and it reappears.

![On the way down — depth markers sweeping past](deep-fishing-descent.webp)

## Size tells you the weight

I'd scaled the fish by **rarity**, which made a **1kg pufferfish look as big as a 900kg whale shark.** I switched to weight (log scale) and **rolled the weight before the bite** so the size you see matches the fish you land. Now one glance tells you if it's a monster or a minnow.

## The tug-of-war nearly wrecked the game

Last, I added a moment where the **fish dives** and you have to let go and hold on. Then I ran the simulation:

| | Before | Right after |
|---|---|---|
| Catch rate | 83% | **33%** |

**The catch rate halved**, and fights could deadlock and never finish. I dialed down the pull force, the progress loss, and how often it fires. Now it adds tension without changing the difficulty.

Once again, **numbers caught a feature I added because "it sounds fun" from breaking the game.**

## The game lab is now eight

| | Game | Vibe |
|---|------|------|
| 🎨 | [Guess the AI Image](/games/guess-image/) | Brain (quiz) |
| 🟩 | [Korean Word Guess](/games/hangul-word/) | Habit (daily) |
| 🍰 | [Dessert Stack](/games/stack-tower/) | Timing (arcade) |
| 🕹️ | [Dodge](/games/dodge/) | Reflex (action) |
| 🗑️ | [Paper Hoop](/games/paper-hoop/) | Aim (physics) |
| 🪐 | [Space Merge](/games/space-merge/) | High score (merge puzzle) |
| 🚂 | [Shunting Yard](/games/shunting/) | Logic (3D puzzle) |
| 🎣 | [Deep Fishing](/games/deep-fishing/) | **Collection (encyclopedia)** |

## What I took away

**"Something feels off" isn't information on its own. But there's always a concrete cause underneath it.** I dug in three times, and each time the cause was right there in the code — no rotation, a fixed descent time, a fixed line endpoint. All of them **one or two lines.**

And once **the cause I'd guessed was wrong.** I thought the background removal had failed; measuring said it was contrast. Measuring before fixing was much faster.

---

**[Play a run of Deep Fishing](/games/deep-fishing/)** and tell me how many species you landed. I still haven't seen the **kraken**. 🐉

*Next time: a ninth game.*
