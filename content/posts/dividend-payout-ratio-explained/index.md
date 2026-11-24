---
title: "배당성향이란? 배당금이 늘어도 낮아지는 이유"
description: "배당성향 계산법과 배당수익률의 차이를 설명합니다. 삼성전자 2026년 3분기 30조 원 배당 공시를 읽고, 2024·2025년 실제 수치로 배당금이 늘어도 배당성향은 낮아질 수 있는 이유를 알아봅니다."
slug: "dividend-payout-ratio-explained"
date: 2026-11-24T00:00:00+09:00
draft: false
image: "dividend-payout-cover.jpg"
categories: ["AI 투자"]
tags: ["배당성향", "배당수익률", "삼성전자 배당", "현금배당", "주주환원"]
---

<style>
.article-content { container-type: inline-size; }
.dp-figure {
  --paper: #f7f4ec;
  --ink: #193e37;
  --muted: #47665e;
  --card: #fffef9;
  --line: #cad7cc;
  --green: #166f63;
  background: var(--paper);
  color: var(--ink);
  border: 1px solid var(--line);
  border-radius: 14px;
  margin: 30px 0;
  padding: 24px;
  line-height: 1.55;
  word-break: keep-all;
}
.dp-figure * { box-sizing: border-box; }
.dp-figure p { margin: 0; }
.dp-figure .dp-kicker { color: var(--muted); font-size: 13px; font-weight: 700; }
.dp-figure .dp-title { margin: 6px 0 18px; font-size: 24px; font-weight: 800; line-height: 1.35; }
.dp-figure .dp-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.dp-figure .dp-card { padding: 16px; border: 1px solid var(--line); border-top: 4px solid var(--green); border-radius: 10px; background: var(--card); }
.dp-figure .dp-label { color: var(--muted); font-size: 14px; font-weight: 700; }
.dp-figure .dp-value { color: var(--green); font-size: 30px; font-weight: 800; margin: 7px 0; }
.dp-figure .dp-detail { font-size: 14px; }
.dp-figure .dp-note { color: var(--muted); font-size: 13px; margin-top: 14px; }
[data-scheme=dark] .dp-figure {
  --paper: #233c36; --ink: #f0f5ed; --muted: #c3d5cb; --card: #2b453d;
  --line: #587565; --green: #a1e4d1;
}
@container (max-width: 460px) {
  .dp-figure { padding: 17px; }
  .dp-figure .dp-grid { grid-template-columns: 1fr; }
  .dp-figure .dp-title { font-size: 21px; }
}
</style>

동업하는 가게가 처음엔 1,000만 원을 벌어 주인들에게 200만 원을 나눠줬습니다. 다음 해에는 2,000만 원을 벌어 300만 원을 나눠줍니다. 받은 돈은 100만 원 늘었지만, 이익에서 나눠준 몫은 20%에서 15%로 줄었습니다. 이 몫이 회사 공시에서 보는 **배당성향**입니다.

