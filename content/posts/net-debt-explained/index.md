---
title: "순차입금이란? 차입금과 현금을 함께 보는 법"
description: "순차입금과 순현금의 뜻, 계산법, 순차입금이 마이너스일 때의 의미를 알아봅니다. 삼성전자 2025년 연결재무제표와 실적 발표 자료를 비교해 현금의 범위에 따라 계산값이 달라지는 이유를 설명합니다."
slug: "net-debt-explained"
date: 2026-11-20T00:00:00+09:00
draft: false
image: "net-debt-cover.jpg"
categories: ["AI 투자"]
tags: ["순차입금", "순현금", "차입금", "재무제표 보는 법", "재무 건전성"]
---

<style>
.article-content{container-type:inline-size}
.nd-intro{font-size:13px;opacity:.75}
.nd-figure{
  --paper:#f7f4ec;
  --ink:#193e37;
  --muted:#516b65;
  --card:#fffef9;
  --border:#cbd7cc;
  --green:#16766b;
  --ochre:#935039;
  background:var(--paper);color:var(--ink);border:1px solid var(--border);
  border-radius:14px;margin:32px 0;padding:26px;line-height:1.6;word-break:keep-all;
}
.nd-figure *{box-sizing:border-box}
.nd-figure p{margin:0}
.nd-figure .nd-kicker{font-size:13px;font-weight:700;color:var(--muted);margin-bottom:7px}
.nd-figure .nd-title{font-size:25px;line-height:1.35;font-weight:800;margin-bottom:20px}
.nd-figure .nd-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}
.nd-figure .nd-card{
  background:var(--card);border:1px solid var(--border);border-radius:10px;
  border-top:4px solid var(--green);padding:17px;
}
.nd-figure .nd-warm{border-top-color:var(--ochre)}
.nd-figure .nd-label{font-size:15px;font-weight:700}
.nd-figure .nd-value{font-size:clamp(25px,5cqi,34px);font-weight:800;color:var(--green);margin:9px 0}
.nd-figure .nd-warm .nd-value{color:var(--ochre)}
.nd-figure .nd-math{font-size:15px;color:var(--muted)}
.nd-figure .nd-track{
  height:10px;margin:15px 0;background:var(--border);border-radius:10px;overflow:hidden;
}
.nd-figure .nd-track span{display:block;height:100%;background:var(--green)}
.nd-figure .nd-note{margin-top:14px;font-size:13px;color:var(--muted)}
[data-scheme=dark] .nd-figure{
  --paper:#233c36;--ink:#f0f5ed;--muted:#c3d5cb;--card:#2b453d;
  --border:#587565;--green:#a1e4d1;--ochre:#ffc2a9;
}
@container (max-width:480px){
  .nd-figure{padding:18px}
  .nd-figure .nd-grid{grid-template-columns:1fr}
  .nd-figure .nd-title{font-size:22px}
}
</style>

<p class="nd-intro">회사의 빚 읽는 법 · 두 번째 이야기</p>

가게 두 곳이 은행에서 똑같이 1억 원을 빌렸습니다. 한 곳은 통장에 2천만 원, 다른 곳은 1억 2천만 원이 있습니다. 대출 잔액만 보면 두 가게가 같은데, 당장 갚는다고 생각해 보면 한 가게는 돈이 모자라고 다른 가게는 갚고도 돈이 남습니다.

[지난 글](/p/debt-ratio-explained/)에서는 부채가 자기자본에 비해 얼마나 큰지 봤습니다. 이번에는 빌린 돈과 보유한 현금을 한 줄에 놓고 비교해 보겠습니다. 삼성전자 자료를 대조하다 보면, 회사가 말하는 ‘현금’이 재무상태표의 현금 한 줄보다 넓을 때도 있다는 걸 확인할 수 있습니다.

## 순차입금의 뜻과 계산법

<strong>순차입금은 빌린 돈의 잔액에서 계산에 포함한 현금성 자산을 뺀 금액</strong>입니다. 본문에서 총차입금은 은행 대출과 회사채 등 돈을 조달하면서 생긴 빚을 합한 금액으로 씁니다. 공시나 데이터 서비스에 따라 리스부채를 포함하기도 합니다.

**순차입금 = 총차입금 − 계산에 포함한 현금성 자산**

순차입금이 양수이면 차입금이 현금성 자산보다 많습니다. 음수이면 현금성 자산이 더 많고, 그 차이를 양수로 표현한 것이 순현금입니다. 같은 항목을 썼다면 순차입금 −2천만 원은 순현금 2천만 원과 같은 뜻입니다.

