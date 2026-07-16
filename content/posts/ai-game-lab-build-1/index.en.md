---
title: "Can You Actually Make Money With an AI Game? — Building a Picture-Guessing Quiz Solo (Build in Public #1)"
description: "I stumbled on a YouTube story about someone who made big money from a game they built with AI in just a few days. What stuck with me wasn't the money — it was the attitude: start small and stack it up one step at a time. So I built and shipped my own 'Guess the AI Picture' quiz on my home gaming-laptop GPU. Why this game, and how I made it — Build in Public #1."
slug: "ai-game-lab-build-1"
date: 2026-07-06T22:00:00+09:00
draft: false
categories: ["AI"]
tags: ["AI", "vibe coding", "indie hacker", "Pieter Levels", "game dev", "build in public", "ComfyUI", "local GPU", "AI coding"]
---

The other day I was watching YouTube and happened to catch an interesting story. Someone had made **big money** from a single browser-based flying game they'd built **with AI in just a few days**. The game was **fly.pieter.com**. The graphics weren't anything special — apparently they earned it by **selling ad-billboard space** floating in the game's sky.

The person behind it is **Pieter Levels**, a solo developer from the Netherlands. With no investors and no employees, he builds and runs a whole bunch of services (Nomad List, Remote OK, PhotoAI, and more) entirely **on his own**. His way of working stuck with me — build **solo and fast**, earn revenue from day one, keep the tech extremely simple, and above all **share the whole process every day (build in public)**. fly.pieter.com was exactly that: whipped up with AI (so-called "vibe coding") and grown by sharing the process as he went.

After watching that video, a thought hit me: *"I should try one more thing too. So… maybe I'll build a game?"* This post is the story of the game I actually built from that thought.

## What I took away from this

Honestly, at first I was drawn to the "made big money" part. But after chewing on it for a few days, what really stuck with me wasn't the money — it was the **attitude**.

Not prepping some grand plan or a perfect finished product first, but **starting small, sharing the process, and stacking it up one step at a time from there** — that approach. Whatever the outcome, I felt that just starting and leaving a record of the process would leave me with something worthwhile.

Once I'd set my mind that way, the direction got clear. A grand 3D game is a problem for much later; for now I'd make something **small, that only I can make, and fun**, and open up the process right here. So I started building.

## The strategy I picked — my weapon is "the GPU at home"

You've got a shot when you do something others can't easily do. And I have one weapon others don't: the [**local image generator (ComfyUI) I set up on my home gaming laptop** in the last post](/p/claude-local-image-generation/).

"Games that run on AI images" are usually daunting for individuals because of **image-generation API costs**. But I can crank out pictures **for free, unlimited** on my RTX 4060 laptop. I do for the price of electricity what others can't do because of the bill. Wondering what game would make the most of this weapon, I landed on —

## The first title: "Guess the AI Picture"

👉 **Play it now: [Guess the AI Picture](/games/guess-image/)**

The rule is simple. **Look at a single AI-drawn picture and guess what it is.** Here are a few examples.

![A cat in a spacesuit](/games/guess-image/img/astro-cat.webp)

![A dragon made of sushi](/games/guess-image/img/sushi-dragon.webp)

![A sea inside a watermelon](/games/guess-image/img/watermelon-sea.webp)

(The answers? Go find out for yourself 😏)

I first made it multiple-choice, but a friend testing it said **"even my pet turtle could get these,"** so I tore it up. Here's how it works now.

- **Three tries per question**
  1. **1st try** — just type your answer (`+3 pts`)
  2. Miss it and you get a **hint**, then try again (`+2 pts`)
  3. Miss again and it's **multiple choice** for the last shot (`+1 pt`)
- The faster you get it, the higher your score, wrapping up with a **total out of 15**
- Your **daily streak** and **cumulative score** build up on your device (no account, no login)
- Results turn into `🟩🟨🟧🟥` emoji you can **share in one tap** (Wordle-style)

There are **30 questions** right now, and each game pulls **5 at random**. So every time you hit "Play again," you get different pictures.

## How I made the 30 images — free, on the home GPU

This is the heart of the project. I generated all 30 quiz images **right on my home laptop**.

- Feed a prompt to ComfyUI + SDXL and generate a picture (**about 30 seconds each**)
- A cloud API would have run up a bill over dozens of images; locally it's **zero, minus the electricity**
- I **converted** the 30 PNGs (48MB) **to WebP**, compressing them down to **2.2MB total** (so they load fast on the web)

If I don't like a picture, I just tweak the prompt and re-roll, so growing the question pool costs basically nothing. This is exactly **why a local GPU is such a strong weapon for an "AI image game."**

## Why a "game lab," not just one game

This game is actually title #1 in a mini-game **library** called [**AI Game Lab**](/games/). I built a library instead of a single game because —

- Even if one game flops, **the library itself remains an asset**, and
- The story of **"the person who keeps cranking out AI games"** fits build-in-public perfectly

I structured it that way too. Adding a new game takes just **copying one folder + one line in a list**, and shared features like score-sharing and cumulative records are set up for every game to reuse. I'll keep stacking games on here.

## I plan to keep stacking from here

Honestly, harder than making the game is **keeping it going**. So instead of finishing and then wondering "now where do I post this?", I decided to **write up the process from the start**, like this. This is episode #1.

The plan isn't grand.

1. Keep **sharing the process** (build in public)
2. **Bake sharing into the game** so anyone who plays can pass their result along easily
3. **Keep adding games** one at a time to grow the library

There's no big result to show off yet. It's only episode #1. But **stacking it up steadily, one step at a time** — that's the thing that matters most to me right now.

---

So let me close this post with a request. 👇

**[Play a round of "Guess the AI Picture"](/games/guess-image/)** — tell me what you scored and which picture cracked you up, and I'll fold it into the next episode. You playing is the real fuel for this experiment. 🚀

*Next time I'll probably show up with a second game, or a report card on how many people actually came by.*
