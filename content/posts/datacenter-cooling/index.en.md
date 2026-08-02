---
title: "Cooling — The Hidden Bottleneck, and Why Immersion Cooling Stocks Have No Revenue · AI Power Investing 101 ⑧"
description: "An Nvidia GB300 rack throws off 135kW. The ceiling for air cooling is 25kW. Here is why liquid cooling became mandatory — and the real reason immersion cooling stocks still book almost nothing."
slug: "datacenter-cooling"
date: 2026-08-02T22:00:00+09:00
draft: false
image: "power-series-8-cover.png"
categories: ["AI 투자"]
tags: ["immersion cooling", "data center cooling", "liquid cooling", "cooling stocks", "AI power"]
---

In [Episode 1](/en/p/ai-power-hunger/) I split the AI power crunch into three branches — generation, delivery and cooling — and in [Episodes 5](/en/p/power-value-chain-map/) and [6](/en/p/power-money-river/) I kept deferring cooling to "Episode 8." This is that episode.

Earlier episodes were about getting electricity **in**. Today is about getting it **out**. Nearly 100% of the power entering a data center turns into heat. A rack drawing 135kW is also a 135kW heater. Fail to remove that heat and the servers stop.

## Air cooling already hit the wall

Two numbers side by side settle the matter.

![Air cooling's 25kW ceiling versus a 135kW GB300 rack, plus per-chip power trend](air-cooling-wall.png)

The practical ceiling for air-cooling a rack is roughly **8–25kW**. Even with special design, 30–40kW is cited as the thermodynamic limit. An Nvidia **GB300 NVL72 rack throws off 135kW** (155kW at peak) — more than **five times** the wall.

The consequence is blunt: **there is no air-cooled version of the GB300.** The default architecture pulls 90% of the heat out with liquid and handles only 10% with air. Liquid cooling stopped being "the more efficient option" and became **a precondition the product imposes on you.**

At the chip level it's starker still. The H100 drew 700W; the B200 draws 1,000W; the B300 draws **1,400W**. A single GPU now radiates about as much heat as an electric blanket. In [Episode 6](/en/p/power-money-river/) I noted rack density jumping from 8kW to 120kW — this heat is the flip side of that number.

## Three methods — but the winner isn't the one you'd expect

There are broadly three approaches.

![Comparison of air, cold plate and immersion cooling by density, PUE and cost](cooling-three-ways.png)

**Air** is, as we saw, no longer an answer for dense AI. Its PUE (power usage effectiveness; closer to 1 is better) sits at a poor 1.5–1.6.

**Cold plate (direct-to-chip)** bolts a metal plate with water running through it directly onto the chip. It handles 60–175kW per rack and brings PUE down to 1.05–1.2.

**Immersion** submerges whole servers in a non-conductive dielectric fluid. It handles 100–250kW per rack at a PUE of **1.01–1.08** — the best of the three.

So immersion should win. It isn't. **As of 2026 the de facto standard is cold plate**, and immersion's global data center adoption rate is still **under 5%.**

## If it's the most efficient, why isn't immersion spreading?

This, I think, is the most important part of the episode.

![Four reasons immersion cooling adoption is delayed](immersion-delay.png)

**① Nvidia won't warrant it.** This is decisive. Submerge a GPU in dielectric fluid and **most warranties are void.** Nvidia still does not issue lifespan certification for immersion cooling. No operator submerges hundreds of thousands of dollars of GPUs without coverage. Worth noting: Intel, together with Shell, Supermicro and Submer, already shipped a warranty-preserving single-phase immersion solution for Xeon processors — so this isn't a case of it being technically impossible.

**② There's no standard.** The first international standard proposal for immersion cooling only appeared in 2025. Tanks, fluids and interfaces differ by vendor.

**③ Retrofitting existing facilities is hard.** Installing tanks means redesigning floor space, floor loading and plumbing. Cold plate, by contrast, can be swapped in one rack at a time. That "incremental adoption" is what decided the race in practice.

**④ Korea adds a regulatory layer.** Korean fire and hazardous-materials law requires coolant fluid with a flash point above **250°C**, while the US and Europe permit under 100°C. Global standard products can't simply be imported as-is.

Taken together, immersion looks like **a 2027–28 story rather than a 2026 one.** The market expects Nvidia to embrace immersion in the generation after Rubin Ultra.

## So where do the Korean names actually stand?

Which raises the question that matters for investors: are the stocks that rallied as "immersion cooling plays" actually making money?

![Where Korean cooling-related companies stand: revenue, certification, PoC or product announcement](korea-cooling-map.png)

As far as I could find, the conclusion is this: **no listed Korean company yet shows meaningful revenue from immersion cooling itself.**

- **LG Electronics** is where real money is verifiably moving — but in **chillers and CDUs** (coolant distribution units), not immersion. Its data center chiller orders tripled year over year, and it targets 1 trillion won in chiller revenue by 2027.
- **Samsung C&T** won a 400 billion won contract for a 40MW data center in Ansan. That's an EPC package, though, not cooling revenue booked separately.
- **GS Caltex and HD Hyundai Oilbank** make the **dielectric fluid** for immersion. Refiners' base-oil expertise transfers directly here, making it an area where Korea genuinely has an edge.
- **Samsung Electronics** acquired FläktGroup, Europe's largest HVAC maker, for 2.4 trillion won — but its immersion work is still a proof of concept with a single company.
- **GST** is the only listed Korean firm with two-phase immersion equipment technology. Its recent strong results, however, came from its core semiconductor scrubber business; no immersion supply contract is confirmed.
- **K Ensol** partners with Submer, the global leader, and is at the stage of introducing that solution domestically.

## Investor's view — check the four stages

There's a useful test for separating theme from earnings. When looking at a cooling stock, ask which of these **four stages** it has actually reached.

| Stage | What to verify |
|---|---|
| 1 | Has it announced a product and its capacity? |
| 2 | Has it run a PoC with an outside customer? |
| 3 | **Has it disclosed a paid supply contract?** |
| 4 | **Are repeat orders coming in?** |

MOUs and sample shipments are stages 1–2. It becomes a business at stage 3, and it becomes investable earnings at stage 4. Most Korean immersion names are still at stage 1–2.

Three more points.

**① The money today is in water cooling, not immersion.** Cold plates, chillers and CDUs are where orders actually land. It's the same structure as [Episode 7](/en/p/copper-cable-ai/), where I argued against buying cable stocks off the copper chart: **the name of the theme and the place revenue appears are different.**

**② Korea's real edge may be the fluid.** Tanks and systems are largely licensed in from Submer, GRC and others, but the refiners developed and certified dielectric coolant themselves.

**③ The trigger is Nvidia.** When immersion names start booking revenue depends on when Nvidia opens up immersion warranty coverage. Watching Nvidia's cooling certification policy will tell you sooner than any company's IR deck.

## And then there's water

Cooling consumes not just electricity but **water**. Direct water use by US data centers is projected to rise from 17.4 billion gallons in 2023 to 38–73 billion by 2028. More than 20 states are already debating data center restrictions or moratoriums, and in Q1 2026 alone over $130 billion of projects were delayed or cancelled.

This is part of why, as noted in [Episode 4](/en/p/power-supercycle-or-bubble/), far less US data center capacity breaks ground than gets announced. Water is the gate after power — which is why waterless and closed-loop cooling have become the new talking point.

## Summary

- **Liquid cooling is no longer optional.** The air ceiling is 25kW per rack; a GB300 throws off 135kW. Nvidia doesn't even build an air-cooled version.
- **But the winner is cold plate, not immersion.** Immersion has the best efficiency (PUE 1.01–1.08) yet under 5% adoption, held back by Nvidia's missing warranty, absent standards, retrofit difficulty, and in Korea a flash-point regulation. Immersion is a 2027–28 story.
- **No listed Korean firm shows immersion revenue yet.** The money lands first in chillers and CDUs (LG Electronics) and in coolant fluid (the refiners). Check which of the four stages a stock is at — product, PoC, **paid contract**, **repeat orders**.

In [Episode 9] we gather every name this series has produced onto one board: **the map of Korean power stocks** — where each one stands from generation through cooling, and what actually distinguishes them.

> ⚠️ This post organizes what I've studied and is not a buy/sell recommendation for any security. Cited figures and outlooks reflect a point in time and can change. Investment decisions and their consequences are your own.