<div class="nd-figure" role="figure" aria-label="두 가게의 차입금은 1억 원으로 같습니다. A는 현금 2천만 원으로 순차입금 8천만 원, B는 현금 1억 2천만 원으로 순현금 2천만 원입니다.">
  <p class="nd-kicker">차입금이 1억 원으로 같은 가상 가게</p>
  <p class="nd-title">현금을 빼보니 한쪽은 돈이 모자라고, 한쪽은 남습니다</p>
  <div class="nd-grid">
    <div class="nd-card nd-warm">
      <p class="nd-label">가게 A · 순차입금</p>
      <p class="nd-value">8천만 원</p>
      <p class="nd-math">차입금 1억 원 − 현금 2천만 원</p>
    </div>
    <div class="nd-card">
      <p class="nd-label">가게 B · 순현금</p>
      <p class="nd-value">2천만 원</p>
      <p class="nd-math">현금 1억 2천만 원 − 차입금 1억 원</p>
    </div>
  </div>
  <p class="nd-note">가게 B에도 대출 1억 원이 남아 있습니다. 현금과 차입금을 계산상 비교한 예시입니다.</p>
</div>

## 부채총계, 차입금, 순차입금의 차이

세 숫자는 기업을 볼 때 서로 다른 질문에 답합니다.

| 항목 | 무엇을 합하거나 빼나요? | 어떤 질문에 답하나요? |
|---|---|---|
| 부채총계 | 차입금, 매입채무, 미지급비용 등 재무상태표의 모든 부채 | 회사가 이행해야 할 의무는 얼마나 큰가요? |
| 총차입금 | 단기·장기차입금, 사채 등. 리스부채 포함 여부는 계산 기준에 따름 | 빌린 돈을 중심으로 보면 부담이 얼마나 되나요? |
| 순차입금 | 총차입금에서 정해진 범위의 현금성 자산을 차감 | 보유 현금을 감안하면 차입 부담은 얼마나 남나요? |

순차입금을 직접 계산할 때는 유동부채와 비유동부채를 둘 다 펼쳐봅니다. 장기차입금이나 회사채 가운데 1년 안에 갚아야 할 부분은 유동성장기부채 등으로 따로 표시될 수 있습니다. 주석에서 이 부분까지 찾고, 다른 항목에 이미 들어 있는 리스부채는 한 번만 셉니다.

