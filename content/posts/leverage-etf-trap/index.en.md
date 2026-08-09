---
title: "The Leverage ETF Trap — Why Retail Bought the Crash and Sold the Rally · AI Index Investing 101 ④"
description: "That week the KOSPI fell 2.4% — while 2x leverage lost 8.7% and the inverse 2x lost 10.4%. Here is the volatility decay that made both sides lose, and the 360,000 accounts liquidated in Korea in 2026."
slug: "leverage-etf-trap"
date: 2026-08-09T11:00:00+09:00
draft: false
image: "index-series-4-cover.png"
categories: ["AI 투자"]
tags: ["leveraged ETF", "inverse ETF", "volatility decay", "single-stock leverage", "AI investing"]
---

This is the episode I most wanted to write.

[Episode 3](/en/p/circuit-breaker-week/) covered the last week of July 2026 — four sessions of −10.84%, −5.98%, −1.23% and +17.91%. When that week ended, **the index was down 2.37%.** Not a dramatic figure.

Unless you were holding leverage.

## Both sides lost — the longs and the shorts

I ran that week's daily moves through leveraged products.

![Four-day cumulative returns for the KOSPI, 2x leverage and inverse 2x](that-week-leverage.png)

- **KOSPI index: −2.37%**
- **2x leverage: −8.65%** — a simple doubling would have been −4.75%
- **Inverse 2x: −10.41%** — the index *fell*, so this should have been **+4.75%**

Read that again if you like. **The index declined and the inverse product still lost more than 10%.** They got the direction right and lost anyway.

Leverage gave up 3.9 percentage points; the inverse gave up 15.2. Real products add management fees and tracking error on top.

## Why — volatility decay

The cause lies in **what the "2x" is two times of.** It is twice the *daily* return, not twice the return over your holding period.

To maintain that ratio, the fund rebalances its exposure every day at the close: buying more when the index rises, selling when it falls. Repeat that buy-high, sell-low mechanic daily and it erodes value. This is **volatility decay.**

![Why leveraged products lose even when the index returns to where it started](volatility-decay.png)

Take the textbook case: down 10% one day, up 11.11% the next, so the **index ends exactly where it began.**

- **Index (1x)**: 100 → 90 → 100. **No loss.**
- **2x**: 100 → 80 → 97.8. **−2.2%**
- **3x**: 100 → 70 → 93.3. **−6.7%**

The index breaks even; only the leveraged versions lose. And **the loss grows with the square of the multiple.** As an approximation:

> Leveraged return = multiple × index return − [multiple × (multiple − 1) ÷ 2] × volatility²

That's why the drag on a 3x product is 2.25 times that of a 2x. And the higher the **volatility**, the larger that second term grows. A week of 10% daily swings is the worst possible environment for leverage.

## This isn't the first time

Not a Korean problem, and not a 2026 problem.

![Actual performance of TQQQ and Korean inverse 2x, plus the 2026 damage in Korea](real-damage.png)

**TQQQ** (3x Nasdaq 100) lost **30.6% between February 2021 and mid-2023 while the index (QQQ) rose 7.8%.** In 2022 alone it fell 79.08%, with a maximum drawdown of 81.7%. After losing 80%, you need a 400% gain just to get back to even.

**Korea's inverse 2x** is worse. NH Investment & Securities analyzed 16,536 of its own clients holding the product: **97.74% were sitting on losses**, with an **average return of −63.58%.** Ninety-eight out of a hundred lost money.

## And then 2026 in Korea

On May 27, 2026, **18 single-stock leveraged and inverse products** tracking Samsung Electronics and SK Hynix listed at once — 4.32 trillion won, the largest single-day listing in Korean history. The rationale for loosening the rules had been: why can Americans do this and Koreans can't?

Within two months, their combined market cap grew from 4.4 trillion won to **11.9 trillion.** By June 19, retail investors had bought a net **8.2 trillion won** of the leveraged versions alone.

Then July arrived.

**The SK Hynix leveraged ETF fell as much as 84% from its June high.** Roughly **360,000 brokerage accounts were forcibly liquidated**, and **62% of them belonged to people under 35.** Citi estimated cumulative retail losses at around **56 trillion won** — the sector's market cap fell from 76 trillion on July 22 to 28 trillion.

Of the six days this year when forced selling exceeded 100 billion won, five came after that May 27 listing.

## The hardest part — when retail bought and when they sold

