---
title: "Making Games with AI #9 — 30 Minutes Before The Odyssey, 30 Minutes After. Odysseus on One Button (Build in Public #9)"
description: "Three hours that never dragged, and it stayed with me — so I built this. Cyclops, the bag of winds, the Sirens, Scylla, the cattle of Helios, the bow of Ithaca: six scenes you live through on a single button. Homework before the film, revision after. Plus the story of catching myself three times shipping a game that punishes you for doing what the screen says. Build in Public #9."
slug: "ai-game-lab-build-9"
date: 2026-08-19T20:00:00+09:00
draft: false
image: "hero.webp"
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "game dev", "build in public", "Making Games with AI", "The Odyssey", "Greek mythology", "Three.js"]
---

After the deep-sea fishing of [the last post](/p/ai-game-lab-build-8/), game number nine is **Odysseia**. Twenty years from Troy to Ithaca, and six scenes from that voyage that you live through **on a single button**. ⛵

**Play it before the film and it's homework; play it after and it's revision.** I made it after, so I started with the second one.

👉 **[Play Odysseia](/games/odyssey/)**

> **A note before you click.** The game's text is still Korean only —
> the story cards, the gauges, the result screens. It plays fine on one button
> and the six scenes read visually, but the story is the point, so localising it
> is next on the patch list.

## Three hours that never dragged

I saw Nolan's *The Odyssey*. **I loved it.**

The casting fit so well. Matt Damon's Odysseus, of course — and **Anne Hathaway** as Penelope was beautiful in it. She had the face someone who waits twenty years ought to have.

One thing did trip me up: I had watched Spider-Man the week before. **Tom Holland** plays Telemachus and **Zendaya** plays Athena, and my head knew that perfectly well, but Peter and MJ kept bleeding through and that stretch pulled me out a little. 😅 (Nolan apparently shot Zendaya's Athena so you cannot tell whether she is really a goddess or a projection of Odysseus's guilt. That part I liked.)

Still, **Odysseus's story unfolds so grandly** that three hours went by without a dull stretch. I walked out of the theatre with it still sitting on me.

## But the person I watched it with had a different temperature

Talking on the way out, I realised: **I went in knowing the original, and they did not.** We saw the same scenes and came away with different amounts.

Why he alone is tied to the mast in front of the Sirens. Why nobody touches the cattle standing right there. Why the bow at the end matters as much as it does — knowing it, you get "ah, *that* is the bit." Not knowing it, you just move past.

Telling someone to read Homer first is a lot to ask. Telling them to read a plot summary does not work either, because **you read it and nothing sticks.** Summaries of somebody else's story are gone in thirty minutes.

So I wondered whether **living through it** would stick instead.

## Thirty minutes, one button

The rules I set were simple.

| | |
|---|---|
| Stages | 6 |
| Controls | **Space · click · tap** — all three do the same thing |
| Per stage | Under 5 minutes |
| Total | Under 30 minutes |
| Desktop & mobile | Identical |

Collapsing everything onto one button was not a limitation, it was **a choice**. Time spent learning the controls is time the story does not get. Anyone who can press a button should be able to reach the end.

Instead, **the meaning of that button changes with every episode.** Same button, different feel in the hand.

| # | Scene | What the button means |
|---|---|---|
| 1 | The Cyclops's cave | **Tap on the instant** — the moment the hand is elsewhere |
| 2 | Aeolus's bag of winds | **Hold, then release** — the longer you bear it, the faster you go |
| 3 | The Sirens' song | **Endure** — let go and you lose (the inverse of #2) |
| 4 | Scylla and Charybdis | **Hammer it in the gaps** |
| 5 | The cattle of Helios | **Ration your taps** — who eats? |
| 6 | The bow of Ithaca | **Draw, and release exactly right** — one shot |

I am especially fond of #3. In #2 **pressing moves you forward and letting go is safe**; in #3 **pressing is safe and letting go loses.** The meaning of the same button flips.

