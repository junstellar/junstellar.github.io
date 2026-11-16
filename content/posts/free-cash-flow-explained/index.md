---
title: "잉여현금흐름(FCF)이란? 투자하고 남은 돈을 보는 법"
description: "잉여현금흐름(FCF)의 뜻과 계산법, 영업현금흐름과의 차이를 설명합니다. 가게의 기계 교체 예시와 삼성전자 현금흐름표로 설비투자(CAPEX)를 빼는 이유, FCF가 마이너스일 때 살펴볼 점을 알아봅니다."
slug: "free-cash-flow-explained"
date: 2026-11-16T00:00:00+09:00
draft: false
image: "fcf-cover.jpg"
categories: ["AI 투자"]
tags: ["잉여현금흐름", "FCF", "영업현금흐름", "CAPEX", "재무제표 보는 법"]
---

<style>
.article-content{container-type:inline-size}.fc-intro{font-size:13px;opacity:.75}.fc{--paper:#f7f4ec;--ink:#193e37;--muted:#526b65;--card:#fffef9;--line:#cbd7cc;--teal:#16766b;--coral:#ad4d36;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:14px;margin:32px 0;padding:28px;line-height:1.7;word-break:keep-all;overflow-wrap:anywhere}.fc *{box-sizing:border-box}.fc p{margin:0}.fc .kicker{font-size:12px;font-weight:800;color:var(--teal);margin-bottom:10px}.fc .figtitle{font-size:26px;line-height:1.4;font-weight:800;margin-bottom:22px}.fc .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.fc .card{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--teal);border-radius:9px;padding:20px;min-width:0}.fc .label{font-size:15px;font-weight:700;color:var(--muted)}.fc .big{font-size:34px;font-weight:900;line-height:1.3;letter-spacing:-.04em;margin:17px 0;color:var(--teal)}.fc .note{font-size:12px;color:var(--muted);margin-top:18px}.fc .warm{border-top-color:var(--coral)}.fc .warm .big{color:var(--coral)}.fc .ledger{background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}.fc .row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;padding:14px 18px;border-bottom:1px solid var(--line);font-size:16px}.fc .row:last-child{border:0}.fc .row b{text-align:right;white-space:nowrap}.fc .row.key{background:#e5eddb;font-weight:800;color:#193e37;font-size:20px}.fc .row small{display:block;font-size:12px;font-weight:400;color:var(--muted)}.fc .calc{font-size:15px;line-height:1.9;border-top:1px dashed var(--line);padding-top:12px}.fc .strip{margin-top:18px;padding:14px 18px;background:var(--card);border-left:4px solid var(--coral);font-size:15px}
[data-scheme=dark] .fc{--paper:#233c36;--ink:#f0f5ed;--muted:#b9cec0;--card:#2b453d;--line:#526e60;--teal:#a1e4d1;--coral:#ffb7a3}
@container(max-width:580px){.fc{padding:22px 18px}.fc .grid{grid-template-columns:1fr}.fc .figtitle{font-size:23px}.fc .row{padding:12px}.fc .row.key{font-size:18px}}
@media(max-width:600px){.fc{padding:22px 18px}.fc .grid{grid-template-columns:1fr}.fc .figtitle{font-size:23px}.fc .row{padding:12px}}
</style>

<p class="fc-intro">회사 실적 읽는 법 · 세 번째 이야기 / 자료 확인: 2026.11.16</p>

## 잉여현금흐름은 영업에서 번 현금에서 투자 지출을 빼서 봅니다

<strong>잉여현금흐름(Free Cash Flow, FCF)은 보통 영업현금흐름에서 설비 등 자산에 투자한 현금 지출을 빼서 계산하는 지표</strong>입니다. 사업을 통해 들어온 현금 중 투자 후 얼마나 남았는지 살펴볼 때 씁니다.

가게가 한 해 장사를 해서 현금 3,000만원을 남겼다고 해보겠습니다. 그런데 오래된 냉장고와 주방 설비를 바꾸는 데 2,000만원이 필요합니다. 가게를 계속 운영하려면 써야 할 돈입니다. 사장님이 3,000만원을 전부 가져가도 되는 상황은 아닌 셈입니다.

[지난 편의 영업현금흐름](/p/operating-cash-flow-explained/)은 외상값과 재고까지 고려해 영업에서 현금이 얼마나 들어오고 나갔는지 보여줬습니다. 이번에는 거기서 한 걸음 더 내려가 보겠습니다. **영업에서 현금을 벌었다면, 사업에 다시 투자하고도 남는가?** 이 질문을 숫자로 보는 방법입니다.

## 현금 3,000만원을 벌어 기계에 2,000만원을 썼다면

앞의 가게가 받은 고객 대금에서 상품 대금·급여·임차료·영업활동에 분류된 세금 등을 지급하고 남은 영업현금흐름이 3,000만원이라고 하겠습니다. 여기에 기계 교체에 현금 2,000만원을 썼다면 단순한 FCF는 1,000만원입니다.

<div class="fc" role="figure" aria-label="가상 가게의 연간 영업현금흐름3000만원에서 기계 취득 현금지출2000만원을 빼면 단순 FCF1000만원입니다.">
<p class="kicker">설명용 가게 / 한 해 / 단위: 만원</p><div class="figtitle">장사로 남긴 3,000만원을<br>전부 가져갈 수는 없습니다.</div>
<div class="ledger"><div class="row key"><span>영업현금흐름<small>영업에서 들어오고 나간 현금의 차이</small></span><b>3,000</b></div><div class="row"><span>기계 취득 지출<small>오래된 설비 교체에 지급한 현금</small></span><b>-2,000</b></div><div class="row key"><span>단순 FCF<small>이 예시에서 투자 후 남은 금액</small></span><b>1,000</b></div></div>
<p class="note">다른 투자 지출과 조정 항목이 없다는 가정입니다. FCF 1,000만원은 통장 잔액이나 배당 가능액을 뜻하지 않습니다.</p></div>

이때 기계·공장처럼 여러 해 사용할 자산에 돈을 쓰는 것을 <strong>자본적 지출(Capital Expenditure, CAPEX)</strong>이라고 합니다. 현금흐름표에서는 유형자산 취득 등 투자활동 항목을 찾아보게 됩니다. 매월 내는 임차료나 직원 급여와는 구분합니다. 이미 영업현금흐름에 반영된 현금 비용을 여기서 다시 빼면 중복 계산입니다.

감가상각비를 또 빼는 것도 아닙니다. [2편에서 본 감가상각](/p/operating-cash-flow-explained/)은 자산의 원가를 사용하는 기간에 나누어 비용으로 반영하는 방법입니다. 여기서는 그 비용이 아니라 **이번 기간에 자산을 사면서 실제로 지급한 현금**을 봅니다.

보통의 출발점은 **FCF = 영업현금흐름 - CAPEX**입니다. 다만 이 식을 모든 회사에 똑같이 적용되는 회계 항목처럼 외우면 곤란합니다. FCF는 통일된 정의가 없으므로 회사가 무엇을 빼고 조정했는지 확인해야 합니다. 미국 SEC도 FCF 설명에서 계산 방법을 명확히 제시하도록 안내합니다. [SEC 비일반회계기준 지표 설명, 질문 102.07](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures)

## 삼성전자 현금흐름표에서 직접 계산해 보겠습니다

앞의 두 편과 같은 **삼성전자 2025년 연간 연결재무제표**를 열어보겠습니다. 영업현금흐름은 약 85.32조원입니다. 투자활동에 있는 유형자산 취득과 무형자산 취득 지출을 빼보겠습니다. 무형자산은 소프트웨어·권리 등 물리적인 형태가 없는 자산입니다.

이 글의 계산 기준은 **영업현금흐름 - 유형자산 취득 현금지출 - 무형자산 취득 현금지출**입니다. 자산 처분 대금이나 보조금 등을 더하지 않은 단순 계산이며, 회사가 주주환원 정책에서 사용하는 FCF를 재현한 숫자는 아닙니다.

단위: 조원

| 현금흐름표 항목 | 2024년 | 2025년 |
|---|---:|---:|
| 영업활동 현금흐름 | 72.98 | 85.32 |
| 유형자산 취득에 지급한 현금 | 51.41 | 47.52 |
| 무형자산 취득에 지급한 현금 | 2.34 | 4.63 |
| 위 두 취득 지출을 뺀 단순 FCF | **19.24** | **33.16** |

출처: [삼성전자 2025년 연결 현금흐름표의 2025·2024년 비교](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=15). 단위는 조원이며, 계산은 반올림 전 원문 금액으로 했습니다. 표의 반올림된 숫자끼리 빼면 차이가 날 수 있습니다.

<div class="fc" role="figure" aria-label="삼성전자2025 연결. 영업현금흐름85.315148조원에서 유형 및 무형자산 취득 합계52.153149조원을 빼면 글의 기준으로 계산한 FCF33.161999조원. 도해는 소수 셋째자리 표시.">
<p class="kicker">삼성전자 / 2025년 연간 연결 / 단위: 조원</p><div class="figtitle">영업현금흐름 85.3조원에서<br>자산 취득 지출을 빼면</div>
<div class="ledger"><div class="row key"><span>영업현금흐름</span><b>85.315</b></div><div class="row"><span>유형·무형자산 취득<small>현금흐름표의 두 취득 지출 합계</small></span><b>-52.153</b></div><div class="row key"><span>이 글의 단순 FCF</span><b>33.162</b></div></div>
<p class="note">원문 금액으로 계산한 뒤 각각 소수 셋째 자리까지 반올림했습니다. 회사 공식 FCF나 배당 예정액이 아닙니다.</p></div>

같은 기준으로 비교하면 2025년에는 영업현금흐름이 늘고 두 자산 취득 지출의 합계는 줄어, 계산 결과가 커졌습니다. 다만 숫자가 늘었다는 것만으로 다음 해에도 같은 현금이 남는다고 단정할 수는 없습니다.

여기서 **투자활동 현금흐름 전체를 빼지 않았다는 점**도 중요합니다. 투자활동에는 설비 취득 외에 금융상품 거래와 기업 인수 등도 섞여 있습니다. CAPEX를 보려는데 투자활동 전체를 사용하면 계산하려던 지표가 달라집니다.

회사 IR 자료의 CAPEX와 현금흐름표의 자산 취득 현금지출도 이름만 보고 같다고 놓지 않는 편이 좋습니다. 집계 범위나 인식 시점이 다를 수 있습니다. 비교할 때는 같은 기간·연결 기준인지, 어떤 항목을 포함했는지부터 맞춥니다.

## FCF가 마이너스면 나쁜 회사일까요

영업에서 들어온 현금보다 자산 투자에 쓴 현금이 많으면 FCF는 마이너스가 됩니다. 이것만으로 장사가 안됐다고 결론 내릴 수는 없습니다. 새 공장이나 매장을 준비하는 해에는 돈이 먼저 나갈 수 있기 때문입니다.

가게 두 곳을 비교해 보겠습니다. A가게는 영업에서 3,000만원을 남겼지만 새 매장 설비에 4,000만원을 투자했습니다. B가게는 영업에서 남긴 현금이 500만원인데 오래된 필수 설비 교체에 1,500만원을 썼습니다. 둘 다 FCF는 마이너스 1,000만원입니다.

<div class="fc" role="figure" aria-label="가상 A가게는 영업현금3000만원-새매장설비4000만원=-1000만원. B가게는 영업현금500만원-기존필수설비1500만원=-1000만원. 같은 음수라도 투자 목적과 영업 상태를 확인해야 합니다.">
<p class="kicker">설명용 가게 두 곳 / 같은 한 해 / 단위: 만원</p><div class="figtitle">같은 마이너스라도<br>돈을 쓴 이유는 다릅니다.</div>
<div class="grid"><div class="card"><div class="label">A · 새 매장 준비</div><div class="big">-1,000만원</div><div class="calc">영업현금흐름 3,000<br>새 매장 설비 취득 -4,000</div><p class="note">새 매장이 현금을 벌기까지<br>자금을 감당할 수 있을까요?</p></div><div class="card warm"><div class="label">B · 기존 설비 교체</div><div class="big">-1,000만원</div><div class="calc">영업현금흐름 500<br>필수 설비 취득 -1,500</div><p class="note">현재 장사에서 남는 현금이<br>왜 적은지 확인해야 합니다.</p></div></div>
<div class="strip">A가 성공한다는 뜻은 아닙니다. 투자 목적에 더해 자금 여력과 이후 성과까지 봅니다.</div></div>

사업을 유지하기 위한 교체 투자와 규모를 키우기 위한 성장 투자를 나눠 생각하면 이해하기 쉽습니다. 다만 실제 공장에서는 노후 설비를 바꾸면서 생산능력도 늘릴 수 있습니다. 두 목적을 정확히 분리하기 어렵고, 회사가 금액을 따로 공개하지 않는 경우도 있습니다. **‘성장 투자니까 빼지 않아도 된다’며 지출 일부를 근거 없이 계산에서 제외하면 현금 여력을 과장할 수 있습니다.**

FCF가 줄었다면 먼저 영업현금흐름이 약해진 것인지, 투자 지출이 늘어난 것인지 나눠 봅니다. 투자가 늘었다면 어디에 왜 썼는지, 가동과 매출 발생까지 얼마나 걸리는지 회사 설명을 확인합니다. 그동안 현금 보유액이나 자금 조달로 버틸 수 있는지도 함께 봐야 합니다.

반대로 FCF가 늘었다고 항상 좋은 것도 아닙니다. 필요한 설비 교체를 뒤로 미루면 당장의 숫자는 좋아질 수 있습니다. 저는 FCF 증가를 보면 ‘돈을 더 잘 벌어서 늘었나, 투자를 덜 해서 늘었나’를 먼저 나눠 보려고 합니다.

## 남은 돈은 전부 배당해도 될까요

처음에는 ‘잉여’라는 말 때문에 용도가 없는 여윳돈처럼 느껴졌습니다. 하지만 위의 FCF 계산에는 대출 원금 상환이 들어 있지 않습니다. 가까운 시기에 갚을 빚이 있거나 다른 필수 지출이 예정돼 있다면 그 돈도 마련해야 합니다. SEC 역시 FCF를 아무 제약 없이 쓸 수 있는 잔여 현금처럼 표현하지 않도록 주의를 줍니다. [SEC 질문 102.07](https://www.sec.gov/rules-regulations/staff-guidance/corporation-finance-interpretations/non-gaap-financial-measures)

앞의 가게가 단순 FCF 1,000만원을 남겼어도 같은 기간에 대출 원금 700만원을 상환했다면, 그 두 항목만 반영한 현금 증가는 300만원입니다. 다른 현금 이동이 없다면 기초 현금 잔액에 300만원이 더해지는 것이지, 통장 잔액이 곧 FCF 1,000만원이 되는 것은 아닙니다.

투자자에게 FCF가 유용한 이유는 **사업을 이어가면서 빚 상환·추가 투자·주주환원에 쓸 현금을 만들어낼 여력이 있는지** 생각하게 해주기 때문입니다. FCF가 배당액을 자동으로 정해주지는 않습니다. 실제 배당이나 자사주 매입은 재무 상태와 회사의 자금 배분 결정을 함께 봐야 합니다.

계산 기준에도 주의해야 합니다. 여기서는 일반적인 비금융기업의 현금흐름표를 출발점으로 한 간단한 FCF를 다뤘습니다. 기업가치 평가에서 쓰는 FCFF·FCFE는 이자·차입 등을 다루는 방식이 달라, 이 글의 숫자를 그대로 대입하면 안 됩니다.

## 세 편의 숫자를 이어서 읽어보겠습니다

손익계산서와 현금흐름표를 따로 외우려니 복잡했는데, 질문을 이어 놓으니 조금 정리가 됩니다.

| 확인할 숫자 | 답하려는 질문 | 함께 볼 내용 |
|---|---|---|
| 매출액·영업이익·순이익 | 얼마나 팔고 이익을 남겼나요? | 원가·비용과 이익이 변한 이유 |
| 영업현금흐름 | 영업에서 실제로 현금이 들어왔나요? | 외상 대금·재고·비현금 항목 |
| 잉여현금흐름 | 자산에 투자하고도 현금이 남았나요? | 계산 범위·투자 목적·상환 부담 |

실제 회사 자료에서는 **같은 기간과 기준의 영업현금흐름을 확인하고, 자산 취득 지출을 찾아 계산한 뒤, 지난해와 차이가 난 이유를 읽는 순서**로 시작할 수 있습니다. 회사가 FCF를 따로 발표했다면 계산 설명도 확인합니다. 같은 이름이라도 내가 구한 숫자와 무엇이 다른지 대조해 보는 겁니다.

이 숫자들이 좋다고 주가가 싸다는 뜻까지 되는 것은 아닙니다. 현금을 잘 만드는 회사인지와, 그 회사를 어느 가격에 사는지는 별개의 질문입니다. 앞서 공부한 [PER](/p/per-explained/)·[PBR](/p/pbr-explained/)·[ROE](/p/roe-explained/)도 이익과 자본의 내용을 이해한 뒤 다시 보면 더 잘 읽힙니다.

## 정리

잉여현금흐름은 보통 영업현금흐름에서 CAPEX를 빼서 봅니다. **사업을 통해 현금이 들어왔다는 사실에 더해, 자산에 다시 투자하고도 남는지를 확인하는 지표**입니다.

FCF가 마이너스라면 투자 확대 때문인지 영업 부진 때문인지, 플러스가 커졌다면 영업이 좋아진 것인지 투자를 줄인 것인지 나눠 봅니다. 계산 범위가 회사마다 다를 수 있고, 남은 금액에 빚 상환 같은 부담이 있다는 점도 함께 기억하려 합니다.

‘회사 실적 읽는 법’은 이번 3편으로 마칩니다. [1편의 이익](/p/revenue-operating-net-income/), [2편의 영업현금흐름](/p/operating-cash-flow-explained/), 이번 편의 투자 후 현금을 연결해 보면, 실적 기사에서 좋은 숫자 하나를 발견했을 때 그다음에 무엇을 물어볼지 조금 더 분명해집니다.

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
