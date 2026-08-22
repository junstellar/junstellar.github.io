---
title: "Not MBTI, but Big Five — I Built the Personality Test Psychology Actually Uses"
description: "Type quizzes are fun, but research psychology measures personality with the Big Five. I translated 50 public-domain IPIP items into a four-language test. Thinking Star Lab, build #2."
slug: "big5-test"
date: 2026-08-22T10:50:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "personality test", "Big Five", "IPIP", "MBTI", "personality types", "psychology test"]
---

After [building an IQ test for my 7th-grade daughter](/en/p/kids-iq-test/), I got ambitious: instead of a one-off, why not a whole series of **tests with an actual research basis**? This post is about build #2 — the Big Five personality test.

👉 The result first: **[Big Five Personality Test](/tools/big5/?lang=en)** · Series hub: **[Thinking Star Lab](/lab/?lang=en)**

## Why a Personality Test?

Personality type quizzes are practically a party game now, and I enjoy them too. But here's the thing: **the model research psychology actually uses to measure personality is a different one** — the **Big Five**. Instead of sorting people into types, it locates you on five continuous dimensions.

- **Extraversion** — sociability, energy, assertiveness
- **Agreeableness** — empathy, kindness, cooperation
- **Conscientiousness** — planning, order, persistence
- **Emotional stability** — calmness, stress resilience
- **Openness** — imagination, intellectual curiosity

It is the de facto standard model of personality psychology, backed by decades of research. A perfect candidate for build #2.

## This Time, the License Twist Went the Other Way

Readers of the IQ test post may remember: the "public" research items (Ch-ICAR) turned out to be research-use-only, so I had to write all 76 items myself.

This time it was the exact opposite. There is a repository called **IPIP (International Personality Item Pool)** whose official site states that its items and scales are in the public domain — usable **for any purpose, without permission or fees**, commercial use included.

It's an asset psychology built over decades, precisely because personality instruments were expensive and closed. So this time I could use **the very items used in research**, verbatim. I chose Goldberg's 50-item Big Five markers (10 per factor) and prepared them in Korean, English, Japanese, and Chinese.

## What I Paid Attention To

**1. Fifty items in five minutes** — long tests lose people. Selecting an answer auto-advances to the next item, so one tap equals one item. On PC, keys 1–5 work too.

**2. Reverse-keyed items** — if you strongly agree with "I don't talk a lot," your extraversion score should go down. Nearly half of the IPIP items are reversed like this, and the scoring flips them. Random clicking cancels itself out — old test-design wisdom.

**3. "Neuroticism" became "Emotional stability"** — nobody enjoys reading "you are high in neuroticism." I flipped the direction, and more importantly, **every pole of every dimension is described as a strength** — low agreeableness reads as "strong in negotiation," low stability as "the sensitivity that powers empathy." In the Big Five there genuinely are no good or bad scores.

**4. Honesty about the numbers** — the 0–100 score is a position within the theoretical range (10–50 per factor), not a norm-based percentile. Pretending otherwise would break the rule I set with the IQ test, so the results page says exactly how it's computed.

## And I Opened a Lab

With two tests done, stacking cards in the blog's tools menu was getting crowded. So, like the [AI Game Lab](/games/), I opened a hub: **[Thinking Star Lab](/lab/?lang=en)**. Two tests are in residence; the waiting list includes:

- ⚡ **Reaction time** — catch the moment the screen changes
- 🔢 **Digit span** — remember ever-longer number strings (working memory)
- 🎨 **Stroop test** — attention under word-color conflict

Built with Claude Code again, reusing the multilingual frame from the IQ test — apart from item collection and translation, it took less than a day. That's the joy of a series: **each build makes the next one easier.**

## Try It

👉 **[Take the Big Five test](/tools/big5/?lang=en)** — 50 items, about 5 minutes.

For the record: I came out high on openness and middling on conscientiousness. I love making plans; the tidying-up items are where it all fell apart. I should start by putting things back where they belong.
