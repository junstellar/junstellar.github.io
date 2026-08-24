---
title: "What's Your Reaction Time in ms? — A 150-Year-Old Psychology Task, on the Web"
description: "I turned 'simple reaction time' — a task experimental psychology has used for over 150 years — into a one-minute web test. Measuring with pointerdown instead of click, and being honest about online latency. Thinking Star Lab #3."
slug: "reaction-test"
date: 2026-08-24T20:10:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "reaction time", "reaction test", "psychology test", "Thinking Star Lab"]
---

The third test at [Thinking Star Lab](/lab/?lang=en) has zero questions. Nothing to read, nothing to choose. It asks exactly one thing of you — **the moment it turns green, click as fast as you can.** The reaction time test.

👉 The result first: **[Reaction Time Test](/tools/reaction/?lang=en)** — done in a minute.

## Actually the Oldest Measurement in Psychology

The rule is almost childish. Stare at a dark screen, and the moment it turns green ●, **click as fast as you can.** Five rounds, averaged.

But this childish task has a distinguished pedigree. Reacting as fast as possible to a stimulus — **simple reaction time** — has been used in experimental psychology for over 150 years; it sits near the very origin of measuring the mind with numbers. Studies typically report visual simple reaction times of **200–300ms** for young adults, and that reference range anchors the results screen.

## No Items to Write — So I Fought Milliseconds Instead

The build took half a day, but the fun was in the details. When your unit is the millisecond, things you never think about become measurement error.

**1. pointerdown, not click** — the web's usual click event fires when you press *and release*. Your finger-lifting time gets billed to your record. Measuring on **pointerdown** — the instant of the press — removes tens of unfair milliseconds. On PC, the spacebar works too.

**2. Random 1.5–4s wait** — with a fixed delay, people stop reacting and start predicting the rhythm. Each round waits a different amount, and clicking before green is a **foul**: the round doesn't count. Exactly how real RT experiments do it.

**3. Color alone isn't enough** — relying only on red→green is unfair to colorblind users, so the shape changes too: **■ becomes ●** at the same moment.

## And the Honesty Corner

A series tradition by now. The results page says it plainly: **online measurement adds roughly 20–50ms of display and input latency.** A 60Hz monitor takes up to 17ms just to change the frame. So this is not a certified absolute record — it's a **reference you track across repeated runs on the same device**. For pre-game warm-up checks or family showdowns, it's plenty.

## Lab News

Following the [kids' IQ test](/en/p/kids-iq-test/) and [Big Five](/en/p/big5-test/), that makes three tests in residence at the lab. Two remain on the waiting list — 🔢 digit span (working memory) and 🎨 the Stroop test. Built with Claude Code again; thanks to the shared series frame, the four-language version was done in the time it takes to drink two coffees.

## Try It

👉 **[Take the reaction time test](/tools/reaction/?lang=en)** — five rounds, one minute.

For the record, mine was an **average of 257ms (Fast)**, best 190ms. The round-by-round numbers are the fun part — 308, 260, 256, 271, 190. My last round was over 100ms faster than my first, which rather neatly proves the point above: watch the trend, not the absolute value.

Take turns with family or friends on the same device. Same screen, same latency — that's a fair fight. Who wins is… for you to find out.
