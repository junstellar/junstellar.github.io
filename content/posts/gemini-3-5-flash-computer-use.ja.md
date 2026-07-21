---
title: "グーグル、Gemini 3.5 Flash に「コンピューター・ユース」を内蔵… 「性能はGPT級、価格は3分の1」"
description: "グーグルがGemini 3.5 Flashに、画面を直接見てクリック・入力する「コンピューターユース」を標準搭載した。観察・判断・実行を繰り返す自動化エージェント機能を整理した。"
slug: "gemini-3-5-flash-computer-use"
date: 2026-06-28T10:00:00+09:00
draft: false
categories: ["AI 트렌드"]
tags: ["AI", "Google", "Gemini", "コンピューターユース"]
---

グーグルは6月24日、自社の生成AIモデル「Gemini 3.5 Flash」に、画面を直接見て操作する「コンピューター・ユース（Computer Use）」機能を標準で内蔵すると発表した。専用の別モデルを介さず、主力モデル自体がブラウザ・モバイル・デスクトップの画面を認識してクリックや入力を行う形で、現在はパブリックプレビューとして提供されている。

コンピューター・ユースは、AIが画面をスクリーンショットのように取り込んで認識し、画面内のボタンや入力欄といったUI要素を判断して、その座標を実際にクリック・入力する機能だ。観察（observe）・思考（think）・実行（act）の過程を繰り返し、人がコンピューターで行う作業を代わりに担う。グーグルは、この機能によって開発者がブラウザだけでなくモバイル・デスクトップ環境でも動く自動化エージェントを作れると説明した。

ただし、画面操作機能そのものは新しいものではない。先んじてアンソロピックが2024年10月にClaudeへ「コンピューター・ユース」を導入し、OpenAIも2025年初頭に「Operator」で同様の機能を披露している。グーグルもこれまで「Gemini 2.5 Computer Use」という別モデルで関連機能を提供してきた。今回の発表の核心は機能の新規性ではなく、別モデルに分かれていた機能を主力のFlashモデルに統合し、100万トークン規模のコンテキストと組み合わせた点にある。これにより、連続的なソフトウェアテストなど長時間の自動化作業での有用性が高まったと評価されている。

業界の関心が集まったのは、性能に対する価格だ。グーグルによると、Gemini 3.5 Flash はコンピューター操作性能の評価「OSWorld Verified」ベンチマークで78.4%を記録し、競合のGPT-5.5と同等の水準を示した。一方、利用料金は入力・出力ともに約3分の1の水準に設定された。

| 項目 | Gemini 3.5 Flash (Computer Use) | GPT-5.5 |
|---|---|---|
| コンピューター操作 | 本体にネイティブ内蔵 | 対応（Operator系） |
| OSWorld Verified ベンチ | 78.4% | 約79%台（近接） |
| 入力価格（100万トークン） | $1.50 | $5.00 |
| 出力価格（100万トークン） | $9.00 | $30.00 |
| コンテキスト | 100万トークン | — |
| 操作範囲 | ブラウザ・モバイル・デスクトップ | 主にブラウザ |

こうした価格競争力により、発表直後から国内外の技術コンテンツ制作者が実地テスト動画を相次いで公開し、話題となっている。最新トピックに検索流入が集中する時期である上、「性能は同等で価格は3分の1」という直感的な構図、そしてOpenAI・アンソロピック・グーグル間の競争構図がかみ合った結果と分析されている。同日、グーグルはChrome向けGeminiに、画面の領域を指定する「Select from screen」機能も併せて追加した。

セキュリティ面では、グーグルはプロンプトインジェクション攻撃を防ぐための敵対的学習を適用し、機微または取り消せない操作についてはユーザー確認を求める任意の安全装置を提供するとした。

なお、当該機能は現在、正式提供（GA）ではなくパブリックプレビュー段階であり、グーグルは正式移行の時期を公式には明らかにしていない。Gemini APIのチェンジログにも「preview」と表記されており、実際の顧客データや決済を伴う業務に適用する前には現状を再確認する必要があるとの指摘が出ている。機能はGemini APIおよびGemini Enterprise Agent Platformを通じて利用できる。

---

出典: [Google公式ブログ](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) · [Gemini API チェンジログ](https://ai.google.dev/gemini-api/docs/changelog) · [TechTimes (6/25)](https://www.techtimes.com/articles/319071/20260625/gemini-computer-use-baked-gemini-35-flash-screen-control-now-pairs-search-maps.htm) · [9to5Google (6/24)](https://9to5google.com/2026/06/24/gemini-chrome-select-screen/) · [The Next Web](https://thenextweb.com/news/google-gemini-3-5-flash-computer-use-built-in-tool)
