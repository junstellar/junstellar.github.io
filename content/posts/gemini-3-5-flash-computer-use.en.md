---
title: "Google Builds 'Computer Use' Into Gemini 3.5 Flash — 'GPT-Level Performance at One-Third the Price'"
description: "Google built 'Computer Use' natively into Gemini 3.5 Flash, letting it see the screen and click directly. A look at this observe-think-act automation agent."
slug: "gemini-3-5-flash-computer-use"
date: 2026-06-28T10:00:00+09:00
draft: false
categories: ["AI 트렌드"]
tags: ["AI", "Google", "Gemini", "computer-use"]
---

On June 24, Google announced that it is building a 'Computer Use' capability — which lets the model look at a screen and operate it directly — natively into its generative AI model, Gemini 3.5 Flash. Rather than routing through a separate dedicated model, the flagship model itself recognizes browser, mobile, and desktop screens and performs clicks and inputs. It is currently offered as a public preview.

Computer Use is a capability in which the AI captures and recognizes the screen like a screenshot, identifies UI elements such as buttons or input fields, and actually clicks and types at the corresponding coordinates. By repeating an observe–think–act loop, it stands in for tasks a person would perform on a computer. Google said the feature lets developers build automation agents that work not only in the browser but also in mobile and desktop environments.

That said, screen-operation features themselves are not new. Anthropic introduced 'Computer Use' to Claude back in October 2024, and OpenAI unveiled a similar capability with 'Operator' in early 2025. Google, too, had been offering related functionality through a separate model called 'Gemini 2.5 Computer Use.' The crux of this announcement is not novelty, but that a feature once split off into a separate model has been integrated into the flagship Flash model and combined with a one-million-token context. This is seen as boosting its usefulness for long-running automation tasks such as continuous software testing.

What drew the industry's attention was performance relative to price. According to Google, Gemini 3.5 Flash scored 78.4% on 'OSWorld Verified,' a benchmark measuring computer-operation performance — on par with the rival GPT-5.5. Its pricing, meanwhile, was set at roughly one-third for both input and output.

| Item | Gemini 3.5 Flash (Computer Use) | GPT-5.5 |
|---|---|---|
| Computer operation | Natively built into the model | Supported (Operator line) |
| OSWorld Verified bench | 78.4% | ~79% (close) |
| Input price (1M tokens) | $1.50 | $5.00 |
| Output price (1M tokens) | $9.00 | $30.00 |
| Context | 1M tokens | — |
| Operation scope | Browser, mobile, desktop | Mainly browser |

This price competitiveness has made it a hot topic, with tech content creators at home and abroad releasing hands-on test videos one after another right after the announcement. Analysts attribute this to the timing — search traffic concentrates on cutting-edge topics — combined with the intuitive framing of 'comparable performance at one-third the price,' and the competitive dynamic among OpenAI, Anthropic, and Google. On the same day, Google also added a 'Select from screen' feature to Gemini for Chrome, letting users designate a region of the screen.

On the security front, Google said it applied adversarial training to defend against prompt-injection attacks, and provides an optional safeguard that requires user confirmation for sensitive or irreversible actions.

For now, the feature is in public preview rather than general availability (GA), and Google has not officially stated when it will move to GA. The Gemini API changelog also marks it as 'preview,' prompting observers to note that its current status should be re-confirmed before applying it to work involving real customer data or payments. The feature is available through the Gemini API and the Gemini Enterprise Agent Platform.

---

Sources: [Google official blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) · [Gemini API changelog](https://ai.google.dev/gemini-api/docs/changelog) · [TechTimes (6/25)](https://www.techtimes.com/articles/319071/20260625/gemini-computer-use-baked-gemini-35-flash-screen-control-now-pairs-search-maps.htm) · [9to5Google (6/24)](https://9to5google.com/2026/06/24/gemini-chrome-select-screen/) · [The Next Web](https://thenextweb.com/news/google-gemini-3-5-flash-computer-use-built-in-tool)
