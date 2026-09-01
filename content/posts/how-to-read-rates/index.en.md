---
title: "How to Read Rates — Six Things You Can Check for Free · AI & Rates Textbook ⑥"
description: "From five episodes of numbers, only the ones an individual can click and verify. Every address was opened and checked; the ones that didn't open were dropped. The series finale."
slug: "how-to-read-rates"
date: 2026-09-01T08:00:00+09:00
draft: false
image: "rate-series-6-cover.png"
categories: ["AI 투자"]
tags: ["checking rates", "treasury yields", "COFIX", "term premium", "AI investing"]
---

The last episode of the series.

Five episodes brought a lot of numbers: free cash flow, term premium, residual value guarantees, curve normalisation. But one thing kept nagging at me.

**How many of those numbers can you actually check yourself?**

Copying a figure out of an article is not the same as opening it yourself. So this episode is an **address book**. I opened every link below myself, and **the ones that didn't open were dropped.**

## Six things you can check for free

![Six rate indicators an individual can verify directly](six-indicators.png)

| What | Where | Address |
|---|---|---|
| US Treasury yield curve | US Treasury | [home.treasury.gov](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve) |
| Term premium (ACM) | New York Fed | [newyorkfed.org](https://www.newyorkfed.org/research/data_indicators/term-premia-tabs) |
| Korean treasury yields by maturity | KOFIA Bond Information Center | [kofiabond.or.kr](https://www.kofiabond.or.kr/) |
| Policy rate history | Bank of Korea | [bok.or.kr](https://www.bok.or.kr/portal/singl/baseRate/list.do?dataSeCd=01&menuNo=200643) |
| COFIX | Korea Federation of Banks | [portal.kfb.or.kr](https://portal.kfb.or.kr/fingoods/cofix.php) |
| Mortgage rate comparison by bank | KFB consumer portal | [portal.kfb.or.kr](https://portal.kfb.or.kr/compare/loan_household_new.php) |

All six are **free, with no sign-up.**

### ① The US Treasury yield curve

Part 3's 5.337% lives here. The Treasury publishes **every business day**, from one-month to 30-year. Because the whole curve appears on one screen, you can apply the "break it up by segment" rule immediately.

### ② Term premium — that number from part 3

The value that went **from 0.2% to 1.20%** in part 3. The New York Fed estimates and publishes it using the ACM (Adrian-Crump-Moench) model.

Note that this is **a model estimate**, not a traded price. Institutions produce different numbers. Watch the **direction** rather than the absolute level.

### ③ Korean treasury yields by maturity

The heart of part 5. KOFIA's Bond Information Center shows the 3-year, 10-year and 30-year together. **Seeing them on one screen is the point** — as part 5 showed, looking at only one gives you the opposite conclusion.

The Bank of Korea's **[ECOS](https://ecos.bok.or.kr/)** offers the same data as downloadable time series.

### ④ Policy rate history

The Bank of Korea publishes every policy rate change as a table, including the move to 3.00% on 27 August. Since this sets **the short end**, reading it alongside ③ makes clear where the central bank's jurisdiction ends.

### ⑤ COFIX

Part 5's **preview of next month's floating rate.** The Korea Federation of Banks publishes it monthly. If COFIX rises this month, floating-rate mortgages follow next month. If you carry a mortgage, this is the most practical of the six.

### ⑥ Mortgage rate comparison

The KFB consumer portal compares mortgage rates across banks. The figures are **averages**, though — your actual rate depends on credit and product, so confirm final terms with the bank itself.

### One more — what your own fund holds

[Part 2](/en/p/datacenters-off-the-books/) showed that a BlackRock high-yield ETF's largest holding was a data center project bond. If you hold overseas bond funds or ETFs, it is worth opening **the holdings list on the manager's website.** I left this out of the table because there is no single address — every product has a different manager.

## Three principles for reading rates

![Three principles for reading rates](how-to-read.png)

Knowing where to look isn't enough. Three methods actually used across these six episodes.

### 1. Break it up by segment

The most-used method in this series.

- **Part 3**: across the whole corporate bond market AI was one issuer among many, but **in the 15-year-plus bucket it was 40%.**
- **Part 5**: after a policy rate hike, the 3-year fell **5bp** while the 30-year rose **25bp**.

Same country's bonds, opposite directions by maturity. **"Rates went up" is only half true unless it says which segment.**

### 2. Don't judge on a single day

[Part 6 of the rotation series](/en/p/how-to-read-rotation/) said the same. One day's move tells you almost nothing. Direction shows up only after days or weeks accumulate.

Interpret the KOSPI's 5.80% fall on 19 August and its rebound the next day separately, and you would have been wrong twice.

### 3. Watch the slope

Keep a record of the **30-year minus the 3-year**. When it widens (steepening), something happened at the long end; when it narrows (flattening), the short end moved.

Korea in part 5 was precisely a steepening — and its cause was not the Bank of Korea but **a shift in insurer demand.** Without watching the slope, you'd have stopped at "the policy rate rose, so rates rose."

## What you can safely ignore

- **Daily rate headlines.** As above.
- **Confident "this time is different" claims.** As part 4 showed, similarities and differences always coexist.
- **A single headline total.** In part 4, the size of circular financing ranged from $70 billion to $750 billion. **A big number whose counting basis you don't know is not information.**

## The hypothesis scorecard

![How the six episodes' hypotheses turned out](hypothesis-scorecard.png)

I wrote per-episode hypotheses into the plan before starting. Results:

| Part | Hypothesis written in advance | Outcome |
|---|---|---|
| 1 | Capex has outgrown operating cash flow | **Right** — Alphabet's first negative FCF since its IPO |
| 2 | Concealment, or ordinary project finance? | **Wrong question** — the debt moved onto someone else's books |
| 3 | Blaming AI is an exaggeration | **Right** — Germany and France peaked too, with no hyperscalers |
| 4 | Is it the 1999 vendor financing structure? | **Different, but** — more sophisticated; the risk still moved |
| 5 | America's fault, or a domestic factor? | **A third answer** — demand created by an accounting regime is disappearing |

**Three of five advance hypotheses missed.** In the rotation series it was five of six.

And every time, **the data's version was the better story.** Had part 2 stopped at "concealment or not," the PIMCO and BlackRock ETF material would never have appeared. Had part 5 only looked for a fiscal deficit, insurers and IFRS 17 would have stayed invisible.

When a plausible explanation arrives first, test it against the numbers. It's usually wrong. **And where it turns out wrong, something more interesting is waiting.**

## Summary

- **Six addresses cover this series' numbers.** US Treasury (yield curve), New York Fed (term premium), KOFIA (Korean yields by maturity), Bank of Korea (policy rate), KFB (COFIX and rate comparison). All free.
- **The term premium is a model estimate** that differs by institution. Watch **direction**, not level.
- **Three reading principles**: break it up by segment; never judge on one day; watch the **slope** (30-year minus 3-year).
- **Safe to ignore**: daily rate headlines, "this time is different" certainty, and **a big total whose counting basis is unknown.**
- **If you have a mortgage, COFIX alone is enough.** It's the most practical of the six.
- **If you hold overseas bond products, open the holdings list once.** The bond from part 2 may be inside.

## Finally — thirty-nine episodes

![Five series, thirty-nine episodes](series-finale-39.png)

This post closes the fifth series.

[Semiconductors, 11 parts](/en/p/what-is-hbm/) covered AI's **components**; [Power, 10 parts](/en/p/ai-power-hunger/) its **fuel**; [Indices, 6 parts](/en/p/what-is-kospi-index/) the **market** AI swallowed; [Rotation, 6 parts](/en/p/what-is-sector-rotation/) the **movement of money**. And these six on rates were **the price of money.** Thirty-nine in total.

In hindsight the order was natural — components, fuel, market, the flow of money, and finally its price. It wasn't planned that way. **Each series' unexplained leftovers became the next one's subject.** This rates series began in a single footnote from part 4 of the rotation series.

The next series isn't decided yet. It will probably be one of the things these six episodes couldn't finish explaining.

Thank you for reading.

> ⚠️ This post is a personal study note and not a recommendation regarding any security, fund or strategy. Every address above was confirmed reachable on the date checked (1 September 2026), but institutions can change URLs and menus. The term premium is a model estimate rather than a traded price, and figures differ by institution. Rates published by the Korea Federation of Banks are averages; your actual rate depends heavily on credit and product, so confirm with the institution. The reading methods here are simply what I used across six episodes, not validated investment techniques. Investment decisions and their consequences are your own.
