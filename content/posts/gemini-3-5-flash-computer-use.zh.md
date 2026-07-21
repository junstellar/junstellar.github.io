---
title: "谷歌将「电脑操作（Computer Use）」内置进 Gemini 3.5 Flash —「性能比肩 GPT，价格仅三分之一」"
description: "谷歌在 Gemini 3.5 Flash 中原生内置了“计算机操作”——直接查看屏幕并点击、输入。本文梳理了这一反复“观察—判断—执行”的自动化智能体功能。"
slug: "gemini-3-5-flash-computer-use"
date: 2026-06-28T10:00:00+09:00
draft: false
categories: ["AI 트렌드"]
tags: ["AI", "谷歌", "Gemini", "电脑操作"]
---

谷歌于 6 月 24 日宣布，将「电脑操作（Computer Use）」功能——即让模型直接查看并操作屏幕——原生内置进其生成式 AI 模型「Gemini 3.5 Flash」。无需经过单独的专用模型，主力模型本身即可识别浏览器、移动端与桌面端的屏幕并执行点击与输入，目前以公开预览（public preview）形式提供。

电脑操作是指：AI 像截图一样捕捉并识别屏幕，判断画面中的按钮、输入框等 UI 元素，并在相应坐标实际进行点击与输入。它反复进行「观察（observe）—思考（think）—执行（act）」的过程，代替人在电脑上完成的工作。谷歌表示，借助该功能，开发者不仅能在浏览器中，也能在移动端和桌面端构建可运行的自动化智能体。

不过，屏幕操作功能本身并不新鲜。此前 Anthropic 已于 2024 年 10 月在 Claude 中引入「Computer Use」，OpenAI 也在 2025 年初以「Operator」展示了类似功能。谷歌此前同样以名为「Gemini 2.5 Computer Use」的独立模型提供相关功能。本次发布的核心并非功能的新颖性，而在于把原本分离为独立模型的功能整合进主力 Flash 模型，并与百万 token 规模的上下文相结合。业界因此认为，它在连续软件测试等长时间自动化任务中的可用性大幅提升。

业界关注的焦点是性能与价格之比。据谷歌称，Gemini 3.5 Flash 在衡量电脑操作性能的「OSWorld Verified」基准测试中取得 78.4% 的成绩，与竞品 GPT-5.5 处于相近水平。而使用费用方面，输入与输出均定在约三分之一的水平。

| 项目 | Gemini 3.5 Flash (Computer Use) | GPT-5.5 |
|---|---|---|
| 电脑操作 | 原生内置于模型 | 支持（Operator 系） |
| OSWorld Verified 基准 | 78.4% | 约 79%（接近） |
| 输入价格（百万 token） | $1.50 | $5.00 |
| 输出价格（百万 token） | $9.00 | $30.00 |
| 上下文 | 百万 token | — |
| 操作范围 | 浏览器、移动端、桌面端 | 主要为浏览器 |

凭借这样的价格竞争力，发布后国内外的技术内容创作者纷纷公开实测视频，引发热议。分析认为，这一方面源于最新话题正值搜索流量集中的时机，另一方面也得益于「性能相当、价格仅三分之一」这一直观对比，以及 OpenAI、Anthropic、谷歌之间的竞争格局相互叠加。同日，谷歌还为 Chrome 版 Gemini 新增了可指定屏幕区域的「Select from screen」功能。

在安全方面，谷歌表示已应用对抗训练以防范提示注入（prompt injection）攻击，并针对敏感或不可逆的操作提供需用户确认的可选安全机制。

另一方面，该功能目前处于公开预览阶段，而非正式发布（GA），谷歌也未正式说明转为正式版的时间。Gemini API 更新日志中亦标注为「preview」，因此有观点指出，在将其应用于涉及真实客户数据或支付的业务之前，应再次确认其当前状态。该功能可通过 Gemini API 与 Gemini Enterprise Agent Platform 使用。

---

来源: [谷歌官方博客](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) · [Gemini API 更新日志](https://ai.google.dev/gemini-api/docs/changelog) · [TechTimes (6/25)](https://www.techtimes.com/articles/319071/20260625/gemini-computer-use-baked-gemini-35-flash-screen-control-now-pairs-search-maps.htm) · [9to5Google (6/24)](https://9to5google.com/2026/06/24/gemini-chrome-select-screen/) · [The Next Web](https://thenextweb.com/news/google-gemini-3-5-flash-computer-use-built-in-tool)