![The Sirens — Odysseus lashed to the mast, the crew with wax in their ears, the coming song drawn above](sirens.webp)

## The six scenes *are* the plot

The point of this game is less fun than **"these six are all you need."** Going in, it is what you carry into the cinema; coming out, it is the "oh, so *that* is what that was" confirmed with your hands. So for each episode I turned what the myth actually says straight into a rule.

**1 · The Cyclops** — a blinded giant sweeps his hand across the cave mouth. You get out clinging to a sheep's belly. The game **never says** he is blind. The shut single eye and the groping hand say it.

**2 · The bag of winds** — you fall asleep on the tenth dawn with Ithaca in sight. **This is not a failure, it is the story.** It cannot be avoided. The crew open the bag and the ship is blown all the way back. You have to watch the progress gauge get sucked from 95% down to the low twenties.

**3 · The Sirens** — they do not offer beauty, they call out *"we will tell you what you do not know."* **The hunger for knowledge** is the real temptation in this scene.

**4 · Scylla** — Circe's advice is cold: *"Better to lose six than the whole ship. Charybdis swallows everything."* And Odysseus **did not tell his crew.** If he had, nobody would have rowed.

![Scylla — six heads coming down. Below is Charybdis](scylla.webp)

**5 · The cattle of Helios** — if you cannot hold back the hunger, the crew take the cattle and Zeus's lightning ends them all. **This is why Odysseus came home alone.** Losing as the myth does is the default ending; squeeze through the very narrow path and you get a card that reads *"This does not happen in Homer."*

![The cattle of Helios — golden cattle on the hill, six hunger bars](cattle.webp)

**6 · The bow of Ithaca** — he comes home after twenty years dressed as a beggar. Penelope's condition: *"whoever can string Odysseus's bow and send one arrow through twelve axe heads."* Only Odysseus can draw that bow. **Drawing it is the moment he reveals himself.**

![The bow of Ithaca — twelve axes bored through in perspective](bow.webp)

## Six hundred crew carry through all six episodes

That is the spine of it. **You sail with 600, and whatever you lose carries into the next episode.** Every result card writes the remaining number on its last line.

And if you reach the end, it closes like this:

> Homer's Odysseus came home **alone**.
> You brought **N** of them back.

![The epilogue — your voyage in six lines](epilogue.webp)

Those six lines describe **what you actually did**. A summary of somebody else's voyage would not be an epilogue.

## Building it — the game was lying to the player

This is the part I learned the most from this time.

Three separate times I had built **a game that punishes you for doing what the screen says.** In a different form each time.

### One — "Endure"

At the end of episode 2, as drowsiness sets in, the screen said **"Endure / keep holding."** Then I measured it by policy:

| Doing as told | Reached | Crew lost |
|---|---|---|
| Endure | 5.8% | 36 |
| Just let go | 8.9% | 30 |

**Obeying was worse on both counts.** The sail load stayed live while you endured, so following the instruction tore the sail.

### Two — "Hammer to row"

Along the bottom of episode 4 it said **"hammer space or the screen to row."** I believed it and hammered, and I kept dying. Rowing my heart out while the rowers on one side got picked off one by one.

To find out why, I built **a bot that does nothing but hammer.** Hammering alone got **all eight rowers taken in 9.5 seconds**, then left me helpless for another seven before the whirlpool swallowed the ship. And the result card said this:

> **"That is the price of stopping — rest and you get dragged under."**

To someone who never rested once. **The instruction was wrong and so was the telling-off.**

I fixed three things: wrote the other half of the rule into the instruction (*"hammer only while the heads are back — stop when they come down"*), taught it in two beats — **"Row" → "Stop"** — and froze the heads for 1.15 seconds at the start so there is time to read the first lesson.

![Scylla — the moment Stop appears. The line below states the other half of the rule](scylla-stop.webp)

