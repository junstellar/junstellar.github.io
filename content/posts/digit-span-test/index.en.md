---
title: "The Magical Number 7±2 — I Built the Memory Test Intelligence Tests Actually Use"
description: "How many digits can you hold? I brought the Digit Span task — a real intelligence-test subtest — to the web, scored in the same scaled format (mean 10, SD 3). Thinking Star Lab build #4."
slug: "digit-span-test"
date: 2026-09-08T11:00:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "digit span", "working memory", "memory test", "psychology test", "Thinking Star Lab"]
---

Test number four has been added to [Thinking Star Lab](/lab/?lang=en) — and this one came with a course correction for the whole series, so let me start there.

👉 The result first: **[Digit Span Test](/tools/digit-span/?lang=en)** — done in 3 minutes.

## I Chose Tests over Games

With three tests built, a fork appeared: keep adding fun mini-games, or head toward real cognitive assessment. I chose the latter — the fun games already live at the [AI Game Lab](/games/), so the Lab should earn its name. New ground rules:

1. Only tasks **actually used in neuropsychological and intelligence testing**
2. Only tasks **with published research reference values**
3. Results delivered **in the same format intelligence tests use**

The first task chosen under these rules: **Digit Span**. Digits appear one at a time and vanish; you type them back in order — then in reverse. It is the working-memory subtest that standardized intelligence tests actually employ.

## The Magical Number 7±2

The task owes its fame to psychologist George Miller's 1956 paper observing that people hold roughly **seven items, plus or minus two**, at once — the "magical number." Later research puts adult forward spans at 6–7 digits and **backward spans at 4–5**.

That forward/backward gap is the heart of the test. Forward span measures raw **storage**; backward span forces you to hold the digits while **manipulating** them — reading your mental note in reverse without letting the original evaporate. Being about two digits shorter backward is normal, and reading the two numbers side by side is how working memory is properly viewed.

## Real Test Rules, Kept Intact

- **One digit per second** — the standard presentation rate. Faster becomes a perception test; slower invites rehearsal strategies.
- **Two tries per length, two misses ends the phase** — the actual discontinue rule. One slip won't end you; a real limit will.
- **No repeated consecutive digits** — no free chunking from "9, 9".
- **Leaving the tab mid-presentation voids the trial** — browsers throttle background timers, which would stretch the presentation. A trap I discovered while building.

## A Report Card in Intelligence-Test Format

This was the real goal. Intelligence-test subtests convert raw scores to **scaled scores with mean 10 and SD 3** (range 1–19): 10 is dead average, 13 is roughly the top 16% — one ruler for every subtest.

So your results read: **Scaled score 11/19 · Average · ≈63rd percentile** — with separate scaled scores and classifications for forward and backward.

One caveat: actual test norm tables are proprietary, so this conversion maps **published adult means and SDs from the research literature** onto that format — and the results page says so. But this is also where the series is heading: as anonymous visitor scores accumulate, the references get replaced by **real percentiles from our own sample**. This test's scoring core is already structured to submit as-is when that lands.

## Lab News

Four tests so far — the [IQ test](/en/p/kids-iq-test/), [Big Five](/en/p/big5-test/), [reaction time](/en/p/reaction-test/), and Digit Span. Next up is 🎨 the Stroop test, with mental rotation and pattern memory planned after. Together they add up to a **cognitive profile battery**: working memory, processing speed, spatial, verbal.

## Try It

👉 **[Take the Digit Span test](/tools/digit-span/?lang=en)** — forward and backward, 3 minutes.

What's your magical number? I promise the backward phase will make your mind go delightfully blank.
