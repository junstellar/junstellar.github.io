---
title: "Even a Typo Fix From Claude Gets Stamped — The New Baseline in the AI Watermark Era"
description: "Anthropic has started embedding invisible watermarks in every piece of text Claude produces. The catch: the mark doesn't say 'who wrote this,' only 'this passed through AI.' Fixing typos gets stamped the same way. Here's what changed and how to handle it."
slug: "ai-trend-2026-08-w3"
date: 2026-08-20T21:30:00+09:00
draft: false
categories: ["AI 트렌드"]
tags: ["AI Trends", "Watermark", "EU AI Act", "Claude", "AI Ethics", "Prompting", "Weekly Roundup"]
---

[Last week](/en/p/ai-trend-2026-08-w2/) was nothing but pricing talk, but this week the mood flipped completely. I was skimming the video list my laptop scrapes every night, and the number one spot went to this: **"Americans have turned against AI."** 220,000 views.

A week that jumped straight from money to trust.

## Three-line summary

- **Every piece of text Claude generates** now carries an invisible watermark. It's a response to the EU AI Act.
- But the mark only says **"this passed through AI,"** not "AI wrote this." Fix a typo and it still shows up.
- On the other side of the week, the word is that **the fewer instructions you give, the better the results**. Prompting common sense is getting flipped.

## Anything Claude writes gets stamped

As of August 2, Anthropic started putting watermarks into the text and files Claude generates. It's a move aligned with the transparency obligations in the EU AI Act.

Two mechanisms run side by side. Text gets an invisible statistical mark, and files get a provenance metadata signature called **C2PA**.

The mechanism is kind of fun.

![Watermarking nudges output word probabilities to leave a statistical trace, then traces it back to detect the mark](watermark.png)

When the model picks the next word, it nudges the probability of certain candidates up ever so slightly. A person reading it notices nothing, but over a long enough stretch of text that bias shows up statistically. It's the approach from **"A Watermark for Large Language Models,"** presented at ICML 2023, and what shipped here is in the same family.

So the sentence quality stays exactly as it was and only the trace is left behind. Pretty clever.

## The problem is it doesn't separate "wrote it" from "passed through it"

This is the part that really matters.

