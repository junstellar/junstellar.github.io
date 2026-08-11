---
title: "Before You Jump to Those '100x Cheaper' AIs — How to Split Work Between Expensive and Cheap Models"
description: "What lit up AI YouTube this week wasn't performance, it was pricing. Chinese open models and Meta's Muse Code knocked the floor out at the same time, but that '100x cheaper' claim comes with strings attached. Here's what actually changed and what to change in your own workflow."
slug: "ai-trend-2026-08-w2"
date: 2026-08-11T21:00:00+09:00
draft: false
categories: ["AI 트렌드"]
tags: ["AI Trends", "Open Models", "Claude Code", "AI Costs", "Muse Code", "Kimi K3", "Weekly Roundup"]
---

Every night at 11, a script runs on my laptop. It scrapes the AI-related YouTube videos posted that day, picks out the ones with high view counts, and leaves me summaries. Skimming those over morning coffee is my routine these days.

I binged the last week's worth, and something felt off. Normally around this time everything is wall-to-wall "look how smart this model is" — but this week there was almost no talk about performance. Everyone was **staring at price tags instead.**

## Three-line summary

- Pricing collapsed. Chinese open models (Kimi K3, Qwen 3.8, DeepSeek V4) and Meta's Muse Code all landed in the same week.
- But "100x cheaper" comes with conditions. That Meta tier costs you **your code, handed over as training data.**
- Agents are starting to have memory. They tidy up on their own during downtime, and memory that travels between tools showed up.

## This week, everyone only talked about price

The title of the most-watched video says it all. *"China just dropped an AI 100x cheaper that beats Fable 5."* 170,000 views.

Moonshot's **Kimi K3** is a 2.8-trillion-parameter open source model. One reviewer had it build a 3D combat game and said it finished for roughly 3.3x less than Claude Fable 5.

I run a weekly [Building games with AI](/en/p/ai-game-lab-build-8/) series, so this part hit close to home. Game building means re-running the thing over and over until it works, which makes per-token pricing a direct tax on the process. I've stopped myself mid-thought more than once, wondering whether to run it one more time.

Meta shipped a terminal coding agent called **Muse Code** in beta. You set how deeply it thinks with `/effort` and swap models with `/model` — honestly, it's nearly identical to Claude Code.

What got people talking was the pricing. On the contributor tier, cached input tokens drop from $0.15 per million to **$0.002.**

What that means in practice: things that were "too expensive to try" are now on the table. Sweeping an entire codebase, triaging hundreds of PRs, refactoring on repeat until it's right. If you shelved an idea over cost, now's a good time to pull it back out.

## But I wouldn't take "100x cheaper" at face value

Stop here for a second. That price has conditions attached.

The contributor tier is cheap because **you hand over your development data.** For a personal toy project you'd use it without a second thought, but if company code or customer information is moving through it, the math changes completely. You can't judge them by the same standard.

To be fair, the video that ran the "100x cheaper" headline did flag this. It noted Meta explicitly says content may be used to improve their products when you use contributor models. Still, it's easy to miss if you only read the title, so I'm writing it down again.

The verdicts were split, too. The reviewer covering Muse Code gave it credit on speed and price but also called out hallucinations, saying it's "not perfect." And one demo of Kimi K3 isn't enough to declare a winner either.

There was one thing every reviewer agreed on: forget benchmarks and **run it on your own actual work.**

![Structure of the SWE-bench benchmark, which measures whether an AI can resolve real GitHub issues on its own](bench.png)

For what it's worth, there's already a public standard for measuring coding agents. Princeton released **SWE-bench** in 2023, and it checks whether an AI can resolve real GitHub issues on its own. A standard like that — or your own workload — beats marketing copy.

## AI started sleeping

Beyond pricing, one more thing stood out: memory and autonomy.

This is the AI weakness Andrej Karpathy pointed to — that it **only learns when it receives a prompt.** Humans have a brain that files away the day's events while they sleep; AI has nothing like it. Anthropic ran with that idea and added **dreaming**, where the model revisits past sessions during downtime and consolidates memory. Enterprise customers only, for now.

There was also an experiment where Claude Opus 5 was told to go make money on its own for nine days. It floundered early on, then ended up building a 3D skiing game and winning prize money. It started with $55 and finished at $87. The amount is cute, but the point is that autonomous operation actually worked.

The funny part is that the AI picked **game development** as its way to make money. Probably because it's a domain where you can ship something short and get judged immediately. It reminded me of [Game Lab, part 1](/en/p/ai-game-lab-build-1/), where I asked "can you actually make money building games with AI?" — a slightly eerie echo.

A prompting technique called the **gauntlet loop** also made the rounds. A main agent spins up several sub-agents, attaches a critic to them, and keeps running until the output meets the bar.

![Run → critique → re-run loop structure, with Reflexion and Self-Refine as research grounding](loop.png)

This one has roots too. It's in the **Reflexion / Self-Refine** line of research (NeurIPS 2023), which established that accuracy improves when an AI evaluates its own output, corrects it, and tries again.

That said, the person who introduced it warned against handing over the whole thing from the start. It works best for **polishing** something that already has direction.

## What I'm taking away this week

I trimmed this down to things worth trying right now.

**Swap models behind a gateway.** Keep your tools as they are and change only the model sitting behind them. With OpenRouter, you install the CLI, make an account, connect an API key, and that's it. Open models like DeepSeek or GLM slot in behind Claude Code.

