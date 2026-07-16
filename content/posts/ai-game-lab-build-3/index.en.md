---
title: "Making Games with AI #3 — A One-Button Dessert Tower, or How Plain Bars Became Macarons (Build in Public #3)"
description: "The third game in the lab is a totally different genre — a one-button arcade stacker. But the first version was a dull tower of colored bars. After a 'the design is ugly' verdict I rebuilt it in 2.5D, and it finally became a tower of pancakes, macarons, and wobbling jelly — three makeovers in all. Build in Public #3."
slug: "ai-game-lab-build-3"
date: 2026-07-16T20:00:00+09:00
draft: false
categories: ["AI"]
tags: ["AI", "vibe coding", "game dev", "build in public", "arcade", "dessert", "indie hacker"]
---

Looking at the [first two games](/p/ai-game-lab-build-2/) (the picture quiz and the Korean Wordle), they had one thing in common — **both are thinking games**. A library full of quizzes gets boring. So for the third game I went the opposite way: something you play with pure **hand-feel**, no thinking required. It ended up as… a **Dessert Stacking Tower**. Why "dessert"? I'll get to that.

👉 **[Play Dessert Tower](/games/stack-tower/)**

## What a "stacker" is

If you've played mobile games, you'll remember the 'Stack'-style genre. The whole rulebook:

- A block **slides left and right** → **tap** and it drops
- Only the part **overlapping the block below survives** — the overhang gets sliced clean off
- Blocks get narrower and narrower; miss completely and it's over — **how many floors did you stack?**

Thirty seconds to learn, thirty seconds a round. And yet "one more try" never ends.

## How you play

1. One **tap** (spacebar on PC) = the dessert drops
2. Miss by a bit and that bit gets sliced off — cream squishes out on every landing
3. Land within a few pixels and it's a **PERFECT** — nothing gets cut, and **a cherry or strawberry pops on top** (it stays there, so your perfect history stacks up like medals)
4. Consecutive PERFECTs slowly **restore** your width (you can come back from mistakes)
5. It gets faster as you climb. Score = floors

![Dessert Tower gameplay](stack-dessert.webp)

Pancakes, macarons, whipped cream, chocolate… every floor brings a different dessert. The problem is —

## The jelly wobbles 🍮

Every few floors, a **jelly** shows up. After it lands, its elasticity keeps it **wobbling side to side** — and the next drop is judged against its **live, wobbling position**. You have to land the next dessert on a moving target. In return, once something lands on it, the jelly gets pressed into place and stops. It's this game's signature gimmick — that "oh no, it's jelly…" moment.

## From plain bars to macarons

Here's the real story of this episode: this game **transformed three times.**

**Take 1 — colored bars.** I finished the logic and showed the first version. The verdict: *"It's good, but the tower design is really ugly."* …Fair:

![Take 1 — flat bars](stack-before.webp)

**Take 2 — 2.5D.** So I rebuilt the rendering with tops and sides. Much better:

![Take 2 — the 2.5D tower](stack-after.webp)

**Take 3 — dessert.** Then came the idea: *"What if you stacked desserts instead? And the jelly wobbles!"* — and in that moment this went from a generic Stack clone to **a game with its own identity**. Pastel sky, a cake stand, syrup drips, perfect-cherries, and the wobbling jelly. The gameplay screenshot above is the result.

The game logic never changed. Only the **rendering and the concept** did — and each time, the game felt completely different. What I learned: if rules are a game's skeleton, **the concept is its face**.

## Three games now — each a different flavor

| | Game | Flavor |
|---|------|--------|
| 🎨 | [Guess the AI Picture](/games/guess-image/) | Brains (quiz) |
| 🟩 | [Guess the Korean Word](/games/hangul-word/) | Habit (daily) |
| 🍰 | [Dessert Tower](/games/stack-tower/) | Hand-feel (arcade) |

Not "a pile of similar games" anymore — the [game lab](/games/) finally feels stocked.

---

**[Stack a dessert tower](/games/stack-tower/)** and tell me how many floors you managed. For the record, I keep collapsing on the jelly. 🚀

*Next time: a fourth game, or maybe the report card on whether anyone actually came to play.*
