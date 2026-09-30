---
title: "AI 기업의 적자, 성장통일까 사업의 한계일까? · AI 수익화 교과서 ②"
description: "AI 매출이 늘어도 적자가 나는 이유는 무엇일까요? 피그마의 실제 손익계산서, 무료 이용자의 AI 비용 분류, 주식보상과 조정 이익을 통해 흑자 전환 가능성을 읽는 법을 살펴봅니다."
slug: "ai-inference-cost"
date: 2026-09-30T11:00:00+09:00
draft: false
image: "ai-revenue-2-cover.jpg"
categories: ["AI 투자"]
tags: ["AI 투자", "AI 수익화", "AI 기업 실적", "AI 추론 비용", "피그마"]
---

<style>
.article-content{container-type:inline-size}.ar2{--paper:#f6f3ea;--card:#fffef9;--ink:#193b3a;--muted:#586d68;--line:#cbd6ce;--teal:#136d67;--coral:#ac4935;--blue:#3369a0;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:8px;padding:30px;margin:34px 0;line-height:1.7;word-break:keep-all;overflow-wrap:anywhere}.ar2 *{box-sizing:border-box}.ar2 p{margin:0}.ar2 .eyebrow{font-size:11px;letter-spacing:.1em;color:var(--teal);font-weight:800;margin-bottom:12px}.ar2 .fig-title{font-size:26px;line-height:1.4;font-weight:800;letter-spacing:-.035em;margin-bottom:20px}.ar2 .note{font-size:12px;color:var(--muted);line-height:1.8;margin-top:18px}.ar2 .steps{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.ar2 .tile{min-width:0;padding:20px 16px;background:var(--card);border:1px solid var(--line);border-top:4px solid var(--teal);font-size:14px}.ar2 .tile b{display:block;font-size:20px;margin:8px 0}.ar2 .small{font-size:12px;color:var(--muted)}.ar2 .band{padding:18px;background:var(--card);border-left:4px solid var(--teal);margin-top:18px;font-size:15px}.ar2 .buttons{display:flex;flex-wrap:wrap;gap:10px;margin-bottom:18px}.ar2 button{font:inherit;font-size:13px;padding:10px 14px;min-height:44px;cursor:pointer;background:var(--card);color:var(--ink);border:1px solid var(--teal);border-radius:24px}.ar2 button[aria-pressed=true]{background:var(--teal);color:var(--card)}.ar2 button:focus-visible{outline:3px solid var(--coral);outline-offset:3px}.ar2 .row{display:grid;grid-template-columns:1fr auto;gap:14px;padding:13px 0;border-bottom:1px solid var(--line);font-size:15px;align-items:center}.ar2 .row strong{font-size:23px;white-space:nowrap}.ar2 .row small{display:block;font-size:12px;color:var(--muted)}.ar2 .result{padding:18px;border:2px solid var(--teal);background:var(--card);margin-top:17px}.ar2 .result strong{color:var(--teal)}.ar2 .result.loss{border-color:var(--coral)}.ar2 .result.loss strong{color:var(--coral)}.ar2 .meter{height:15px;background:var(--line);border-radius:8px;overflow:hidden;margin:12px 0}.ar2 .meter span{display:block;height:100%;background:var(--coral);width:10%}.ar2 .equation{display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:14px;padding:20px;background:var(--card);font-size:21px;font-weight:800}.ar2 .equation span{color:var(--teal);font-size:32px}.ar2 .equation .up{color:var(--coral)}
[data-scheme=dark] .ar2{--paper:#233731;--card:#2c423c;--ink:#edf4ed;--muted:#b8cdc2;--line:#526e61;--teal:#9cddcb;--coral:#ffb399;--blue:#a6cef4}
@container(max-width:600px){.ar2{padding:23px 18px}.ar2 .steps{grid-template-columns:1fr}.ar2 .fig-title{font-size:23px}.ar2 .row strong{font-size:20px}}
@media(max-width:600px){.ar2{padding:23px 18px}.ar2 .steps{grid-template-columns:1fr}.ar2 .fig-title{font-size:23px}.ar2 .row strong{font-size:20px}}
</style>

손님이 늘어나는 식당인데 장부는 적자입니다. 새 매장을 준비하느라 돈을 많이 쓴 것일 수도 있고, 음식값으로 재료비조차 감당하지 못하는 것일 수도 있습니다. 둘 다 적자지만, 기다리면 나아질 가능성은 같지 않습니다.

AI 기업을 볼 때도 비슷한 질문이 생깁니다. **“매출은 이렇게 늘어나는데 왜 적자일까? 지금 투자하느라 못 버는 걸까, 이 방식으로는 돈을 벌기 어려운 걸까?”**

[1편](/p/how-ai-makes-money/)에서는 AI를 활용하는 기업이 실제로 흑자인지 확인했습니다. 이번에는 한 걸음 더 들어가 **손익계산서의 어디에서 이익이 사라지는지** 보겠습니다. 연구개발비가 크다고 무조건 성장통도 아니고, 추론 비용이 늘었다고 곧바로 실패한 사업도 아닙니다.

결론부터 말씀드리면, ‘성장통’은 적자에 붙여주는 별명이 아니라 **앞으로의 실적으로 입증해야 할 주장**입니다.

## 01 적자라는 결과보다, 어디에서 손실이 나는지가 중요합니다

서비스를 팔아 받은 매출에서 회사가 매출원가로 분류한 비용을 빼면 **매출총이익**이 나옵니다. 여기서 연구개발·판매·관리 등의 영업비용을 더 빼면 **영업이익 또는 영업손실**입니다.

이 구분으로 첫 질문을 좁힐 수 있습니다. 서비스 제공에 해당하는 비용부터 매출보다 큰지, 그 단계에서는 이익이 나지만 나머지 비용을 감당하지 못하는지 살펴보는 것입니다.

다만 식당 비유를 회계에 그대로 대입하면 안 됩니다. 매출원가에는 변동비뿐 아니라 고정적인 비용도 들어갈 수 있습니다. 또 어떤 비용을 어느 항목에 넣는지는 사업과 회계 정책에 따라 다릅니다. **매출총이익이 양수라는 사실과 고객 한 명이 추가될 때마다 이익이 난다는 말은 다릅니다.**

그래서 실제 기업을 하나 열어보겠습니다. 디자인·협업 소프트웨어 기업 피그마의 2026년 2분기입니다. 아래는 **AI 기능만이 아니라 회사 전체**의 실적입니다.

## 02 피그마는 매출에서 무엇을 빼다가 적자가 됐을까요

<div class="ar2" id="ar2-income" role="group" aria-label="피그마 2026년 2분기 회사 전체 GAAP 손익, 단위 백만 달러">
<p class="eyebrow">FIGURE 01 / FIGMA · 2026년 2분기 · GAAP</p><p class="fig-title">매출원가를 빼면 이익,<br>영업비용까지 빼면 적자.</p>
<p class="small">단위: 백만 달러 · 회사 전체 · 소수 첫째 자리 반올림</p>
<div class="row"><span>매출</span><strong>370.1</strong></div>
<div class="row"><span>차감: 매출원가</span><strong>-60.5</strong></div>
<div class="row result"><span>매출총이익</span><strong>309.6</strong></div>
<div class="row"><span>차감: 영업비용<small>연구개발 167.3 / 판매·마케팅 154.9 / 일반관리 104.7</small></span><strong>-426.9</strong></div>
<div class="row result loss"><span>영업손실</span><strong>-117.3</strong></div>
<p class="note">출처: 피그마 2026년 2분기 공식 실적 발표, 연결손익계산서. 금액은 분기 실적이며 반기 누적이 아닙니다. AI 제품 단독 손익 또는 고객당 원가를 나타내지 않습니다.</p>
</div>

위 숫자에서 확인되는 것은 **매출총이익보다 영업비용이 크다**는 사실입니다. 따라서 회사 전체의 영업적자를 곧바로 “AI 답변을 제공할 때마다 손해”라고 해석할 수는 없습니다. 반대로 매출총이익이 있다고 나머지 비용을 무시해도 되는 것은 아닙니다. [피그마 공식 실적 발표](https://investor.figma.com/news-events/news/news-details/2026/Figma-Announces-Second-Quarter-2026-Financial-Results/default.aspx)

개발자는 제품을 만들고 고쳐야 하고, 영업 조직은 고객을 확보하고 유지해야 합니다. 이런 비용에는 미래 성장을 위한 지출과 현재 사업을 유지하기 위한 지출이 섞여 있습니다. **연구개발비라는 이름만 보고 “언젠가는 없어질 비용”으로 처리하면 흑자 전환을 지나치게 쉽게 보게 됩니다.**

## 03 매출총이익률이 높아도 AI 비용을 다 본 것은 아닙니다

피그마의 전년 동기 대비 매출 증가율은 **48%**, 매출원가 증가율은 **117%였습니다**. 매출총이익률은 회사가 반올림해 발표한 기준으로 **89%에서 84%로 낮아졌습니다**. 분기보고서는 원가 증가의 주된 이유로 AI 및 유료 이용자의 사용 증가와 관련된 인프라·호스팅 비용 증가 **2,710만 달러**를 설명합니다. 이 금액 전부를 순수 추론 비용으로 읽어서는 안 됩니다. [피그마 2분기 보고서: 비용 증감 설명](https://www.sec.gov/Archives/edgar/data/1579878/000162828026053348/fig-20260630.htm)

더 중요한 것은 비용이 들어가는 위치입니다. 같은 보고서에 따르면 **유료 이용자 관련 AI 추론 비용은 매출원가에, 무료 이용자 관련 추론·호스팅 비용은 판매·마케팅비에 포함됩니다**. AI 관련 지출은 연구개발비에도 영향을 줍니다. [분기보고서: 비용 분류](https://www.sec.gov/Archives/edgar/data/1579878/000162828026053348/fig-20260630.htm)

<div class="ar2" role="group" aria-label="피그마 분기보고서에 기재된 AI 관련 비용의 회계 분류">
<p class="eyebrow">FIGURE 02 / 같은 AI 비용도 들어가는 칸이 다릅니다</p><p class="fig-title">무료 고객의 추론 비용은<br>매출원가 밖에도 있습니다.</p>
<div class="steps"><div class="tile"><span class="small">유료 이용자 서비스</span><b>매출원가</b><p>AI 추론을 포함한 인프라·호스팅 비용 등</p></div><div class="tile"><span class="small">무료 이용자 서비스</span><b>판매·마케팅비</b><p>AI 추론·호스팅 및 관련 지원 비용 등</p></div><div class="tile"><span class="small">제품·기술 개발</span><b>연구개발비</b><p>AI 관련 개발 인력·인프라 비용 등</p></div></div>
<p class="note">피그마의 공시상 분류를 간추렸습니다. 항목별 AI 비용 총액은 이 도해로 알 수 없으며, 모든 기업에 동일한 분류를 적용할 수 없습니다.</p>
</div>

이 분류 자체가 이상하다는 뜻은 아닙니다. 무료 체험을 고객 확보 활동으로 볼 수 있기 때문입니다. 다만 투자자의 질문은 여기에서 달라집니다.

**“무료로 써본 사람이 나중에 유료로 전환하고, 그동안 쓴 비용까지 회수할 만큼 오래 남는가?”**

이것이 입증되면 무료 제공은 고객 확보를 위한 투자가 될 수 있습니다. 반대로 무료 사용량만 커지고 유료 전환이나 유지가 따라오지 못한다면 부담이 계속됩니다. 가입자 증가만으로는 둘 중 어느 쪽인지 알 수 없습니다.

따라서 매출총이익률 하나만으로 AI 서비스의 경제성을 판정하면 안 됩니다. 비용 분류와 무료·유료 고객의 연결을 함께 봐야 합니다.

## 04 ‘조정 흑자’라는데, 적자가 아닌 걸까요

피그마의 같은 분기 **GAAP 영업손실은 1억 1,729만 달러**, 회사가 일부 항목을 제외한 **non-GAAP 영업이익은 3,609만 달러**였습니다. 미국 회계기준에 따른 결과와 회사의 조정 지표를 구분해야 합니다.

<div class="ar2" role="group" aria-label="피그마 GAAP 영업손실에서 non-GAAP 영업이익으로의 조정, 백만 달러">
<p class="eyebrow">FIGURE 03 / 손실이 흑자로 바뀌는 계산</p><p class="fig-title">가장 큰 차이는<br>주식보상 비용입니다.</p><p class="small">피그마 2026년 2분기 · 백만 달러 · 반올림</p>
<div class="row loss"><span>GAAP 영업손실</span><strong>-117.3</strong></div>
<div class="row"><span>제외한 주식보상 비용을 더함</span><strong>+147.6</strong></div>
<div class="row"><span>그 밖의 조정 항목을 더함<small>자본화된 주식보상의 상각, 관련 급여세, 인수 무형자산 상각</small></span><strong>+5.8</strong></div>
<div class="row result"><span>non-GAAP 영업이익</span><strong>+36.1</strong></div>
<p class="note">원문 천 달러 단위 검산: -117,289 + 147,554 + 308 + 3,486 + 2,034 = 36,093. 표시값은 반올림해 합계에 차이가 날 수 있습니다. 앞 도해의 비용에 새 비용을 더하는 계산이 아니라, 이미 반영된 비용 일부를 제외하는 조정입니다.</p>
</div>

해당 분기 영업현금흐름도 **6,089만 달러로 양수**였습니다. 회계상 적자와 현금 유출을 같은 뜻으로 쓰면 안 되는 사례입니다. [피그마의 조정 내역·현금흐름표](https://investor.figma.com/news-events/news/news-details/2026/Figma-Announces-Second-Quarter-2026-Financial-Results/default.aspx)

그렇다고 “주식으로 줬으니 공짜”는 아닙니다. 주식보상은 인력을 확보하는 보상의 한 형태이고, 주식 발행에 따른 기존 주주의 지분 희석도 살펴야 합니다. 반복되는 보상을 매번 제외한 흑자와, 그 보상까지 감당하는 흑자는 주주에게 같지 않습니다.

이 대목에서는 두 숫자를 나란히 두는 편이 낫습니다. GAAP 손익으로 전체 비용을 확인하고, 조정 지표로 회사가 어떤 비용을 덜어내 보여주는지 확인합니다. **흑자라는 단어보다, 흑자를 만들기 위해 무엇을 제외했는지가 먼저입니다.**

## 05 비용을 낮추고 가격을 올리면 해결될까요

회사에 방법이 없는 것은 아닙니다. 같은 일을 더 적은 비용으로 처리하거나, 비용이 많이 드는 작업에 추가 요금을 받거나, 고객이 더 지불할 만큼 제품의 가치를 높일 수 있습니다. 다만 방법을 발표하는 것과 실제 이익을 내는 것은 별개입니다.

듀오링고는 2026년 2분기 매출총이익률이 **72.6%로**, 기존 예상인 **약 71.0%를 웃돈 이유**로 AI 비용 효율화와 AI 기능 확대 속도 조절을 함께 설명했습니다. “모델이 싸져서 좋아졌다” 하나로 요약하면, 얼마나 많은 기능을 얼마나 빨리 제공했는지라는 조건을 놓칩니다. 이 수치 역시 AI 기능만이 아닌 회사 전체 기준입니다. [듀오링고 주주서한](https://www.sec.gov/Archives/edgar/data/1562088/000162828026053299/q2fy26duolingo6-30x26share.htm)

가격 쪽에서는 GitHub의 Copilot 사례가 있습니다. 회사는 **2026년 4월 27일** 사용량 기반 과금 전환을 발표하며, 짧은 질문과 길게 이어지는 에이전트 작업을 요청 횟수만으로 다루기 어렵다고 설명했습니다. 에이전트는 여러 단계의 작업을 이어가는 AI입니다. 사용자에게는 요청 한 번이어도 내부 모델 호출은 여러 번일 수 있습니다. [GitHub의 전환 배경 설명](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

이런 변화는 **비용이 늘어나는 만큼 매출도 따라오게 하려는 시도**로 읽을 수 있습니다. 하지만 해당 발표가 Copilot의 흑자를 입증하지는 않습니다. 추가 요금을 내면서도 고객이 계속 사용하는지까지 봐야 합니다.

비용 절감에도 같은 검증이 필요합니다. 저렴한 모델로 바꿨지만 오류와 재시도가 늘면 절감 효과가 줄어듭니다. 단가가 낮아졌어도 처리량이 더 빠르게 늘면 총비용은 커질 수 있습니다. 투자자가 확인할 것은 “AI가 싸졌다”가 아니라 **같은 품질의 서비스를 제공하고, 고객에게 돈을 받아, 최종적으로 더 남겼는가**입니다.

## 06 무엇이 보여야 ‘성장통’이라는 설명을 믿을 수 있을까요

아래는 특정 회사의 미래를 판정하는 점수표가 아닙니다. 다음 실적에서 경영진의 설명을 확인하기 위한 질문입니다.

| 회사의 설명 | 다음에 확인할 증거 | 경계할 경우 |
|---|---|---|
| 지금은 고객을 확보하는 중입니다 | 무료 고객의 유료 전환, 기존 유료 고객의 갱신·추가 구매 | 사용량만 늘고 결제·유지가 따라오지 않음 |
| AI 비용을 효율화하고 있습니다 | 비슷한 품질·이용 조건에서 비용 부담이 줄고 이익률이 개선되는지 | 제공 범위 축소를 기술 효율 향상으로만 설명 |
| 먼저 개발하고 나중에 회수합니다 | 새 제품 매출·매출총이익이 늘어 영업비용을 감당하는 방향인지 | 개발비 증가를 매번 미래 매출로 정당화 |
| 가격을 원가에 맞추고 있습니다 | 추가 과금 이후 고객 유지와 매출·이익 변화 | 요금 인상 뒤 해지·할인이 늘어남 |
| 조정 기준으로는 이미 흑자입니다 | 제외 항목의 반복성, 주식 수 변화, 현금흐름 | 반복 비용을 빼야만 계속 흑자가 됨 |

한 분기로 끝낼 질문은 아닙니다. 성장 과정에서는 개발비와 매출이 같은 분기에 움직이지 않을 수 있습니다. 그렇다고 검증을 무기한 미뤄도 된다는 뜻은 아닙니다. **어떤 비용을 먼저 썼고, 어떤 매출로 회수할 것이며, 어느 지표로 진행 상황을 확인할지**가 연결되어야 합니다.

여기에 자금 사정도 더해야 합니다. 회수 가능성이 있는 사업이라도 그때까지 버틸 현금이 부족하면 추가 조달이 필요합니다. 영업현금흐름과 설비투자, 부채 만기 등을 따로 확인해야 하는 이유입니다. 영업적자 금액을 그대로 현금 소진액으로 놓고 버틸 기간을 계산하지는 마세요.

그리고 공개 자료가 부족한 기업에는 결론을 억지로 채워 넣지 않는 것이 좋겠습니다. 매출 증가 보도나 이용자 수만으로는 추론 비용, 연구개발비, 회사 전체 손익을 복원할 수 없습니다. **아직 확인할 수 없다는 판단도 투자 정보를 읽는 결과입니다.**

## 정리

AI 기업의 적자가 성장통인지 사업의 한계인지는, 적자라는 숫자 하나로 정해지지 않습니다.

- **손실이 발생하는 위치부터 봅니다.** 매출원가와 나머지 영업비용을 나누되, 매출총이익을 고객당 이익으로 오해하지 않습니다.
- **비용의 분류와 조정 내역을 읽습니다.** 무료 이용자 비용이 매출원가 밖에 있을 수 있고, 조정 흑자는 일부 비용을 제외한 결과입니다.
- **성장통이라는 설명은 이후 실적으로 확인합니다.** 고객이 남고, 비용을 회수하고, 전체 비용과 현금 지출까지 감당하는 방향으로 가는지 봅니다.

AI를 많이 쓴다는 사실은 수요의 단서입니다. **그 수요를 이익으로 바꾸는 능력은 따로 확인해야 합니다.** 다음 편에서는 클라우드 회사의 매출 증가 중 어디까지를 AI의 성과로 읽을 수 있는지 살펴보겠습니다.

---

자료 확인일: **2026년 9월 30일**. 기업 수치는 별도 표시가 없는 한 2026년 2분기(4~6월) 회사 전체 실적입니다. 달러 금액은 원화로 환산하지 않았습니다. 비용 분류와 조정 지표의 정의는 회사마다 다르며, 이 글은 특정 AI 제품의 비공개 원가나 손익을 추정하지 않습니다.

> ⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