**Set up failover.** In OmniRoute you can bundle several models and set priority or rotation. When one model hits its limit, it moves to the next on its own so your work doesn't stall.

There's also the option of just running things on your own machine. I wrote that up a while back in [Running your own LLM on a gaming laptop](/en/p/llama-cpp-local-llm/), and with this week's flood of open models, that option got a lot more realistic.

**Teach documents as skills.** Give the Hermes agent's `/learn` command a file path and it remembers the contents permanently. Load in your internal docs or a work manual once and it survives across sessions, so you stop pasting the same files every time.

**Share memory across tools.** Connect Walrus Memory and ChatGPT and Claude draw on the same memory. No more re-explaining your background every time you switch tools.

**Use voice as a conductor, not a worker.** The tip was: don't hand work directly to ChatGPT voice — say something like "spin up a thread and handle this" and pass it off to another thread. The voice model is a lightweight one, so heavy work gets better results when it's delegated.

## If I could keep only one thing

From here on, this isn't this week's news — it's the part that will still hold in six months.

You don't pick one model. You **split the work across models by difficulty.**

![Model cascading: expensive model for design, cheap and open models for execution, mid-tier for verification, grounded in the FrugalGPT research](cascade.png)

| Stage | What | Which model |
|---|---|---|
| Design & planning | Architecture, sorting out requirements | The smartest, most expensive model |
| Execution & iteration | Writing code, conversion, cleanup | Cheap and open models |
| Verification | Checking results, review | Mid-tier |

This isn't just a buzzword. Academics call it **model cascading**, and Stanford's **FrugalGPT** research from 2023 is the canonical example. Handle most of the work with a cheap model and pass only the hard cases to an expensive one, and you cut cost while holding performance.

What changed this week is the middle row of that table. The options you can use for "execution" suddenly got much wider. The principle itself is unchanged.

## Worth looking at the shadows too

OpenAI's Astra got delayed. It tripped the "critical" grade on the cybersecurity item of their own safety framework — meaning it's capable of producing zero-day exploits without human involvement.

On the investment side, the bubble debate got louder. The argument goes like this: if open models and low-cost competition spread, the infrastructure demand projections everyone has been building on may have been overestimated.

One channel warned specifically about the moment **Jevons paradox** ("when it gets cheaper, total usage actually goes up") starts spreading uncritically. The more plausible an argument sounds, the more easily it gets repeated without being checked. I've been fond of that line myself, so it stung a little.

## The rest, briefly

- The default model for free users switched to **GPT-5.6 Luna.**
- **Gemini Notebook 2.0** now generates slides and short-form video from your source material.
- Five Claude Code plugins made the rounds: Omni Route, Claude-mem, Headroom, Claude Code Setup, Task Observer.
- **Claude Design** got motion graphics, but there's still no backend and no live URL. It doesn't connect straight into a real service. Treat it as a prototyping tool.
- Fintech company **Ramp** put agents across their entire dev process and cut CI time by 3x. The trick was a bit unexpected: instead of telling agents "how to do it," they **only specify "what to achieve."**

## Just this one thing this week

Connect a gateway. OpenRouter, OmniRoute, whichever — just put one open model behind the tool you already use.

The goal isn't saving money. It's getting yourself into a **swappable state.** The next time the ground shifts (and it will), only the people who prepared get to move.

Has anyone already switched over to open models? I'm still using Claude Code as my main driver, but after this week I'm starting to think I should at least run some experiments. I'd love to hear from anyone who's tried it.

---

*Every week I skim dozens of AI videos on YouTube, pick out the ones that represent a real trend, translate them into "what changes for my own work," and add research grounding plus a hype filter. This edition covered the 42 most-viewed videos from August 4–10, 2026. The performance and pricing figures are claims made in the individual videos and I couldn't verify them myself, which is why I wrote the conditions and counterarguments into the text. The research I cite — FrugalGPT, SWE-bench, Reflexion — is all published papers.*

**Source videos**
- [China Just Dropped an AI 100x Cheaper That Beats Claude Fable 5](https://www.youtube.com/watch?v=A-2WKQxhI_8) — Vaibhav Sisinty
- [Meta's Claude Code clone is INSANELY cheap](https://www.youtube.com/watch?v=-Gj0-EIyx6g) — Theo
- [Kimi Code colocou o Claude Code pra chorar](https://www.youtube.com/watch?v=KHRNed37LvA) — mano deyvin
- [Affordable Claude Code in 3 steps](https://www.youtube.com/watch?v=fXSwktXhAOM) — Abhishek Veeramalla
- [Give ChatGPT and Claude the Same Memory](https://www.youtube.com/watch?v=NClayXM8pU0) — Nate Herk
- [Hermes AI Just Learned to Read Books](https://www.youtube.com/watch?v=0sDKQMO23xE) — Julian Goldie SEO
- [This NEW Claude Prompting Technique (gauntlet-loop)](https://www.youtube.com/watch?v=BNjzXcEXmg4) — Jay E RoboNuggets
- [I Let Claude Opus 5 Run a Business Alone for 9 Days](https://www.youtube.com/watch?v=vOK0Cdbk-Ps) — Ben Awad
- [Andrej Karpathy Just Fixed Claude Code's Biggest Weakness](https://www.youtube.com/watch?v=jI4ZVB_MPhU) — Dream Labs AI
- [OpenAI's Model Got Too Dangerous So They Locked It Up](https://www.youtube.com/watch?v=mH70ny2LcX4) — Universe of AI