### Three — a death that was not in the design

Then I found something stranger. **There was no rule anywhere in the design about dying when you lose your rowers.** The design document only said *"two or three if you are good, six or more if you are not."*

Which makes sense when you think about it. **How can a ship with 570 people aboard die because eight oar seats are empty?** Somebody else takes the seat.

So I let the seats refill and left Charybdis as the only way to lose. Running the same hammering again, the ship **came through the strait alive.** Down 51 crew.

**Losses were a score, not a death.** The Scylla of the myth takes her six and the ship sails on.

## Without measurement I would have caught none of them

None of the three were **visible to my own judgement.** I wrote "Endure." I wrote "hammer." I put the death rule in. Whoever builds it knows the rules, so they never do as they are told.

The method was the same every time: **write several policies and put the outcomes in a table.**

- A bot that obeys and a bot that does not → which does better
- A bot that mashes like a person → how many seconds until it dies

The last one mattered most. The autoplay function the game already had was a **"perfect bot"** — it only rowed when it was safe. So episode 4 passed a hundred runs in a row. **Only after building a bot that imitates what a person actually does** did the 9.5-second wipe show up.

## And then I cleared episode 1 and got the epilogue

A bug that turned up right before publishing. I cleared episode 1 and instead of episode 2 I got **"the rest of this story continues in the cinema."**

There were two layers to it.

**First, caching.** The preview server sent no cache headers, so the browser was holding a build from days earlier. That build referenced a file I had since deleted, so it could not load episodes 2–6.

**Second, and this is the real problem.** The boot code **quietly skipped the episodes it could not load and built the voyage from what was left.** So a one-episode voyage got made, and clearing episode 1 counted as finishing the last one.

Better to stop and say what is missing than to run on short. Now it does this:

```
Stage modules missing (5/6) — absent: st3.
Clear your browser cache and reload.
```

## Numbers

| | |
|---|---|
| Code | **13,882 lines** across 9 files |
| External assets | **Zero** — shapes and sound are all generated in code |
| Stages | 6, each wholly owned by one file |
| A flawless run | About 5 minutes |
| A first run | 25–30 minutes with retries |
| Console errors | 0 |

Giving each episode a single file that owns its scene, rules, gauges and result is the core of this structure. Nothing broke in episode 4 while I was fixing episode 3.

## Afterword

**Building "the thing that helps when you watch the film" turned game design backwards.** Normally fun comes first and story follows; this time **the six scenes you have to know were fixed first.** Everything was about what each of those six should feel like in the hand.

Episode 2 was the hardest for that reason. **The scene where he falls asleep with Ithaca right there** has to be unwinnable. An unwinnable round has to land as "that stings," not "that is boring." Now the progress gauge climbs to 95% right up to the moment he sleeps, and you watch it get sucked back to the low twenties.

And one more. **A well-built test tool can be the thing blinding you.** This game had an autoplay bot from the start, and it was a "perfect bot" — it pressed only when safe, knowing the rules. So episode 4 passed **every single time.** There was no bot that simply did what the screen said.

I do not think it is a coincidence that the same class of problem came up three times running. The test should have been asking **"does it work if you do what is written on screen?"** rather than **"does it work if you follow the rules?"**

---

This game is not finished here. **I intend to keep working on it with some affection.** I caught three cases of "do what the screen says and lose" this time, and I expect there are more I have not found. I will keep tuning the feel of each episode, work on mobile some more, and patch it bit by bit.

If you have not seen it yet, **spend thirty minutes before the cinema.** If those six scenes land as "ah, that one," it worked.

If you have already seen it, **thirty minutes afterwards** is fine too. That is the side I was on, and building it actually made the film stay with me longer. Why Odysseus was doing what he was doing in front of the Sirens only landed in my body after I had held that rope myself. 😄

👉 **[Play Odysseia](/games/odyssey/)** · [See all of AI Game Lab](/games/)
