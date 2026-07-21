---
title: "How Was '₩4-Million hynix' Calculated? — Anatomy of a Price Target · AI Chip Investing 101 ⑨"
description: "Same company, same day, targets from ₩1.85M to ₩4.3M. What kind of number is a price target, really? We dissect actual report formulas — and the 19% hit-rate report card."
slug: "target-price-anatomy"
date: 2026-07-17T11:20:00+09:00
draft: false
image: "hbm-series-9-cover.png"
categories: ["AI 투자"]
tags: ["price target", "SK hynix target price", "PER PBR", "analyst reports", "valuation"]
---

SK hynix trades at ₩1.84 million today. Yet the price targets from brokers watching the very same market run from BNK's ₩1.85M to Hanwha's ₩4.3M — **a 2.3x spread.** One side effectively says "it's fairly priced here"; the other says "double from here." Same company, same earnings, same news. How is that possible?

Because a price target is not a *measurement* — it's a **bundle of assumptions**. In [part 8](/en/p/kospi-semiconductor/) we saw experts split between KOSPI 10,000 and peak-out; today we tour the factory where that split is manufactured — the price-target calculation room. Once you've seen it, a headline like "target raised to ₩4M!" will never read the same way.

## One formula — future earnings × a multiple

Every price target shares a skeleton of almost embarrassing simplicity: **an estimate of future results times a multiple.** Earnings-based: projected EPS × target P/E. Asset-based: projected BPS × target P/B. Here are real formulas from real reports.

When IBK's analyst Kim Un-ho raised his hynix target from ₩1.8M to ₩4M on July 2, the math was: **12-month forward EPS of ₩411,000 × P/E 10 = ₩4,000,000.** Hanwha's ₩4.3M is the same structure (EPS ₩429,777 × 10). Kyobo, meanwhile, got to a similar number via assets: **BPS ₩739,083 × target P/B 5.4.**

![How ₩4M hynix was computed — the P/E camp and P/B camp, same answer, different formulas](target-price-factory.png)

If the formula is that simple, the reason targets diverge 2.3x is clear: **both sides of the multiplication are estimates.** The divergence happens at exactly three points.

## Split ① — which yardstick? (P/E vs P/B)

Memory has traditionally been a **P/B industry**. As part 4 showed, profits ride a rollercoaster every cycle, so analysts anchored to stable book value instead of swinging earnings — top of the P/B band in booms, bottom in busts.

This cycle, Nomura and SK Securities staged a rebellion: HBM's long-term contracts (part 1) have made earnings stable, memory is no longer a cyclical, so **it deserves a P/E valuation.** Hynix's forward P/E sits at 6–7x versus TSMC's 20x — one third. Apply the P/E yardstick and "undervalued" pops out, justifying ₩4M targets.

The balance of power is telling: of 24 brokers covering hynix in the past three months, **18 still use P/B.** The P/E-only camp — IBK, Hanwha, Eugene, SK Securities — is a minority. LS Securities' Hwang San-hae counters that the low P/E is "the market's verification period for earnings durability." Part 4's "this time is different" debate is being re-fought, disguised as a methodology choice.

## Split ② — how much will they earn?

The front half of the multiplication is no firmer. Analysts stack quarterly estimates from assumptions about DRAM contract prices, bit growth, HBM mix, and FX — and small changes compound. Hynix's 2026 operating-profit estimates currently range from **₩223T to ₩281T** across brokers. That ₩58T spread — larger than Samsung's entire operating profit last year — exists purely as *differences of assumption*.

When Korea Investment & Securities lifted its Samsung target 54% in one step (₩370K→₩570K) in May, the formula hadn't changed — **the assumptions had**: the Q2 commodity-DRAM price-hike assumption went from 30% to 60%, earnings estimates jumped, and a target P/B of 5x emerged from a 50% ROE assumption.

## Split ③ — and how many multiples to award?

Finally, the target multiple itself is a judgment call. The anchors are historical bands (how high has this stock ever been rated?) and global peers (Micron ~9x, TSMC ~20x, Nvidia…), but there is no objective answer to "how big should Korean memory's discount to TSMC be." Nomura's ₩670K Samsung target (raised June 24) was argued on precisely that: "it should track TSMC's valuation."

## The report card — consult, don't believe

So how do these numbers actually perform? The Korea Capital Market Institute analyzed ~740,000 reports from 2000–2024.

![The price-target report card — 19% hit rate, 93% buy ratings, 0.02% sells, 5:1 upgrades](target-price-report-card.png)

**A 19% hit rate.** More than 8 of 10 reports never see their target reached. 93% of domestic ratings are Buy; Sell opinions numbered 2 out of 8,668 reports (0.02%), and 28 of 31 brokers have literally zero sell notes — an open secret of a business that lives on investment banking and commissions. This year's revisions: 4,106 upgrades vs 802 cuts, five to one. Hence the standing criticism that targets don't lead prices — **they chase them.**

History teaches humility in both directions. In the 2021 "₩100K Samsung" mania, the street called ₩120K at the top; the stock fell to ₩52,600, and Samsung didn't actually print ₩100K until **4 years and 9 months later**. The reverse also happened: Morgan Stanley's 2024 "Winter Looms" report cut hynix's target 54% — right before the supercycle arrived. Extremes miss, whichever direction they point.

Which makes today textbook material: after the crash, the consensus target sits in the ₩3.1M range — a +70% gap to the current price. Whether you read that gap as "upside" or "estimates that haven't come down yet" cannot be decided by the number itself — only by the assumptions underneath (do DRAM prices keep rising next year? is HBM profit really stable?).

## Recap

- Price target = **future earnings estimate × target multiple.** "₩4M hynix" is EPS ₩411K × P/E 10 (IBK) or BPS ₩739K × P/B 5.4 (Kyobo) — a simple formula whose every term is an assumption.
- Same-day targets span ₩1.85M–₩4.3M for three reasons — **① P/E vs P/B methodology (18 of 24 brokers still use P/B), ② earnings assumptions (op-profit estimates ₩223–281T), ③ the peer-discount judgment.** The methodology choice is a proxy war for "this time is different."
- The report card is sobering — **19% hit rate, 93% buys, 0.02% sells, 5:1 upgrades-to-cuts.** A target is a lagging opinion, not a prophecy.
- The right way to use one: discard the *how much*, read the **why**. Know the assumptions (DRAM price, HBM mix, multiple), and you'll notice for yourself the moment they break.

Part 10 closes the series where those assumptions get tested — **how to read an earnings release, hynix edition.**

> ⚠️ This post is a summary of my own learning, not a recommendation to buy or sell any security. Cited targets and expert views reflect opinions at the time and can change. Investment decisions and responsibility are your own.