삼성전자는 2026년 3분기 현금배당으로 **약 30조 원**을 결정했습니다. 보통주와 우선주 모두 주당 4,601원이고, 공시상 지급 예정일은 11월 27일입니다. 큰 금액이라 배당 자료를 찾아봤는데, 바로 전 두 해에는 배당액과 배당성향이 서로 다른 방향으로 움직였습니다. 금액과 비율을 구분하면 그 이유가 보입니다. [삼성전자 2026년 3분기 현금배당 결정](https://www.samsung.com/sec/ir/reports-disclosures/public-disclosure/4083/)

## 배당성향 계산법

**현금배당성향 = 현금배당총액 ÷ 당기순이익 × 100**

배당성향은 그 사업연도의 순이익과 그해에 귀속되는 현금배당을 비교합니다. 위 가게처럼 이익이 1,000만 원이고 배당이 200만 원이면 배당성향은 20%입니다. 다음 해에 배당액이 늘어도 이익이 더 빠르게 늘면 배당성향은 낮아집니다.

<div class="dp-figure" role="figure" aria-label="가상 가게의 배당액이 200만 원에서 300만 원으로 늘지만, 순이익이 1천만 원에서 2천만 원으로 늘어 배당성향은 20퍼센트에서 15퍼센트로 내려갑니다.">
  <p class="dp-kicker">가상 가게의 두 해</p>
  <p class="dp-title">나눠 준 돈은 늘고, 나눠 준 비율은 줄었습니다</p>
  <div class="dp-grid">
    <div class="dp-card">
      <p class="dp-label">첫해 배당성향</p>
      <p class="dp-value">20%</p>
      <p class="dp-detail">배당 200만 원 ÷ 순이익 1,000만 원</p>
    </div>
    <div class="dp-card">
      <p class="dp-label">다음 해 배당성향</p>
      <p class="dp-value">15%</p>
      <p class="dp-detail">배당 300만 원 ÷ 순이익 2,000만 원</p>
    </div>
  </div>
</div>

순이익이 아주 작으면 배당금이 비슷해도 비율은 크게 뜁니다. 이익이 0이면 나눗셈을 할 수 없고, 적자라면 계산상 음수가 나와도 평소의 배당성향과 같은 방식으로 해석하기 어렵습니다. 그래서 배당성향을 보면 배당총액과 순이익을 먼저 펼쳐봅니다.

## 배당성향과 배당수익률의 차이

둘 다 퍼센트라 헷갈리는데, 무엇으로 나누는지부터 보면 쉽습니다.

| 궁금한 숫자 | 계산에 쓰는 값 | 이렇게 읽습니다 |
|---|---|---|
| 배당성향 | 현금배당총액 ÷ 당기순이익 | 회사 이익에 비해 얼마나 나눠줬는가 |
| 배당수익률 | 주당배당금 ÷ 기준 주가 | 주식 한 주 가격에 비해 배당금이 얼마나 되는가 |

두 비율 모두 100을 곱해 퍼센트로 표시합니다. 예를 들어 연간 주당배당금이 1,000원으로 같은데 주가가 5만 원에서 4만 원으로 내리면, 배당수익률은 2%에서 2.5%로 올라갑니다. 배당금 자체는 그대로입니다. 화면에 나온 수익률을 비교할 때는 어느 날짜의 주가를 썼는지, 한 분기 배당인지 지난 1년 배당인지도 함께 확인합니다.

## 삼성전자 배당금은 13.2% 늘었는데 배당성향은 내려갔습니다

삼성전자 투자자 정보 페이지에서 ‘연도별 배당 내역’을 펼쳐봤습니다. 여기서 순이익은 연결 당기순이익 가운데 **지배기업 소유주에게 귀속되는 몫**을 씁니다. 배당총액은 보통주와 우선주를 합친 값입니다. 앱에서 직접 계산한 비율과 회사 발표값이 다르면, 우선 이 두 범위를 맞춰보면 됩니다. [삼성전자 연도별 배당 내역](https://www.samsung.com/sec/ir/stock-information/shareholder-return/)

| 사업연도 | 현금배당총액 | 지배기업 소유주 귀속 순이익 | 배당성향 |
|---|---:|---:|---:|
| 2023년 | 9.81조 원 | 14.47조 원 | 67.8% |
| 2024년 | 9.81조 원 | 33.62조 원 | 29.2% |
| 2025년 | 11.11조 원 | 44.26조 원 | 25.1% |

2023년과 2024년에는 배당총액을 조 원 단위로 반올림하면 같습니다. 그런데 순이익이 커지면서 배당성향은 67.8%에서 29.2%로 내려갔습니다. 2025년에는 추가 배당을 포함해 배당액을 전년보다 13.2% 늘렸지만 순이익은 약 31.6% 늘었습니다. 나누는 쪽이 더 많이 커져 배당성향이 25.1%로 낮아졌습니다. [삼성전자 주주환원 내역](https://www.samsung.com/sec/ir/stock-information/shareholder-return/) · [기업가치 제고 계획 공시](https://www.samsung.com/sec/ir/reports-disclosures/public-disclosure/3764/)

<div class="dp-figure" role="figure" aria-label="삼성전자 2024년 배당총액은 9.81조 원, 배당성향은 29.2퍼센트입니다. 2025년 배당총액은 11.11조 원으로 늘었고 배당성향은 25.1퍼센트로 줄었습니다.">
  <p class="dp-kicker">삼성전자 · 연간 현금배당</p>
  <p class="dp-title">2025년에는 순이익이 배당금보다 빠르게 늘었습니다</p>
  <div class="dp-grid">
    <div class="dp-card">
      <p class="dp-label">2024년 배당성향</p>
      <p class="dp-value">29.2%</p>
      <p class="dp-detail">배당 9.81조 원 ÷ 순이익 33.62조 원</p>
    </div>
    <div class="dp-card">
      <p class="dp-label">2025년 배당성향</p>
      <p class="dp-value">25.1%</p>
      <p class="dp-detail">배당 11.11조 원 ÷ 순이익 44.26조 원</p>
    </div>
  </div>
  <p class="dp-note">금액은 반올림했습니다. 배당성향은 회사가 공시한 값입니다.</p>
</div>

## 삼성전자 30조 원 배당 공시에서 확인할 것

삼성전자의 2026년 3분기 약 30조 원은 공시에서 **한 분기의 현금배당총액**으로 확인할 수 있습니다. 회사는 정규 분기배당을 포함한 금액이라고 설명했습니다. 주당 4,601원은 이번 분기 공시값이고, 앞으로의 정규 분기배당을 계산할 때는 회사의 배당 정책과 후속 공시를 따로 확인해야 합니다. 2026년 연간 배당성향을 계산하려면 2026년에 귀속되는 연간 배당과 연간 순이익이 모두 필요합니다. [삼성전자 주주환원 공시](https://www.samsung.com/sec/ir/reports-disclosures/public-disclosure/4047/) · [3분기 배당 결정](https://www.samsung.com/sec/ir/reports-disclosures/public-disclosure/4083/)

배당받을 주주를 정하는 **배당기준일은 9월 30일**, 돈을 지급할 **예정일은 11월 27일**입니다. 지급을 앞두고 소식을 접했다면, 먼저 공시에서 어느 시점에 배당받을 주주를 정했는지 보면 됩니다. [삼성전자 3분기 배당 결정 공시](https://www.samsung.com/sec/ir/reports-disclosures/public-disclosure/4083/)

## 정리

배당성향을 보면 저는 세 가지를 같이 확인하려고 합니다.

1. **배당총액과 순이익 중 어느 쪽이 변했는지** 봅니다. 배당금이 올라가도 순이익이 더 빠르게 늘면 배당성향은 내려갑니다.
2. **정기적으로 지급하는 배당과 추가 배당을 구분합니다.** 주당배당금과 배당수익률을 비교할 때는 기간과 기준 주가도 확인합니다.
3. **배당을 지급할 현금이 사업에서 얼마나 나오는지** 봅니다. [잉여현금흐름](/p/free-cash-flow-explained/)과 [순차입금](/p/net-debt-explained/)을 함께 보면 설비투자와 상환 부담까지 이어서 살펴볼 수 있습니다.

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