현금 쪽에서는 우선 **현금및현금성자산** 항목을 찾습니다. 현금성자산은 현금으로 쉽게 바꿀 수 있고 가치 변동 위험이 작은 단기 투자자산입니다. 순차입금 계산에 단기금융상품도 넣을지는 만기와 사용 조건, 비교하려는 자료의 기준을 보고 정합니다. [IFRS 재단의 IAS 7 설명](https://www.ifrs.org/issued-standards/list-of-standards/ias-7-statement-of-cash-flows/)

## 삼성전자 순현금은 왜 32.62조 원과 100.61조 원으로 나올까요?

1편과 같은 **2025년 말 삼성전자 연결재무제표**를 펼쳐봤습니다. 부채총계는 130.62조 원이지만, 단기차입금·유동성장기부채·사채·장기차입금을 합하면 25.24조 원입니다. 이 합계에는 유동성장기부채와 장기차입금에 들어 있는 리스부채가 포함돼 있습니다. [삼성전자 연결재무상태표 부채](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=7) · [리스 회계정책](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=36) · [차입금 변동 주석](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=77)

| 2025년 말 차입금에 넣은 항목 | 금액(백만 원) |
|---|---:|
| 단기차입금 | 17,574,980 |
| 유동성장기부채 | 1,177,508 |
| 사채 | 7,134 |
| 장기차입금 | 6,479,517 |
| 합계 | **25,239,139** |

이 차입금에 현금의 범위만 두 가지로 바꿔 적용해 보겠습니다.

<div class="nd-figure" role="figure" aria-label="차입금 25.24조 원을 고정하면 현금및현금성자산만 쓴 순현금은 32.62조 원, 단기금융상품 등을 포함한 회사 발표 순현금은 100.61조 원입니다. 막대는 순현금 금액을 같은 축으로 비교합니다.">
  <p class="nd-kicker">삼성전자 · 2025년 말 연결 · 차입금 25.24조 원</p>
  <p class="nd-title">현금의 범위를 넓히면 순현금도 커집니다</p>
  <div class="nd-grid">
    <div class="nd-card">
      <p class="nd-label">현금및현금성자산만 사용</p>
      <p class="nd-value">32.62조 원</p>
      <div class="nd-track" aria-hidden="true"><span style="width:32.42%"></span></div>
      <p class="nd-math">57.86 − 25.24</p>
    </div>
    <div class="nd-card">
      <p class="nd-label">단기금융상품 등 포함</p>
      <p class="nd-value">100.61조 원</p>
      <div class="nd-track" aria-hidden="true"><span style="width:100%"></span></div>
      <p class="nd-math">125.85 − 25.24</p>
    </div>
  </div>
  <p class="nd-note">32.62조 원은 재무제표로 직접 계산한 값이고, 100.61조 원은 회사 발표값입니다.</p>
</div>

재무상태표의 현금및현금성자산은 57.86조 원입니다. 삼성전자는 실적 발표 자료에서 여기에 단기금융상품 등을 포함해 **기말현금 125.85조 원**을 제시했습니다. 재무상태표상 단기금융상품만 약 67.97조 원으로, 두 계산의 차이가 생긴 가장 큰 항목입니다. [삼성전자 연결재무상태표 자산](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=6) · [삼성전자 2025년 4분기 실적 발표 자료, 별첨 2](https://images.samsung.com/kdp/ir/events/2025/2025_4Q_conference_kor.pdf)

같은 회사라도 기사나 앱에서 순현금 숫자가 다르게 보인다면, 먼저 기준일과 연결·별도 여부를 맞춰봅니다. 그다음 현금에 단기금융상품까지 넣었는지, 차입금에 리스부채가 들어갔는지 보면 차이의 이유를 찾을 수 있습니다.

## 순현금이 늘었다면 차입금도 줄었을까요?

삼성전자의 2024년 말과 2025년 말을 회사 발표 기준으로 비교하면 답이 나옵니다. 순현금이 늘어난 두 시점 사이에 차입금도 함께 늘었습니다.

| 연결 기준 | 2024년 말 | 2025년 말 | 증감 |
|---|---:|---:|---:|
| 현금 등 | 112.65조 원 | 125.85조 원 | +13.20조 원 |
| 차입금 | 19.33조 원 | 25.24조 원 | +5.91조 원 |
| 순현금 | 93.32조 원 | 100.61조 원 | +7.29조 원 |

현금 등이 차입금보다 더 많이 증가해 순현금이 커졌습니다. 위 표는 두 날짜의 **잔액**을 비교한 것입니다. 1년 동안 실제로 얼마를 빌리고 갚았는지는 현금흐름표와 관련 주석에서 확인할 수 있습니다. 차입금 잔액에는 환율과 새 리스계약처럼 현금 거래 이외의 변화도 반영될 수 있습니다. [실적 발표 자료, 별첨 2](https://images.samsung.com/kdp/ir/events/2025/2025_4Q_conference_kor.pdf) · [연결재무제표 주석 27](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=77)

## 순현금이 있어도 만기를 따로 보는 이유

가게 B로 돌아가 보겠습니다. 차입금 1억 원 가운데 8천만 원을 다음 달에 갚아야 한다고 해보겠습니다. 현금으로 셌던 1억 2천만 원 중 1억 원은 담보로 묶여 상환에 쓸 수 없습니다. 처음 계산한 순현금은 2천만 원이지만 자유롭게 쓸 수 있는 현금도 2천만 원뿐입니다. 다른 곳에서 들어올 돈이 없다면, 만기에 맞추려면 6천만 원을 더 마련해야 합니다.

그래서 저는 순차입금을 확인한 뒤에는 **가까운 만기에 얼마가 필요한지**부터 보려고 합니다. 그다음 현금의 사용 제한, 급여와 거래처 대금, 예정된 투자 지출을 확인합니다. 앞으로 사업에서 들어올 돈은 [영업현금흐름](/p/operating-cash-flow-explained/)을 보고, 설비 투자까지 감안한 현금의 흐름은 [잉여현금흐름](/p/free-cash-flow-explained/) 글과 함께 보면 이해하기 쉽습니다. 현금 사용 제한은 재무제표 주석에서 확인할 수 있습니다. [IFRS 해석위원회 자료](https://www.ifrs.org/news-and-events/updates/ifric/2021/ifric-update-september-2021/)

## 정리

순차입금은 총차입금에서 일정 범위의 현금성 자산을 뺀 금액입니다. 순차입금이 음수라면, 같은 기준으로 그 차액만큼 순현금이 있습니다.

숫자를 비교할 때는 **현금과 차입금에 무엇을 넣었는지**, 시점 사이에 **어느 쪽이 얼마나 변했는지**, **가까운 만기에 쓸 수 있는 돈이 얼마나 되는지**를 차례로 봅니다. 다음 편에서는 회사가 사업에서 번 이익으로 이자를 얼마나 감당하는지, **이자보상배율**을 살펴보겠습니다.

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
