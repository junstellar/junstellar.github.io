---
title: "ROE란? 자기자본이익률의 뜻과 PER·PBR 함께 읽는 법"
description: "ROE의 뜻과 평균 자기자본을 이용한 계산법을 설명합니다. ROE와 주식 수익률의 차이, 부채와 자사주 매입이 미치는 영향, KB금융 사례를 살펴보고 PER·PBR·ROE를 함께 읽는 방법을 정리합니다."
slug: "roe-explained"
date: 2026-11-08T00:00:00+09:00
draft: false
image: "roe-cover.png"
categories: ["AI 투자"]
tags: ["ROE", "자기자본이익률", "PER", "PBR", "재무제표 보는 법"]
---

<style>
.article-content{container-type:inline-size}.re-intro{font-size:13px;opacity:.75}
.re{--paper:#f7f4ec;--ink:#193e37;--muted:#526b65;--card:#fffef9;--line:#cbd7cc;--teal:#16766b;--coral:#ad4d36;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:14px;margin:32px 0;padding:28px;line-height:1.7;word-break:keep-all;overflow-wrap:anywhere}.re *{box-sizing:border-box}.re p{margin:0}.re .kicker{font-size:12px;font-weight:800;color:var(--teal);letter-spacing:.04em;margin-bottom:10px}.re .figtitle{font-size:26px;line-height:1.4;font-weight:800;margin-bottom:22px}.re .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.re .card{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--teal);border-radius:9px;padding:20px;min-width:0}.re .label{font-size:14px;color:var(--muted)}.re .big{font-size:36px;font-weight:900;line-height:1.3;letter-spacing:-.04em;margin:13px 0;color:var(--teal)}.re .total{font-size:22px;font-weight:800;border-top:1px dashed var(--line);padding-top:14px;margin-top:16px}.re .note{font-size:12px;color:var(--muted);margin-top:18px}.re .strip{background:var(--card);border-left:4px solid var(--coral);padding:14px 18px;margin-top:18px;font-size:16px}.re .warm{border-top-color:var(--coral)}.re .warm .big{color:var(--coral)}
[data-scheme=dark] .re{--paper:#233c36;--ink:#f0f5ed;--muted:#b9cec0;--card:#2b453d;--line:#526e60;--teal:#a1e4d1;--coral:#ffb7a3}
@container(max-width:580px){.re{padding:22px 18px}.re .grid{grid-template-columns:1fr}.re .figtitle{font-size:23px}}
@media(max-width:600px){.re{padding:22px 18px}.re .grid{grid-template-columns:1fr}.re .figtitle{font-size:23px}}
</style>

<p class="re-intro">기업을 읽는 기초 · 세 번째 이야기 / 자료 확인: 2026.11.08</p>

## ROE는 자기자본으로 얼마나 이익을 냈는지 보여줍니다

<strong>ROE(Return on Equity, 자기자본이익률)는 회사가 자기자본에 비해 얼마나 순이익을 냈는지 나타내는 비율</strong>입니다. 보통 한 해의 순이익을 그 기간의 평균 자기자본으로 나누고 100을 곱해 계산합니다.

가게 두 곳이 모두 1년에 1,000만원을 남겼다고 해보겠습니다. 한 곳은 주인 몫의 자본 1억원으로, 다른 곳은 2억원으로 운영했다면 이익의 액수는 같아도 자본을 활용한 결과는 다릅니다. 각각 10%, 5%입니다. 물론 빚을 얼마나 썼는지, 위험은 비슷한지도 확인해야겠지요.

[지난 PBR 편](/p/pbr-explained/)에서는 장부상 순자산과 주가를 비교했습니다. 이번에는 그 순자산, 즉 자기자본으로 **얼마나 벌었는지**를 보겠습니다. 여기서 자기자본은 자산에서 부채를 뺀 장부상 금액입니다. 주주가 처음 낸 돈뿐 아니라 회사에 쌓아 둔 이익 등도 포함됩니다.

**ROE = 순이익 ÷ 평균 자기자본 × 100**

왜 평균을 쓸까요? 순이익은 1년 동안 벌어들인 금액인데, 재무상태표의 자기자본은 특정 날짜의 잔액이기 때문입니다. 한 해의 성과를 볼 때는 그 기간에 사용한 자본과 비교해야 자연스럽습니다. [CFA Institute 재무비율 정의](https://www.cfainstitute.org/sites/default/files/-/media/documents/support/programs/cfa/cfa_program_level_ii_financial_ratio_list.pdf)

## 자기자본 100억원으로 15억원을 벌면 ROE는 15%입니다

연초 자기자본이 80억원, 연말이 120억원인 가상 회사로 계산해 보겠습니다. 두 시점의 단순 평균은 100억원입니다. 이 회사가 그해 순이익 15억원을 냈다면 ROE는 15%입니다.

<div class="re" role="figure" aria-label="가상 회사: 연초 자기자본80억원, 연말120억원, 평균100억원. 연간 순이익15억원을 평균자기자본100억원으로 나누면 ROE15퍼센트">
<p class="kicker">설명용 예시 / 연초·연말 단순 평균 사용</p>
<div class="figtitle">자기자본의 평균과<br>한 해 순이익을 비교합니다.</div>
<div class="grid"><div class="card"><div class="label">평균 자기자본</div><div class="big">100억원</div><div>(연초 80억 + 연말 120억)<br>÷ 2</div><div class="total">비교할 자본의 크기</div></div><div class="card"><div class="label">연간 순이익</div><div class="big">15억원</div><div>순이익 15억 ÷ 평균 100억<br>× 100</div><div class="total">ROE 15%</div></div></div>
<p class="note">순이익 외에도 증자·배당 등으로 자본이 변할 수 있습니다. 실제 기업이 월별·분기별 평균을 쓰면 위 단순 평균과 결과가 달라질 수 있습니다.</p>
</div>

연말 자기자본 120억원으로만 나누면 12.5%가 나옵니다. 틀린 숫자를 눌렀기 때문이 아니라, 분모의 시점이 달라진 결과입니다. 앱이나 보고서의 ROE가 다를 때는 계산에 어떤 자기자본을 썼는지부터 봐야겠습니다.

연결재무제표에서는 범위도 맞춰야 합니다. 지배주주 순이익을 쓰면 자기자본도 지배주주 지분에 해당하는 평균 금액을 써야 합니다. 다른 주주 몫인 비지배지분까지 포함한 자본과 섞지 않는 것입니다. 우선주가 있다면 보통주 기준인지도 확인합니다.

그리고 ROE 15%는 **회사 자기자본의 수익성**입니다. 내가 증시에서 산 주식의 수익률 15%를 뜻하지 않습니다. 이 차이는 마지막에 PER·PBR과 연결하면 더 분명해집니다.

## 높은 ROE가 이익 증가 때문인지, 자본이 작아서인지 봅니다

ROE의 분자는 순이익, 분모는 자기자본입니다. 이익이 늘면 올라가지만, 이익이 그대로인데 자기자본이 작아져도 올라갑니다. 그래서 ‘ROE가 높으니 장사를 잘한다’고 바로 결론 내리기는 어렵습니다.

같은 규모의 가게를 자기 돈만으로 운영할 수도 있고, 일부를 빌려서 운영할 수도 있습니다. 빚을 쓰면 주인 자본이 적어도 같은 규모의 자산을 운용할 수 있습니다. 대신 이자를 내야 하고 원금도 갚아야 합니다.

아래 두 회사는 평균 자산 100억원으로 이자 지급 전 이익 10억원을 낸다고 가정했습니다. A는 전액 자기자본, B는 자기자본 50억원과 차입금 50억원을 씁니다. 차입금리는 연 5%, 세금은 없다고 단순화했습니다.

<div class="re" role="figure" aria-label="가상 비교: A는 자기자본100억 순이익10억 ROE10퍼센트. B는 자기자본50억 차입금50억, 이자2.5억을 빼 순이익7.5억 ROE15퍼센트">
<p class="kicker">설명용 예시 / 평균 자산 100억원 · 이자 전 이익 10억원</p>
<div class="figtitle">이익은 더 적어도,<br>ROE는 더 높을 수 있습니다.</div>
<div class="grid"><div class="card"><div class="label">A · 차입금 없음</div><div class="big">ROE 10%</div><div>평균 자기자본 100억원<br>이자 0원<br>순이익 10억원</div><div class="total">10억 ÷ 100억</div></div><div class="card warm"><div class="label">B · 차입금 50억원</div><div class="big">ROE 15%</div><div>평균 자기자본 50억원<br>연 이자 2.5억원<br>순이익 7.5억원</div><div class="total">7.5억 ÷ 50억</div></div></div>
<div class="strip">같은 사업 수익에서도 자금 조달 방식이 달라지면 ROE가 달라집니다.</div>
<p class="note">평균 자산·자본·차입금을 제시한 별도 가상 예시입니다. 세금과 기타 손익은 없고 차입금리는 연 5%로 고정했습니다. 실제 기업의 수치가 아닙니다.</p>
</div>

B가 A보다 물건을 더 잘 팔거나 비용을 더 줄인 것은 아닙니다. 더 작은 자기자본으로 사업을 하고 있어서 ROE가 높습니다. 사업이 나빠져 이자 전 이익이 2억원으로 줄면 A는 2억원을 남기지만, B는 이자 2.5억원을 내고 0.5억원의 적자가 됩니다. 빚이 수익성을 언제나 높여주는 것도 아닙니다.

같은 이유로 배당이나 [자사주 매입](/p/share-buyback-vs-cancellation/)도 함께 봐야 합니다. 회사가 현금을 주주에게 돌려주거나 자기주식을 사들이면 장부상 자기자본이 줄 수 있습니다. 그 뒤 순이익이 유지된다면 평균 자기자본이 작아져 ROE가 높아질 수 있습니다. 불필요하게 쌓인 자본을 효율적으로 쓰는 선택일 수도 있지만, 그 자체가 영업 경쟁력이 좋아졌다는 증거는 아닙니다. 이미 사들인 자기주식을 소각할 때 매입 때와 같은 자본 감소가 다시 생기는 것으로 중복 계산해서도 안 됩니다.

이익이 왜 늘었는지도 중요합니다. 상품을 더 많이 팔아 번 돈인지, 건물을 팔아 한 번 생긴 이익인지에 따라 다음 해에도 기대할 수 있는 금액이 달라집니다.

ROE를 순이익률·자산회전율·재무레버리지로 나눠 살피는 방식을 **듀퐁 분석**이라고 부릅니다. 처음에는 공식을 외우기보다 ‘매출에서 더 남겼나, 자산으로 더 많이 팔았나, 자기자본에 비해 부채를 많이 썼나’라는 세 질문으로 이해하면 편합니다. [CFA Institute 재무분석 설명](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques)

## KB금융의 ROE도 숫자 옆의 실적 설명을 같이 읽었습니다

지난 편에서 본 KB금융 자료를 다시 펼쳐보겠습니다. 회사는 **2025년 연간 ROE 10.86%**, 당기순이익 **5조 8,430억원**을 발표했습니다. 여기서는 현재 주가나 최신 분기 전망이 아니라, 2025년 실적을 설명한 당시 자료를 읽습니다.

| 발표에서 확인한 내용 | 함께 읽을 이유 |
|---|---|
| 2025년 ROE 10.86% | 해당 연도의 자본 대비 수익성을 보여줍니다. |
| 은행·증권 등 핵심 계열사 이익과 비이자 부문 실적 확대 | 어떤 사업에서 이익이 늘었는지 볼 수 있습니다. |
| 2024년 ELS 고객보상비용 등 큰 일회성 영향의 소멸 | 전년도에 있었던 비용이 사라진 효과도 실적 개선에 포함됩니다. |

출처: [KB금융 2025년 공식 실적발표 설명문](https://m.kbfg.com/IR_new/2025_4/player/vod_kor.html)

이 자료를 읽으면서 저는 ROE 옆에 <strong>‘왜 이익이 늘었는가’</strong>를 한 줄 더 적어 두는 게 도움이 됐습니다. 사업에서 더 벌어들인 부분과 과거의 큰 비용이 사라진 부분을 구분하면, 다음 해에도 이어질 수익성을 생각하기가 조금 쉬워집니다. 이 설명만으로 각각의 효과를 정확히 분리해 계산했다는 뜻은 아닙니다.

은행은 예금을 받아 대출하는 사업이므로 일반 제조업과 자산·부채 구조가 다릅니다. 금융회사와 제조업체의 ROE를 숫자 하나로 겨루게 하기보다는, 같은 회사의 여러 해와 사업 구조가 비슷한 회사들을 비교하는 편이 낫겠습니다.

## ROE 15%인 회사를 사도 내 수익률이 15%가 되지는 않습니다

여기서 가장 헷갈리기 쉬운 부분이 나옵니다. 회사가 가진 자기자본과 **내가 주식을 사면서 낸 가격은 다릅니다.** 이미 발행된 주식을 시장에서 산다면, 내가 낸 돈은 보통 그 주식을 판 사람에게 갑니다. 회사의 장부에 그만큼 자기자본이 새로 들어가는 거래가 아닙니다.

자기자본 100억원인 회사가 순이익 15억원을 낸다고 해보겠습니다. 이 회사의 주식 전체를 시장에서 150억원으로 평가할 때와 300억원으로 평가할 때, 사업의 ROE는 같아도 내가 이익을 사는 가격은 두 배 차이입니다.

<div class="re" role="figure" aria-label="같은 가상 회사: 순이익15억 자기자본100억 ROE15퍼센트. 시총150억이면 PER10배 PBR1.5배, 시총300억이면 PER20배 PBR3배">
<p class="kicker">설명용 예시 / 순이익 15억원 · 평균·기말 자기자본 모두 100억원</p>
<div class="figtitle">같은 ROE 15%라도,<br>주식을 사는 가격은 다릅니다.</div>
<div class="grid"><div class="card"><div class="label">시가총액 150억원일 때</div><div class="big">PER 10배</div><div>150억 ÷ 순이익 15억<br>PBR = 150억 ÷ 자본 100억</div><div class="total">PBR 1.5배</div></div><div class="card warm"><div class="label">시가총액 300억원일 때</div><div class="big">PER 20배</div><div>300억 ÷ 순이익 15억<br>PBR = 300억 ÷ 자본 100억</div><div class="total">PBR 3배</div></div></div>
<div class="strip">사업의 수익성과 주식에 지불하는 가격을 함께 봐야 합니다.</div>
<p class="note">앞의 계산 예시와 별개인 가상 회사입니다. 보통주만 있고 주식 수·계산 범위가 같다고 가정합니다. 미래 수익률이나 적정 주가를 계산한 것이 아닙니다.</p>
</div>

150억원에 평가될 때 순이익은 가격의 10%, 300억원일 때는 5%입니다. 이것이 PER의 역수인 **이익수익률**입니다. 하지만 순이익이 전부 배당되는 것도 아니고, 앞으로 같은 이익을 낸다는 보장도 없습니다. 이익수익률 역시 주식 투자자가 실제로 얻을 수익률과 같지는 않습니다.

내 투자 결과는 매수 가격과 매도 가격, 받은 배당 등에 따라 결정됩니다. ROE가 높은 회사여도 기대가 과하게 반영된 가격에 사면 손실을 볼 수 있습니다. 반대로 낮은 ROE가 개선되는 기업도 있을 수 있습니다. 그래서 좋은 사업인지와 좋은 가격인지를 따로 묻는 것입니다.

## PER·PBR·ROE를 함께 놓으면 가격과 수익성이 연결됩니다

이제 세 편에서 공부한 숫자를 한곳에 놓아보겠습니다.

| 지표 | 비교하는 것 | 먼저 떠올릴 질문 |
|---|---|---|
| PER | 가격 ÷ 이익 | 회사가 버는 돈의 몇 배를 주고 사나요? |
| PBR | 가격 ÷ 자기자본 | 장부상 순자산의 몇 배를 주고 사나요? |
| ROE | 이익 ÷ 자기자본 | 그 자본으로 얼마나 벌었나요? |

분자와 분모를 같은 기준으로 맞추면 연결식도 나옵니다.

**PBR = PER × ROE(소수로 표시)**

가상 예시의 10배 × 0.15 = 1.5배, 20배 × 0.15 = 3배가 여기에 해당합니다. ‘가격 ÷ 이익’에 ‘이익 ÷ 자기자본’을 곱하면 중간의 이익이 약분되어 ‘가격 ÷ 자기자본’이 남습니다.

다만 실제 앱의 숫자가 딱 맞지 않는다고 오류라고 단정하면 안 됩니다. **일반적인 ROE는 평균 자기자본, PBR은 특정 시점의 자기자본을 씁니다.** 같은 순이익·시가총액 범위라면 정확한 연결은 ‘PBR = PER × ROE × 평균 자기자본 ÷ PBR에 사용한 자기자본’입니다. 여기에 PER이 예상 이익 기준인지, 주식 수와 비지배지분 처리가 같은지도 영향을 줍니다.

그리고 이 식은 **관계를 설명하는 식이지 목표 주가 공식이 아닙니다.** PER과 ROE 중 무엇을 가정하느냐에 따라 결과가 달라집니다. ROE 15%니까 PBR 1.5배가 적정하다고 정해 주는 식도 아닙니다.

그래도 세 지표를 함께 보면 질문이 구체적으로 바뀝니다. PBR이 낮은 기업이라면 자본으로 버는 이익도 낮아서 그런지 볼 수 있습니다. ROE가 높은 기업이라면 그 수익성이 계속될지, 높은 가격을 이미 지불하고 있는지 확인할 수 있습니다.

## 정리

ROE는 **평균 자기자본에 비해 얼마나 순이익을 냈는지** 보여줍니다. 높으면 눈길이 가지만, 이익의 증가뿐 아니라 부채 사용이나 자기자본 감소로도 높아질 수 있습니다. 한 해의 숫자보다 같은 기준으로 여러 해를 비교하고, 이익의 내용과 자본의 변화를 같이 읽으려 합니다.

처음 확인할 때는 세 가지를 적어 두면 좋겠습니다. <strong>얼마나 벌었는지, 얼마의 자기자본으로 벌었는지, 나는 그 회사에 얼마의 가격을 지불하는지.</strong> 순이익이나 자기자본이 0·음수라면 일반적인 비율 비교부터 멈추고 적자와 자본 상태를 먼저 살펴야 합니다. 적자와 음수 자본을 나눠 양수 ROE가 나왔다고 좋은 수익성으로 읽어서는 안 됩니다.

이 글로 **기업을 읽는 기초 3편을 마칩니다.** [1편 PER](/p/per-explained/)에서는 이익과 가격을, [2편 PBR](/p/pbr-explained/)에서는 순자산과 가격을 봤습니다. ROE까지 연결하고 나니, ‘낮으면 싸다, 높으면 좋다’로 외우기보다 그 숫자가 만들어진 이유부터 묻게 됩니다.

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
