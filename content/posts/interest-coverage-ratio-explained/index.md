---
title: "이자보상배율이란? 계산법과 1배의 의미"
description: "이자보상배율의 뜻과 계산법, 1배 미만의 의미를 설명합니다. 삼성전자 연결재무제표에서 영업이익과 이자비용을 찾고, 이자보상배율과 원금 상환 능력을 함께 읽는 법을 알아봅니다."
slug: "interest-coverage-ratio-explained"
date: 2026-11-23T00:00:00+09:00
draft: false
image: "interest-coverage-cover.jpg"
categories: ["AI 투자"]
tags: ["이자보상배율", "이자보상비율", "이자비용", "영업이익", "재무제표 보는 법"]
---

<style>
.article-content { container-type: inline-size; }
.ic-intro { font-size: 13px; opacity: .76; }
.ic-figure {
  --paper: #f7f4ec;
  --ink: #193e37;
  --muted: #48675e;
  --card: #fffef9;
  --line: #cad7cc;
  --green: #166f63;
  --rust: #994632;
  color: var(--ink);
  background: var(--paper);
  border: 1px solid var(--line);
  border-radius: 14px;
  margin: 32px 0;
  padding: 25px;
  line-height: 1.55;
  word-break: keep-all;
}
.ic-figure * { box-sizing: border-box; }
.ic-figure p { margin: 0; }
.ic-figure .ic-caption { color: var(--muted); font-size: 13px; font-weight: 700; }
.ic-figure .ic-title { font-size: 25px; font-weight: 800; line-height: 1.35; margin: 6px 0 18px; }
.ic-figure .ic-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.ic-figure .ic-pair { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.ic-figure .ic-card {
  background: var(--card);
  border: 1px solid var(--line);
  border-top: 4px solid var(--green);
  border-radius: 9px;
  padding: 15px;
}
.ic-figure .ic-short { border-top-color: var(--rust); }
.ic-figure .ic-label { font-size: 14px; font-weight: 700; }
.ic-figure .ic-value { color: var(--green); font-size: 29px; font-weight: 850; margin: 7px 0; }
.ic-figure .ic-short .ic-value { color: var(--rust); }
.ic-figure .ic-detail { color: var(--muted); font-size: 14px; }
.ic-figure .ic-note { color: var(--muted); font-size: 13px; margin-top: 14px; }
[data-scheme=dark] .ic-figure {
  --paper: #233c36; --ink: #f0f5ed; --muted: #bdd4c8; --card: #2b453d;
  --line: #587565; --green: #a1e4d1; --rust: #ffc2a9;
}
@container (max-width: 480px) {
  .ic-figure { padding: 17px; }
  .ic-figure .ic-grid { grid-template-columns: 1fr; }
  .ic-figure .ic-title { font-size: 21px; }
}
</style>

<p class="ic-intro">회사의 빚 읽는 법 · 세 번째 이야기</p>

한 가게의 올해 영업이익은 2천만 원입니다. 이자비용이 1천만 원이라면 영업이익은 이자의 두 배입니다. 그런데 내년에 장사가 부진해 영업이익이 800만 원으로 줄고 이자는 그대로라면 어떨까요? 대출 잔액이 같아도, 이번에는 영업이익이 이자비용보다 200만 원 적습니다.

**이자보상배율은 같은 기간의 영업이익을 이자비용으로 나눈 값**입니다. 앞에서 살펴본 부채비율과 순차입금은 특정 날짜의 재무상태를 보여줍니다. 이자보상배율을 계산할 때는 한 해나 한 분기 동안 쌓인 이익과 이자비용을 비교합니다. [한국은행의 이자보상배율 설명](https://www.bok.or.kr/portal/bbs/B0000217/view.do?menuNo=200144&nttId=10092841)

## 이자보상배율 계산법과 1배의 의미

**이자보상배율 = 영업이익 ÷ 이자비용**

영업이익 2천만 원을 이자비용 1천만 원으로 나누면 2배입니다. 자료에 따라 ‘이자보상비율’이라는 이름으로 100을 곱해 표시하기도 합니다. 같은 산식이라면 2배는 200%, 1배는 100%입니다.

<div class="ic-figure" role="figure" aria-label="이자비용 1천만 원일 때 영업이익 800만 원은 0.8배, 1천만 원은 1배, 2천만 원은 2배입니다.">
  <p class="ic-caption">이자비용이 연 1천만 원인 가상 가게</p>
  <p class="ic-title">영업이익이 1천만 원이면 이자와 같은 크기입니다</p>
  <div class="ic-grid">
    <div class="ic-card ic-short">
      <p class="ic-label">영업이익 800만 원</p>
      <p class="ic-value">0.8배</p>
      <p class="ic-detail">이자보다 200만 원 적음</p>
    </div>
    <div class="ic-card">
      <p class="ic-label">영업이익 1천만 원</p>
      <p class="ic-value">1배</p>
      <p class="ic-detail">이자와 같은 금액</p>
    </div>
    <div class="ic-card">
      <p class="ic-label">영업이익 2천만 원</p>
      <p class="ic-value">2배</p>
      <p class="ic-detail">이자보다 1천만 원 많음</p>
    </div>
  </div>
  <p class="ic-note">같은 기간의 손익 항목을 비교했습니다. 현금 유입이나 원금 상환액은 별도로 봅니다.</p>
</div>

1배 아래라면 그 기간의 영업이익이 이자비용을 밑돌았다는 뜻입니다. 기존 현금을 쓰거나 자산을 팔아 이자를 낼 수도 있으므로 실제 연체 여부는 현금 사정과 지급 일정을 함께 봐야 합니다. 반대로 1배를 조금 넘던 회사는 영업이익이 줄거나 이자비용이 오르면 1배 아래로 내려갈 수 있습니다.

영업손실이면 이자비용이 있는 경우 배율도 음수가 됩니다. 이자비용이 0이면 계산할 수 없고, 이자비용이 아주 작으면 배율이 크게 나올 수 있습니다. 그래서 배율 옆에 영업이익과 이자비용 원래 금액을 적어 두는 편이 좋습니다.

## 삼성전자 공시에서 이자비용 찾기

지난 두 글에서 본 삼성전자 자료를 다시 펼쳤습니다. 연결손익계산서에서 **영업이익**을 찾고 아래쪽의 ‘금융비용’을 따라가니 주석 24가 나옵니다. 이 주석에서 이자비용만 골라 같은 해의 영업이익과 맞춰봤습니다. [삼성전자 연결손익계산서](https://images.samsung.com/kdp/ir/financial-info/2025/2025_con_quarter04_all.pdf#page=12) · [주석 24 금융수익 및 금융비용](https://images.samsung.com/kdp/ir/financial-info/2025/2025_con_quarter04_all.pdf#page=96)

| 연결 기준 | 2024년 | 2025년 |
|---|---:|---:|
| 영업이익(백만 원) | 32,725,961 | 43,601,051 |
| 주석의 이자비용(백만 원) | 903,918 | 605,783 |
| 영업이익 ÷ 이자비용 | **36.2배** | **72.0배** |

2025년에는 영업이익이 증가하고 주석에 잡힌 이자비용이 감소해 배율이 높아졌습니다. 2편에서 본 연말 차입금은 같은 해에 늘었습니다. 연말 차입금은 결산일의 잔액이고, 이자비용은 한 해 동안 비용으로 인식한 금액입니다. 둘이 다른 방향으로 움직였다면 평균 차입 잔액, 금리, 비용으로 잡힌 범위를 살펴볼 차례입니다.

제가 계산할 때 구분한 항목이 세 가지 있습니다.

- **금융비용 합계.** 2025년 금융비용 11,733,764백만 원에는 외환차이와 파생상품 관련 손실도 들어 있습니다. 이 글의 산식에는 주석의 이자비용 605,783백만 원을 넣었습니다.
- **이자의 지급.** 현금흐름표의 ‘이자의 지급’은 실제 현금이 나간 금액입니다. 비용으로 인식한 시점과 돈을 낸 시점이 다를 수 있습니다. [삼성전자 연결현금흐름표](https://images.samsung.com/kdp/ir/financial-info/2025/2025_con_quarter04_all.pdf#page=15)
- **자산 취득원가에 포함한 차입원가.** 공장처럼 완성까지 시간이 걸리는 자산에 직접 관련된 차입원가는 기준에 따라 취득원가에 포함될 수 있습니다. 삼성전자도 이 금액을 유형자산 주석에 따로 공개합니다. 회사끼리 비교할 때는 이자비용의 범위를 맞춰야 배율 차이를 해석할 수 있습니다. [삼성전자 주석 10 유형자산](https://images.samsung.com/kdp/ir/financial-info/2025/2025_con_quarter04_all.pdf#page=71) · [IFRS 재단의 차입원가 설명](https://www.ifrs.org/issued-standards/list-of-standards/ias-23-borrowing-costs/)

## 이자보상배율이 2배인데 원금 상환이 어려울 수도 있을까요?

처음 가게로 돌아가 보겠습니다. 연간 영업이익은 2천만 원, 이자비용은 1천만 원입니다. 이제 다음 달에 대출 원금 5천만 원을 갚아야 하고, 지금 쓸 수 있는 현금은 3천만 원이라고 해보겠습니다. 만기까지 추가로 들어올 돈이 없다면 원금만 놓고도 2천만 원이 모자랍니다.

<div class="ic-figure" role="figure" aria-label="가상 가게의 연간 영업이익 2천만 원과 이자비용 1천만 원으로 계산한 배율은 2배입니다. 다음 달 원금 5천만 원을 앞두고 사용 가능 현금이 3천만 원이라면 추가 유입이 없을 때 2천만 원이 부족합니다.">
  <p class="ic-caption">가상 가게 · 연간 손익과 다음 달 현금</p>
  <p class="ic-title">이자와 원금은 서로 다른 숫자로 확인합니다</p>
  <div class="ic-grid ic-pair">
    <div class="ic-card">
      <p class="ic-label">연간 이자보상배율</p>
      <p class="ic-value">2배</p>
      <p class="ic-detail">영업이익 2천만 원 ÷ 이자비용 1천만 원</p>
    </div>
    <div class="ic-card ic-short">
      <p class="ic-label">다음 달 원금에 부족한 금액</p>
      <p class="ic-value">2천만 원</p>
      <p class="ic-detail">만기 원금 5천만 원 − 사용 가능 현금 3천만 원</p>
    </div>
  </div>
  <p class="ic-note">만기 전 추가 현금 유입이나 대출 연장이 없다고 가정했습니다.</p>
</div>

원금의 만기는 차입금이나 유동성 위험 관련 주석에서 확인합니다. 그 시점까지 거래처에서 받을 돈이 들어오는지, 급여와 설비 대금 등 먼저 나갈 돈은 얼마인지도 봐야 합니다. 연간 [영업현금흐름](/p/operating-cash-flow-explained/)은 사업에서 현금을 얼마나 만들었는지 보는 출발점이고, 당장 돌아오는 만기에는 실제 입출금 일정이 필요합니다.

## 정리

회사 하나를 볼 때 저는 세 지표를 아래 순서로 확인하려고 합니다. 숫자가 변했다면 먼저 그 숫자를 만든 항목들부터 다시 펼쳐봅니다.

| 확인할 지표 | 재무제표를 읽으면서 던질 질문 |
|---|---|
| [부채비율](/p/debt-ratio-explained/) | 자기자본에 비해 부채가 얼마나 큰가요? 부채와 자본 중 어느 쪽이 변했나요? |
| [순차입금](/p/net-debt-explained/) | 차입금에서 현금을 빼면 얼마가 남나요? 그 현금을 쓸 수 있는 조건은 무엇인가요? |
| 이자보상배율 | 같은 기간의 영업이익이 이자비용을 몇 배 감당하나요? 이익과 이자비용 중 어느 쪽이 변했나요? |

마지막으로 **가까운 만기에 갚을 원금과 그때 쓸 수 있는 현금**을 확인합니다. 삼성전자 사례처럼 차입금 잔액이 늘면서 이자보상배율도 올라갈 수 있어서, 두 숫자를 읽고 나면 회사에 물어볼 질문이 서로 달라집니다.

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
