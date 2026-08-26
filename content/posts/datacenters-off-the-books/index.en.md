---
title: "The Data Centers Built Off the Books — Whose Debt Did It Become? · AI & Rates Textbook ②"
description: "How $30 billion stops being Meta's debt, dissected. Except the debt didn't vanish — PIMCO bought $18 billion of it, and BlackRock ETFs bought more than $3 billion."
slug: "datacenters-off-the-books"
date: 2026-08-25T18:30:00+09:00
draft: false
image: "rate-series-2-cover.png"
categories: ["AI 투자"]
tags: ["private credit", "SPV", "data centers", "shadow finance", "AI investing"]
---

[Part 1](/en/p/why-bigtech-borrows/) showed three doors the money comes through: bonds, equity, and **off the balance sheet**. Today we go through the third one only.

## "I don't have a single loan in my name"

Say you want to put up a building and need three billion. Borrow from a bank and it's your debt. So instead, you do this.

You set up a **new company** with a group of investors. You take **20%** of it; they take the other 80%. That company borrows the three billion and builds the building. When it's finished, you move in **as a tenant**, on a twenty-year lease.

Now the question: **whose debt is that three billion?**

Legally, the company's. It doesn't appear on your financial statements. With only 20%, you don't even have to consolidate that company into yours. You're just **the tenant**.

And this is what Meta is doing in Louisiana right now.

## Anatomy of a $30 billion deal