![From typo fixes to fully generated drafts — the watermark doesn't distinguish between these four](spectrum.png)

Take something you wrote yourself, drop it into Claude, and **fix nothing but the typos** — the watermark attaches anyway. Same with translation, same with summarizing. The mark only says "this text passed through AI." It tells you nothing about who wrote it.

That could get awkward anywhere AI usage is sensitive, like a school or an office. The person who generated an entire draft and the person who fixed one typo end up wearing the same mark.

> **So what does this mean for me?**
> If it's a document you're submitting, **it's safer to state up front how far AI was involved**. Writing "used for translation only" from the start beats explaining yourself after someone detects the mark.

And predictably, watermark removal tools are already showing up on GitHub. The arms race has begun. That said, rather than straining to break through it, **disclosing and moving on** is going to be the easier path in the end.

One more thing. This only applies to commercial models like Claude. [Open models running on my own laptop](/en/p/llama-cpp-local-llm/) carry no such mark. If you handle sensitive documents, that's an option worth keeping.

## The public is already walking away

The most-viewed video this week was "Americans Have Turned Against AI." 220,000 views is an overwhelming number in this corner of YouTube.

The content is heavy. Job losses, data center power and water consumption, copyright infringement. AI adoption keeps climbing while trust keeps sliding.

There was a video in a similar vein, too. It's titled "Wait, let me ask ChatGPT," and it's about the **decline in critical thinking** that comes from leaning on AI. Psychology calls this **cognitive offloading**. Same principle as your mental arithmetic getting rusty once you start using a calculator — except this time what's being offloaded is judgment, which makes it a different conversation.

Layered on top of that are surveillance worries. The ChatGPT desktop app picked up a **computer activity logging** feature. It learns what you do so it can take repetitive work off your hands, but flip it around and it means something is watching your screen the whole time. One podcast panel recommended **turning it on only on a work-dedicated machine**. I'm with them on that.

## What I took away this week

**Write down your AI usage scope first.** For anything you're submitting, leave one line at the bottom like "AI used for translation and proofreading." In an era where watermarks come standard, that's the cheapest insurance available.

**Send sensitive documents to a local model.** No watermark attached, and your data never leaves the machine.

**Separate your devices for the activity logging feature.** If you turn it on, work-dedicated machine only. Don't enable it on a personal device.

**Claude Code got a `/design` command.** The flow is to pull up design mockups, pick one, and only then move on to writing code. Fewer cases of building the whole thing and then going "yeah, this isn't it" and tearing it down.

**Keep three documents in your project folder.** One video walked through this and it's genuinely usable. A doc describing how you work, a doc describing what matters right now, and a doc describing how to judge the output. Put those three in place and the AI picks up the context on its own.

## If I keep only one thing — give fewer instructions

From here on this isn't this week's news, it's the part with a longer shelf life.

A Claude Code developer reportedly said this: **deleting 80% of the system prompt made the results better**.

![Giving goals and verification criteria instead of piling on instructions](hobbling.png)

The claim is that the smarter the model gets, the more that fine-grained step-by-step instruction holds it back. The industry apparently calls this **hobbling**. Literally, tying its feet together.

So what should you give it instead? Two things.

1. **What needs to be accomplished** (not how to do it)
2. **How to prove that it's done**

The Ramp case from last week was saying exactly the same thing. They cut CI time to a third by instructing "what to achieve" instead of "how to do it." That's two weeks running landing on the same conclusion.

Honestly, I've been doing the opposite. When the results were weak I'd pile on more instructions. After this week's material, I figure it's time to strip a prompt back and see what happens.

## Worth flagging

Some of this week's headlines were pretty aggressive. Things like **"GPT-6 Astra just destroyed Claude AI."**

Look at the actual content and Astra solved 10 unsolved math problems, machine-verified with a proof checker called Lean 4. That's a genuinely impressive result.

Except in the same week, **Claude also made progress on the Riemann hypothesis**. It reportedly pushed the lower bound on the proportion of zeros satisfying the condition from the human-established 41.6% up to 67.2%. Not a proof of the hypothesis itself, but a meaningful improvement.

So instead of a "destroyed it" headline, **both sides are making progress in math** is closer to the truth. And the shared observation across the videos was that Astra looks like a research system rather than a consumer product. It's not something we can go use right now.

The price cuts kept coming as well. OpenAI cut up to 80%, and the free gateway talk surfaced again. [Last week's trend](/en/p/ai-trend-2026-08-w2/) is carrying straight through.

## The rest, briefly

- **Google Pixel 11 / Pixel Watch 5** announced. On-device AI, offline Gemini, and trend detection for blood pressure and insulin resistance.
- **Gemini** got a feature that **removes** image watermarks. One side puts them in, the other side takes them out — an odd picture.
- **MiniMax H3** drew good reviews for open-source video generation. Being able to run it locally is the strong point.
- **"Unlimited" is disappearing.** Suno and other AI services that advertised "unlimited" are putting usage caps in place one by one.
- A leak went around that **Claude Fable 5.1** is close to release.

## Just one thing this week

**Leave a single line on any document where you used AI.** Something like "AI was used for translation and proofreading on this piece" is plenty.

Now that watermarks are the default, hiding it only gets more exhausting. Say it first and the whole thing is over. I'm still weighing whether to put that line on this blog.

Where do you draw the line on what counts as "my writing"? Is typo correction fine but draft generation not? I haven't managed to draw that line either.

---

*Every week I skim dozens of AI videos on YouTube, pick out the ones that add up to a trend, translate them into "what changes in my own work," and attach research grounding plus an exaggeration filter. This edition covered the top-viewed videos from August 12–19, 2026. Performance numbers are the values claimed in each video, so I couldn't verify them directly — where there were counterarguments, I wrote those in too. The ICML 2023 paper cited for how watermarking works, along with C2PA and the EU AI Act, are publicly available material.*

**Source videos**
- [Americans Have Turned Against AI](https://www.youtube.com/watch?v=14Uc2WCSPiw) — The Infographics Show
- [🚨 이제 AI로 글 쓰면 다 걸립니다](https://www.youtube.com/watch?v=8OKKeF86O5c) — 조코딩 JoCoding
- [Claude Is Hiding Watermarks in Your AI Text](https://www.youtube.com/watch?v=rR2QW5WQ3aE) — Kyle Balmer
- ["Wait, let me ask ChatGPT"](https://www.youtube.com/watch?v=3wy5cOBxYno) — Bryony Claire
- [Casey Newton on ChatGPT's New Feature](https://www.youtube.com/watch?v=altkJOZPK3g) — Pod Save America
- [I Deleted All My Claude Skills... And Claude Got Smarter](https://www.youtube.com/watch?v=XNQBCRcwXV4) — Nate Herk
- [Claude Code New Features, Explained](https://www.youtube.com/watch?v=SkY-tR9kf-k) — Greg Isenberg
- [리만 가설에 도전한 클로드의 놀라운 결과](https://www.youtube.com/watch?v=-raeMYTV1lg) — 조코딩 JoCoding
- [GPT-6 Astra: OpenAI's Next Model Just Destroyed Claude AI](https://www.youtube.com/watch?v=Elwg-3Ql8u0) — AI Master
- [Probé Claude Code Design y es...](https://www.youtube.com/watch?v=4s-CA76dROQ) — midudev
