---
title: "Dad-Made IQ Test — I Built One Myself for My 7th-Grade Daughter"
description: "My daughter wanted an IQ test, so I built one myself: a kids' reasoning test modeled on the Ch-ICAR study (820 children), with a 76-item bank and random draws."
slug: "kids-iq-test"
date: 2026-08-19T21:00:00+09:00
draft: false
categories: ["AI 코딩"]
tags: ["AI", "vibe coding", "IQ test", "building", "Ch-ICAR"]
---

One day my 7th-grade daughter told me, dead serious: **"Dad, I think I'm a genius. I want to take an IQ test."**

A normal dad would have nodded along or searched for a free online test. Instead, I blurted out: **"A test? I'll build you one."**

Then I started researching what I had just promised. This post is the cleanup record of that big talk.

👉 The result first: **[Thinking Star IQ Lab — Kids' IQ Test](/tools/iq-test/)** (Korean)

## Real IQ Tests Are No Joke

Proper intelligence tests (like the WISC) are **paid, one-on-one assessments administered by professionals** — not something an individual can imitate on the web. Meanwhile, the free IQ tests all over the internet mostly have no traceable items or scoring basis.

Then I found **ICAR (International Cognitive Ability Resource)**, a public item repository researchers build and share — and it has a **children's version (Ch-ICAR)**. In 2025, Belgian researchers validated a 27-item test with **820 students** aged 10–14. The structure is clear:

| Subtest | Items | Actual % correct |
|------|--------|------------|
| Verbal reasoning | 8 | 44% |
| Matrix reasoning | 6 | 31% |
| Number series | 7 | 46% |
| Figural analogies | 6 | 37% |

The overall mean was **10.76 out of 27**. Kids that age get less than half right — it's a genuinely hard test. This was it.

## "Public" Doesn't Mean "Free to Use"

But there was a twist. ICAR calls itself a public-domain resource, yet getting the actual items requires **researcher registration and an application**, under a **Scientific Use License**. The reason makes sense: if items and answer keys end up on the open web, the test itself breaks. An IQ test whose answers are one search away is no longer a test.

So I set my direction: **don't use the original items — follow the validated structure instead.** The subtest composition (8·6·7·6), 27 items, ascending difficulty, and the scoring approach. Every item I wrote myself.

## First Version — and My Daughter's Verdict

The prototype came together in a day with AI coding — the skeleton with OpenAI Codex, later overhauls with Claude Code. Parental consent screen, 27 items, per-area results, and a reference score converted with the Belgian sample statistics. I proudly handed it to my daughter.

The result — **she got every single one right.** "See? Told you I'm a genius," she said, triumphant.

I should have been happy, but something was off. The real test's average is 40% correct, and she aced it? Looking at my items again, the answer was obvious: **they were way too easy.** "2, 4, 6, 8, what's next?" — of course a 7th-grader gets a perfect score. Not a genius verdict; an authoring error.

## Second Overhaul — Hard Like the Real Thing

So I went back into the paper and rebuilt the test to match the real Ch-ICAR's format as closely as possible.

- **Two sets by age** — a basic set for ages 10–11 and an advanced set for 12–14, with contrapositives, syllogisms, day-of-week puzzles ("If the day after tomorrow is two days before Thursday…"), Fibonacci, primes, and interleaved series.
- **SVG figure items** — instead of text symbols (●▲), shapes are drawn in code: real 3×3 matrix problems and figural analogies.
- **8 response options** — the real Ch-ICAR uses eight options, so I matched it: 7 choices + "I don't know". Blind-guess odds drop from 25% to 12.5%.
- **Open-ended number series** — typed directly, like the real test. The mobile-keyboard problem is solved with an **on-screen number pad** drawn right on the page; on PC the physical keyboard works too.
- **A 76-item bank with random draws** — 36 basic + 40 advanced items; each run draws 27 at the fixed area ratio, with shuffled options. Memorizing answers won't help on a retake.

Everything runs in the browser with no server. Answers never leave the device.

## Honest About the Score

What I cared about most wasn't the items but **honesty about the score**. The score is an **entertainment/education reference score** converted to a mean-100, SD-15 scale borrowed from the Belgian sample statistics. It is not a standardized IQ for Korean children and cannot replace a professional assessment. The results page says exactly that, and a parental confirmation is required before starting.

Rather than fixating on one number, it works best as a way to see together **which kinds of problems your child enjoys and solves well**.

## Try It

👉 **[Open Thinking Star IQ Lab](/tools/iq-test/)** (Korean) — also available from the **Tools** menu.

Now it's time to hand my daughter the advanced set. If she aces it again… then maybe I really should suspect a genius.