![The financing structure of Meta's Hyperion project](hyperion-anatomy.png)

In Richland Parish, Louisiana, Meta is building a one-gigawatt data center called **Hyperion**, targeted for completion in 2030. The price tag is **$30 billion**.

Pull the structure apart and it looks like this.

| Element | Detail |
|---|---|
| Design | Morgan Stanley arranged it as a **special purpose vehicle (SPV)** |
| Funding | **$27 billion in debt plus $2.5 billion in equity** |
| Ownership | **Blue Owl Capital 80% / Meta 20%** (S&P Global Ratings) |
| Meta's role | Developer · operator · **tenant** |
| Cash flow | Blue Owl put in roughly $7 billion of cash; **Meta received a one-time dividend of about $3 billion** |

A **special purpose vehicle** is a shell company created to do one thing: one power plant, one toll road, one data center. When the project ends, it's wound up. The vehicle borrows, and only its own assets stand behind the debt.

The number to watch is **20%**. At that level you are not deemed to **control** the entity. No control, no consolidation. And no debt following you home.

Now read the last row again. **Meta received $3 billion in cash for building a data center.** Given what part 1 showed — a company whose free cash flow has dried up — that single line explains the whole appeal of this structure.

## But is "off the books" the right phrase?

Here I have to check my own wording from part 1. I wrote that the debt "never appears on the balance sheet." **That wasn't accurate.**

![Two ways of counting Big Tech's debt](not-off-the-books.png)

Across Alphabet, Microsoft, Amazon, Meta and Oracle, **AI-related contractual obligations** total **$1.65 trillion** — an **eightfold increase in four years**.

The weight of that figure only registers next to its neighbor. The same five companies carry **$1.35 trillion of actual debt on their balance sheets**. **The contractual obligations have overtaken the reported debt.**

Those obligations are things like:

- **Long-term leases** committing to rent a data center for twenty years
- **Prepurchase agreements** for years' worth of GPUs and servers

None of it appears in the body of the balance sheet, but **it does appear in the notes**. Nothing was hidden. **The place where you read it changed.**

So the accurate phrase isn't "off the books" but **"out of the body, into the notes."** The problem is that this figure has now grown larger than the body. Skip the notes and you miss half the company.

## So where did the debt go?

This is the heart of the episode.

I came into it planning to weigh one question: is this concealing risk, or is it simply how infrastructure has always been financed? Reading the material, **I realized the question was wrong.**

The debt wasn't hidden and it didn't disappear. **It moved onto someone else's books.** The question is whose.

![Who bought the Hyperion bonds](who-holds-the-risk.png)

Here is the buyer list.

| Buyer | Size | Type |
|---|---|---|
| **PIMCO** | **$18 billion** | Largest buyer in the bond market |
| **BlackRock active high-yield ETF** | **$2.1 billion** | **The fund's single largest holding** |
| BlackRock Total Return ETF | about $1.2 billion | Publicly listed ETF |
| BlackRock loan ETF | about $651 million | Publicly listed ETF |

BlackRock ETFs took **more than $3 billion** of these project bonds. In one of them, this position became **the largest single holding in the fund**.

The term **private credit** makes it sound like money circulating among a handful of institutions. Follow it to the end and you find **publicly listed exchange-traded funds**. Anyone with a brokerage account can buy those.

The Korea Economic Daily made the same point: the risk of AI investment **may be migrating from Big Tech toward insurers, private credit, and pension funds.**

Put plainly: **the risk didn't vanish. It moved from Big Tech's books onto ours.**

## Is this Enron?

The question is unavoidable — Enron used SPVs too. But balance is required here.

**Start with the differences.**

- Enron was **concealment**. Vehicles like Chewco and the Raptors hid debt and inflated earnings. Hyperion is a **disclosed structure**. S&P Global Ratings publishes the ownership split; you can see which ETF holds how much. That is the only reason I can write this article.
- Much of Enron's asset base was **fictional**. Hyperion is an actual one-gigawatt building going up.

**And the SPV itself is nothing exotic.**

Project finance and SPVs have been the **standard method** for large infrastructure since the late twentieth century. Power plants, toll roads, telecom networks, pipelines were all built this way. Because a finished data center throws off cash from rack rentals, power charges and operating services, REITs, infrastructure funds and pension funds now treat them as **infrastructure assets**.

**Korea does exactly the same thing.** Domestic data centers are built through project financing vehicles and recycled into REITs. Different acronym, same grammar.

The scale matters too. Morgan Stanley estimates that global data center construction needs **$1.5 trillion through 2028**, and that **private credit could supply more than half of it — roughly $800 billion**, with $200 billion from corporate bonds and $150 billion from securitized products. The Bank of Korea's New York office estimates that about **40% of Big Tech's AI capex this year** will be funded through private credit.

The US private credit market is roughly **$1.3 trillion**. The Financial Stability Board put it at $1.5–2 trillion as of end-2024.

**This is an industry, not a fraud.** The problem is how fast that industry grew.

## The real risk is somewhere else

If it isn't Enron-style concealment, what should we watch? Two things.

### One: the maturities don't match

![The gap between an asset's life and its accounting useful life](maturity-mismatch.png)

Data center loans are structured long. The building lasts twenty years. But the **product cycle of an Nvidia GPU is two to three years**. The collateral ages far faster than the loan.

Which brings up depreciation. **Depreciation** spreads the cost of a long-lived asset across the years it is used; the number of years is the **useful life**.

Michael Burry, of *The Big Short*, raised the objection: Big Tech depreciates two-to-three-year chips over **five to six years**. Stretch the period and the annual charge shrinks — and reported profit swells.

The arithmetic is simple. If Microsoft depreciates $60 billion of equipment over six years, the annual charge is $10 billion. Over three years it becomes **$20 billion**. Same equipment, $10 billion difference in profit. Burry's camp estimates the practice could **understate depreciation by roughly $176 billion across 2026–2028**.

**The rebuttal is solid too.** Bernstein and others argue five to six years is defensible: AI chips are frequently **redeployed for inference** after their training life, and serve other workloads besides. Older GPUs often move to different tasks rather than being scrapped.

Nobody has settled this. But it's worth knowing that **how many years you call an asset changes profit by tens of billions.**

### Two: regulation hasn't kept pace

The capital rules applied to private credit were written for a **smaller, more conventional market**. What this market now finances is **purpose-built, single-tenant, technologically fast-depreciating** infrastructure. Different animal.

The legal side is signalling too. US law firms have begun publishing client alerts on **litigation risk** in AI data center financing. Some deals were funded at a **floating rate averaging around 11%**, with repayment beginning in January 2026.

## Where this reaches an ordinary portfolio

**First, you may already own it.** If you hold a global high-yield bond ETF or an overseas bond fund, data center project bonds may well be inside. In BlackRock's active high-yield ETF, this bond is the **largest holding**. It's worth checking what your own fund actually holds.

**Second, the same structure runs domestically.** Korean data centers are financed through PFVs and exited through REITs. How far construction firms' and brokerages' exposure runs is a separate question worth asking.

**Third, this money eventually touches rates.** Private credit or public bonds, it comes from the same pool. For reference: AI-related companies accounted for **40% of US investment-grade corporate bonds issued in 2026 with maturities of fifteen years or longer**. **Part 3** takes that number on — from the opposite direction. Is it really AI that pushed rates up?

## Summary

- **The Hyperion structure**: Morgan Stanley arranged an SPV, $27 billion debt plus $2.5 billion equity, **Blue Owl 80% / Meta 20%**. Meta is developer, operator and tenant — and **collected a one-time dividend of about $3 billion**.
- **"Off the books" is inaccurate.** The five largest tech firms carry **$1.65 trillion in AI-related contractual obligations**, up eightfold in four years, **exceeding their $1.35 trillion of reported debt**. It sits in the notes, not the body — but it exists.
- **The risk moved to other books.** PIMCO took **$18 billion** and BlackRock ETFs more than **$3 billion**; in one ETF it is the **largest holding**. Despite the name "private," the destination includes public ETFs and pension funds.
- **This is not Enron.** Enron concealed, and its assets were partly fictional. This is disclosed, and the building is real. SPVs and project finance built power plants and telecom networks, and Korean data centers use the same playbook.
- **The real issue is maturity mismatch.** Twenty-year buildings, two-to-three-year GPUs, five-to-six-year accounting lives. Burry's camp sees **$176 billion of understated depreciation across 2026–2028**; Bernstein counters with inference redeployment. Unresolved.

Next time the direction reverses. I began this series assuming **AI debt is pushing rates up**. In part 3 I'll test that assumption **from the skeptical side**. Bank of America attributed only about **30 basis points** of this year's rise in the 10-year yield to corporate bonds and mortgage securities. So what lifted the rest?

> ⚠️ This post is a personal study note and not a recommendation regarding any security, fund or strategy. Financing structures and holdings reflect disclosures, rating agency material and press reports as of the date checked (25 August 2026); fund holdings change frequently. Verify what your own products hold using the manager's latest documents. The depreciation debate is unsettled and no side is endorsed here. Investment decisions and their consequences are your own.