This is the core of the episode.

![Retail trading direction on the crash day versus the rally day](retail-timing.png)

**On the day the KOSPI fell more than 10%, retail investors bought 1.0996 trillion won of leveraged ETFs** — 25.5% of all retail net buying in the market that day. On July 30 they added another 770 billion won to products that had already halved.

Then on **July 31, the day the KOSPI rose 17.91%, retail sold over 1 trillion won of single-stock leverage.** Foreign investors bought a record 7.24 trillion won the same day.

They levered into the fall and sold into the recovery. I don't want to write this as "retail is foolish." **Buying an asset as it falls can be a perfectly rational strategy.** The problem was doing it **with 2x attached.** Volatility decay betrays averaging down, and forced liquidation doesn't wait for the rebound.

As Episode 3 showed, the index recovered 86% of the drop in a single day. For the 360,000 accounts liquidated before that, the rebound never existed.

## Did leverage cause the crash? Opinions split here

One caveat. Many argued that single-stock leveraged ETFs caused this crash. Experts disagree.

**The amplification case**: maintaining 2x means buying more as prices rise and selling more as they fall, and this rebalancing clusters near the close — creating a force that pushes the tape further in whichever direction it's already going.

**The overstated case** is substantial too. Korea Investment & Securities analyst Yeom Dong-chan called single-stock leveraged ETFs "an amplifier rather than the cause," arguing the root driver was rising volatility at global semiconductor firms. He also noted a timing mismatch: rebalancing clusters late in the session, while the actual volatility was larger in the morning.

The Capital Market Institute splits the difference: rebalancing can add volatility, but **retail's counter-trend behavior — buying crashes and selling rallies — partly offset it.** Ironically, the same pattern that cost retail money dampened market volatility.

## What happened to regulation

The response was fast.

| Date | Action |
|---|---|
| May 27 | 18 single-stock leveraged/inverse products list (deposit requirement 10m won) |
| July 16 | New listings suspended; advertising and marketing banned immediately |
| July 24 | Minimum deposit raised to **30 million won**, cash only |
| July 31 | Rules take effect early |

The same requirement was extended to overseas-listed single-stock leverage (Tesla, Nvidia and the like) to prevent money simply relocating abroad.

The effect was immediate: daily turnover in the 16 single-stock products fell from 12.45 trillion won on July 30 to **919.9 billion won on August 5** — from 32.5% of total KOSPI turnover down to 3.7%.

Though note this: on July 31 itself, **retail bought over 500 billion won of index-based inverse ETFs, which the new rules didn't cover.** Money moved from the blocked door to the open one.

## Investor's view — four points

**① "2x" means twice the daily move.** Hold it a month and you do not get twice the month's return. Remembering only this sentence avoids half the damage.

**② Choppy, violent markets are leverage's enemy.** You can be right on direction and still lose if the path zigzags. A tape swinging 8–18% a day is the worst possible setting.

**③ Never average down on leverage.** Buying more as something falls can be a valid approach; with a multiplier attached it isn't. Decay breaks your cost-basis math, and margin calls don't wait for recovery.

**④ The US regulators' wording is the most precise.** The SEC and FINRA state that leveraged and inverse ETFs, because they reset daily, are **generally inappropriate for medium- to long-term holding.** They are trading and hedging tools, not assets you own.

## Summary

- **Both sides lost that week.** KOSPI −2.37%, 2x leverage −8.65%, inverse 2x −10.41%. Even the side that called the direction correctly lost.
- **The cause is volatility decay.** "2x" is twice the daily return, and daily rebalancing erodes value in round trips. Losses scale with the square of the multiple. TQQQ lost 30.6% while its index rose 7.8%; 97.74% of Korean inverse-2x holders were underwater.
- **The 2026 bill in Korea was heavy.** The SK Hynix leveraged ETF fell 84% from its high; roughly **360,000 accounts were liquidated, 62% belonging to people under 35.** Retail bought a trillion won on the crash day and sold a trillion on the record rally.

[Episode 5] changes direction. Forget leverage: **how do you actually choose an ETF for AI exposure?** We'll compare semiconductor and AI-power ETFs, Korean versus US products, and what to look at before buying.

> ⚠️ This post organizes what I've studied and is not a buy/sell recommendation for any security or product. The leveraged returns above are calculated from published daily index moves as an illustration; actual product returns differ due to fees and tracking error. Investment decisions and their consequences are your own.
