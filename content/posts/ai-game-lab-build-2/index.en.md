---
title: "Making Games with AI #2 — A Korean Wordle, and Rewriting the Hint Difficulty Three Times (Build in Public #2)"
description: "I added a second game to the lab: a 'Korean Wordle' where you guess a two-syllable Korean word, judged jamo by jamo. But the real story was the hints — too hard, then too easy, until I rebuilt them three times into 'progressive hints that unlock one per wrong guess.' Build in Public #2."
slug: "ai-game-lab-build-2"
date: 2026-07-11T09:00:00+09:00
draft: false
categories: ["AI"]
tags: ["AI", "vibe coding", "game dev", "build in public", "Wordle", "Hangul", "indie hacker"]
---

Last time I said I'd "keep stacking games one by one," so — as promised — I built the **second game**. This time it's a **Korean Wordle**: guess one two-syllable Korean word a day.

👉 **[Go play 한글 단어 맞히기 (Guess the Korean Word)](/games/hangul-word/)**

## What Wordle is, in case you don't know

You know Wordle? The word game that swept the world in early 2022. The rules are simple:

- Guess a hidden **five-letter English word** in **six tries**
- Each guess colors every letter as a hint — 🟩 (right letter, right spot) · 🟨 (in the word, wrong spot) · ⬜ (not in the word)
- **One word a day.** Everyone solves the same puzzle, and shares the result as an emoji grid

That "one puzzle a day + color hints" combo is quietly addictive, and it blew up for a while. I wanted to make it **in Korean**.

## Making Wordle work in Korean

In English you just guess letter by letter — but how does that work in Korean? The key is that **a Korean character breaks down into jamo** (its component letters).

- '버' = ㅂ + ㅓ
- '스' = ㅅ + ㅡ
- With a final consonant, three of them — '박' = ㅂ + ㅏ + ㄱ

So just as English Wordle colors each letter box, Korean Wordle colors **each jamo (initial / medial / final)**. Here's what it looks like:

![Guess the Korean Word — start screen](hangul-word-start.webp)

## How you play

1. There's a fixed **two-syllable word of the day** (once a day, same puzzle for everyone)
2. Type two syllables, and each jamo gets colored — 🟩 right spot / 🟨 in the word, wrong spot / ⬜ not there
3. Narrow it down from the color hints and get it in **six tries**

For example, if the answer is '버스' (beoseu, "bus") and you enter '구름' (gureum, "cloud"), the ㅡ in '름' turns green — it matches the ㅡ in the answer's '스', in the very same slot. You pin the jamo down one at a time like this:

![Colored jamo and progressive hints](hangul-word-play.webp)

## Stuck? Hints unlock one at a time

This is the part I sweated over most. Just telling you to guess two syllables with no starting clue is hopeless; but handing over the full description upfront makes it a one-guess gimme. (Honestly, I rebuilt this middle ground a few times.) So here's where I landed: **you start with no hints. Each time you guess wrong, one more opens — getting stronger each step.**

1. **Broad bucket** — "something people made" (one of dozens; almost no help)
2. **Category** — "transportation"
3. **Description** — "public transit lots of people ride together"
4. **Initial consonants** — "ㅂ ㅅ"
5. **First syllable** — "버_"

Those green boxes stacked above the board in the screenshot are exactly this (three wrong guesses → three hints open). So **if you've got a good feel, you solve it fast with no hints for a high score**; if you're stuck, the help narrows in as you miss. The player basically tunes their own difficulty.

## And sharing the result

Solve it and the result becomes a `🟩🟨⬜` emoji grid you can share in one tap. It hides the answer and leaves only the colors — "how many tries, how much you struggled" — exactly the Wordle way. Your daily streak and cumulative score pile up on your device too.

---

So the [game lab](/games/) now has two games — 🎨 Guess the AI Picture, 🟩 Guess the Korean Word.

**[Play a round of the Korean word game](/games/hangul-word/)** and tell me how many tries it took, and whether the hints feel right. If a word's hint seems off, I'll fix it right away. 🚀

*Next time I'll be back with a third game, or the story of whether anyone actually showed up to play.*
