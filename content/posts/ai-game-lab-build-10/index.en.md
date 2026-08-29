---
title: "Making Games with AI #10 — I Built It Twice and Threw It Away Twice (Build in Public #10)"
description: "I built the tenth game for the lab twice, and scrapped it both times. The scoring was correct, the balance was tuned with simulations — and it still wasn't fun. It took throwing away two builds to learn that difficulty is measurable but fun isn't. Both dead prototypes are still playable. Build in Public #10."
slug: "ai-game-lab-build-10"
date: 2026-08-29T09:00:00+09:00
draft: false
image: "dice-push.webp"
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "game dev", "build in public", "Making Games with AI", "game design", "failure", "indie hacker"]
---

After the Odyssey in [the last post](/p/ai-game-lab-build-9/), I built the tenth game. **I built it twice, and threw it away twice.**

So there's no new game this time. Instead, here's the story of **backing out twice.**

I didn't delete the two dead builds. They're not on the game lab list, but they're still up if you know the address. Poke at them as you read.

👉 **[First prototype — Dice of the Day](/games/dice-yacht/)** · **[Second prototype — One More Roll](/games/dice-push/)**

## The tenth was supposed to have no art at all

Every game so far uses images I generated with [ComfyUI](/p/claude-local-image-generation/). But images are finite. However many you make, eventually one you've already seen comes around again — and that's when interest drops off.

So this time the rule was **no art.** Even the pips on the dice would be CSS dots. I still think that call was right.

## First try — I finished it, and never reached for it

I built it Yacht-style: five dice, up to three rolls, twelve categories to fill.

It worked. I verified eighteen scoring cases down to the boundary conditions — four of a kind, full house, the straights — plus the bonus and the round progression. One file, 21KB, not a single image.

Then I opened it, and — **I just didn't want to touch it.**

![First prototype — a screen where you fill twelve boxes with numbers](dice-yacht.webp)

At first I assumed the explanation was missing. The card just said `Four of a Kind`, `Full House`, `Sm. Straight`. **Nowhere on the screen did it say what dice actually make those score.** Only someone who already knew Yacht could read it.

But I cleaned all that up and nothing changed. The problem wasn't the explanation.

## Yacht has no tension in it

![Tension curves compared — Yacht stays flat all game; push-your-luck spikes and crashes on every roll](dice-tension.webp)

**There's nothing to lose.** Every round you bank something and move on. Even scratching a zero just takes you to the next round. No risk, no tension.

**The decision is homework, not a thrill.** "Twenty points in Fives, or twenty-three in Four of a Kind?" isn't a pulse-raiser, it's arithmetic. There's an optimal answer, so once you know it you play on autopilot.

And the killer: **Yacht is a game you play sitting around a table, talking.** Half the fun is the people. Alone on a phone, that half is gone and what's left is **filling in a spreadsheet.**

## Second try — this time I tuned it with numbers

I tore it down and rebuilt it so there's a decision every single moment.

You roll, set aside only the dice that score, and then choose: **roll again, or stop?** If a roll comes up with nothing scoring at all, **the whole round is wiped.**

![Second prototype — choosing whether to roll once more or stop](dice-push.webp)

This time I didn't tune by feel. I ran **3,000 games per strategy** with auto-players: Coward (bank after one keep), Careful (stop at 30% bust risk), Greedy (push to 45%), Reckless (roll until it blows).

With five dice, a round lasted **1.8 rolls on average.** Two rolls and it was over — no time for tension to build. **Going to six dice created a sweet spot.**

| Strategy | Average score |
|---|---|
| Coward | 1058 |
| **Careful** | **1343** |
| Greedy | 1082 |
| Reckless | 0 |

Roll too little and you lose; roll too much and you lose. Exactly the shape I wanted.

## My hunch was wrong again

The rounds still felt short, so I reached for a classic Farkle rule: **you can't stop until you've banked at least 300.** Force people to keep rolling, and tension goes up — or so I assumed.

I measured it. It did the opposite.

| | Coward | Careful | Gap |
|---|---|---|---|
| No minimum | 1058 | 1343 | **+27%** |
| 300 minimum | 1282 | 1321 | **+3%** |

The minimum didn't add tension — **it removed the decision.** It herded everyone into the same line of play, so playing well and playing badly ended up scoring the same. Shipping that would have ruined the game.

## Everything was tuned, and it still wasn't fun

I put the probabilities right on the buttons. "One more — 2 dice · 44% bust" next to "Stop — bank 550". Showing the odds turned the choice into a real choice.

Then I opened it again — **and it still wasn't fun.**

That's where I stopped. If I've rebuilt it from the rules up twice and neither version lands, the problem isn't the rules. It's the **genre.**

## The answer was already written in my own back catalogue

Only after deciding to scrap it did I go back and look at what I'd made.

| Game | What the fun actually is |
|---|---|
| 🗑️ [Paper Hoop](/games/paper-hoop/) | pull, release → **watch it fly** |
| 🎣 [Deep Fishing](/games/deep-fishing/) | the **split second** you set the hook |
| 🪐 [Space Merge](/games/space-merge/) | drop it and **things burst together** |
| 🍰 [Dessert Stack](/games/stack-tower/) | nail the **timing** |

The ones I'm proudest of are all games you play **with your hands and eyes.** The result reaches your body inside half a second.

Dice — Yacht or Farkle — is a game where you **judge numbers in your head.** Nothing on screen moves. What kind of game I actually enjoy building was already written all over the shelf, and I was the one person not reading it.

## "Use less art" quietly became "the screen doesn't move"

The condition I set myself was **"cut down on image assets."** Somewhere along the way it turned into **"the screen doesn't have to move."**

Those are not the same thing. **Having no image files and having a frozen screen are completely different problems.** Shapes and lines alone can move plenty — I killed both at once.

This keeps happening to me with vibe coding: **when the brief is vague, the result goes to the extreme.** Say "cut down" and you get back "eliminate." This time I didn't notice until I was looking right at it.

## What I took away

**Fun isn't measurable.**

Measurement has caught a lot for me in past posts: [the structural flaw where merging freed up space](/p/ai-game-lab-build-6/), [the problem that turned out to be contrast rather than backgrounds](/p/ai-game-lab-build-8/), [the stages that punished you for doing what the screen said](/p/ai-game-lab-build-9/). It worked this time too. The balance landed, the odds were exact, and it caught a wrong hunch.

**None of that made the game fun.**

Numbers could answer *how to build it*. *What to build* had to be settled before any measuring started, and that's where I was wrong — twice.

So I'm changing the order. **From now on I write one sentence first: "the fun of this game is exactly this moment."** If I can't write that sentence, I don't build it. Asking whether it's fun after it's finished is too late. Two scrapped builds to learn that.

## I rewrote the shortlist

I stripped **every think-in-your-head game** out of the candidate list. Dice, card layouts, mental arithmetic — all gone. I refilled it with games that **move on screen without needing art.**

I don't regret the two I threw away. It took building them to learn **what I shouldn't be building.** Nine games in, I still didn't know; scrapping the tenth taught me.

---

Both dead prototypes are still open. Go see for yourself where the fun isn't. I think the second one is at least better than the first — but I don't want to open either of them again.

👉 **[Dice of the Day (first)](/games/dice-yacht/)** · **[One More Roll (second)](/games/dice-push/)** · [Browse the AI Game Lab](/games/)
