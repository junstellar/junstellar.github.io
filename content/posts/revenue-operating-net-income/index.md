---
title: "매출액·영업이익·순이익이란? 차이와 손익계산서 읽는 법"
description: "매출액, 영업이익, 당기순이익의 뜻과 차이를 가게 계산 예시로 설명합니다. 영업이익률 계산법과 삼성전자 2025년 연결 실적을 통해 매출이 늘어도 이익이 줄고, 순이익이 영업이익보다 커질 수 있는 이유를 알아봅니다."
slug: "revenue-operating-net-income"
date: 2026-11-11T00:00:00+09:00
draft: false
image: "earnings-cover.jpg"
categories: ["AI 투자"]
tags: ["매출액", "영업이익", "당기순이익", "영업이익률", "재무제표 보는 법"]
---

<style>
.article-content{container-type:inline-size}.eb-intro{font-size:13px;opacity:.75}
.eb{--paper:#f7f4ec;--ink:#193e37;--muted:#526b65;--card:#fffef9;--line:#cbd7cc;--teal:#16766b;--coral:#ad4d36;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:14px;margin:32px 0;padding:28px;line-height:1.7;word-break:keep-all;overflow-wrap:anywhere}.eb *{box-sizing:border-box}.eb p{margin:0}.eb .kicker{font-size:12px;font-weight:800;color:var(--teal);letter-spacing:.04em;margin-bottom:10px}.eb .figtitle{font-size:26px;line-height:1.4;font-weight:800;margin-bottom:22px}.eb .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.eb .card{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--teal);border-radius:9px;padding:20px;min-width:0}.eb .label{font-size:14px;color:var(--muted)}.eb .big{font-size:34px;font-weight:900;line-height:1.3;letter-spacing:-.04em;margin:13px 0;color:var(--teal)}.eb .total{font-size:22px;font-weight:800;border-top:1px dashed var(--line);padding-top:14px;margin-top:16px}.eb .note{font-size:12px;color:var(--muted);margin-top:18px}.eb .strip{background:var(--card);border-left:4px solid var(--coral);padding:14px 18px;margin-top:18px;font-size:16px}.eb .warm{border-top-color:var(--coral)}.eb .warm .big{color:var(--coral)}.eb .ledger{background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}.eb .row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:12px;padding:12px 18px;border-bottom:1px solid var(--line);font-size:16px}.eb .row:last-child{border:0}.eb .row b{text-align:right;white-space:nowrap}.eb .row.key{background:#e5eddb;font-weight:800;color:#193e37;font-size:20px}.eb .row.cost{color:var(--muted);font-size:14px}.eb .row small{display:block;font-size:12px;font-weight:400;opacity:.8}.eb .bartrack{height:12px;background:var(--line);border-radius:9px;margin:16px 0}.eb .bar{height:100%;background:var(--teal);border-radius:9px}.eb .warm .bar{background:var(--coral)}
[data-scheme=dark] .eb{--paper:#233c36;--ink:#f0f5ed;--muted:#b9cec0;--card:#2b453d;--line:#526e60;--teal:#a1e4d1;--coral:#ffb7a3}
@container(max-width:580px){.eb{padding:22px 18px}.eb .grid{grid-template-columns:1fr}.eb .figtitle{font-size:23px}.eb .row{padding:12px}.eb .row.key{font-size:18px}}
@media(max-width:600px){.eb{padding:22px 18px}.eb .grid{grid-template-columns:1fr}.eb .figtitle{font-size:23px}.eb .row{padding:12px}.eb .row.key{font-size:18px}}
</style>

<p class="eb-intro">회사 실적 읽는 법 · 첫 번째 이야기 / 자료 확인: 2026.11.11</p>

## 매출액은 판 금액, 영업이익과 순이익은 비용을 반영한 결과입니다

<strong>매출액은 회사가 상품이나 서비스를 팔아 인식한 수익, 영업이익은 그 영업에 들어간 비용을 빼고 남은 이익, 순이익은 영업 밖의 손익과 법인세 등까지 반영한 최종 이익</strong>입니다.

동네 가게가 올해 1억원어치를 팔았다고 해보겠습니다. 사장님이 1억원을 벌어 간 것은 아닙니다. 물건을 들여온 값도 내야 하고, 직원 급여와 가게 운영비도 부담해야 합니다. 은행에서 빌린 돈이 있다면 이자도 나갑니다. ‘얼마나 팔았나’와 ‘얼마나 남겼나’를 나눠 봐야 하는 이유입니다.

기업의 실적 기사에 매출과 영업이익이 나란히 나오는 것도 같습니다. [PER](/p/per-explained/)과 [ROE](/p/roe-explained/)를 공부하면서 등장한 순이익은 여기에서 한 단계 더 내려간 숫자입니다. 그 이익이 어떻게 만들어지는지 가게 한 곳의 계산으로 풀어보겠습니다.

## 1억원을 판 가게에 순이익 640만원이 남는 과정

상품을 사서 파는 작은 법인 가게를 가정하겠습니다. 1년 매출액은 1억원이고, 그해 판매한 상품의 매입원가는 6,000만원입니다. 우선 이를 빼면 4,000만원이 남습니다. 이 중간 금액을 **매출총이익**이라고 합니다.

하지만 여기서 끝이 아닙니다. 직원 급여·광고비·가게 운영비 등 판매와 관리에 든 비용이 3,000만원이라면 영업이익은 1,000만원입니다. 여기에 대출 이자 200만원을 빼고, 법인세비용을 160만원으로 가정하면 순이익은 640만원입니다.

<div class="eb" role="figure" aria-label="가상 가게 손익계산: 매출1억원-매출원가6000만원=매출총이익4000만원-판매관리비3000만원=영업이익1000만원-이자200만원-법인세160만원=순이익640만원">
<p class="kicker">설명용 가상 가게 / 한 해 실적 / 단위: 만원</p>
<div class="figtitle">1억원을 팔아도<br>이익이 1억원은 아닙니다.</div>
<div class="ledger"><div class="row key"><span>매출액<small>상품을 판 금액</small></span><b>10,000</b></div><div class="row cost"><span>판매한 상품의 원가</span><b>-6,000</b></div><div class="row"><span>매출총이익</span><b>4,000</b></div><div class="row cost"><span>판매비와 관리비</span><b>-3,000</b></div><div class="row key"><span>영업이익<small>영업에 든 비용까지 반영</small></span><b>1,000</b></div><div class="row cost"><span>이자비용</span><b>-200</b></div><div class="row"><span>법인세비용차감전순이익</span><b>800</b></div><div class="row cost"><span>법인세비용</span><b>-160</b></div><div class="row key"><span>당기순이익<small>그 기간의 최종 이익</small></span><b>640</b></div></div>
<p class="note">부가가치세를 제외한 금액이며, 비용 분류를 단순화했습니다. 이자 외의 영업외손익은 없다고 가정했습니다. 법인세 160만원은 설명용 가정으로 실제 세율을 적용한 세액 안내가 아닙니다.</p>
</div>

각 숫자를 조금 더 구분해 보겠습니다.

**매출액**은 사업의 판매 규모를 보여줍니다. 상품 수량이 늘거나 가격이 오르면 커질 수 있습니다. 다만 돈이 입금된 날과 매출을 인식하는 날은 다를 수 있어, 매출액을 통장에 들어온 현금과 같다고 보면 안 됩니다.

**영업이익**은 일반적인 제조·유통기업에서 매출액에서 매출원가와 판매비·관리비를 뺀 결과입니다. 여기서 매출원가는 ‘그 기간에 산 모든 물건값’이 아니라 **그 기간에 판매한 상품이나 제품에 대응하는 원가**입니다. 팔리지 않은 재고는 구분해야 합니다. 급여나 감가상각도 사용처에 따라 원가 또는 판매관리비 등에 들어갈 수 있으므로 한쪽 항목으로만 외우지는 않는 편이 좋습니다.

**당기순이익**의 ‘당기’는 해당 기간이라는 뜻입니다. 영업이익에 금융손익·기타손익 등을 더하거나 빼고 법인세비용 등을 반영한 결과입니다. 마이너스라면 당기순손실입니다. 은행·보험 등은 사업과 손익 표시 구조가 다르므로, 이 가게 예시를 모든 업종에 그대로 적용할 수는 없습니다. [SEC의 손익계산서 기초 설명](https://www.sec.gov/investor/pubs/begfinstmtguide.htm)

저는 세 숫자 옆에 **판 규모, 영업에서 남긴 금액, 최종 손익**이라고 적어 놓으니 구분하기가 쉬웠습니다. 전부 ‘회사가 번 돈’이라고 부르면 정작 무엇이 늘었는지 놓치게 됩니다.

## 매출이 늘어도 영업이익은 줄 수 있습니다

가게 매출이 다음 해 1억 2,000만원으로 늘었다면 좋은 소식처럼 보입니다. 그런데 상품 원가가 7,800만원, 판매관리비가 3,600만원으로 늘었다면 어떨까요? 영업이익은 600만원입니다. **매출은 20% 늘었지만 영업이익은 40% 줄었습니다.**

<div class="eb" role="figure" aria-label="가상 비교: 작년 매출1억원 원가6000만원 판매관리비3000만원 영업이익1000만원 이익률10퍼센트. 올해 매출1억2000만원 원가7800만원 판매관리비3600만원 영업이익600만원 이익률5퍼센트">
<p class="kicker">앞의 가게가 다음 해에도 영업했다는 가정</p>
<div class="figtitle">더 많이 팔았는데,<br>영업이익은 줄었습니다.</div>
<div class="grid"><div class="card"><div class="label">작년 · 매출 1억원</div><div class="big">1,000만원</div><div>매출원가 6,000만원<br>판매관리비 3,000만원</div><div class="bartrack"><div class="bar" style="width:100%"></div></div><div class="total">영업이익률 10%</div></div><div class="card warm"><div class="label">올해 · 매출 1억 2,000만원</div><div class="big">600만원</div><div>매출원가 7,800만원<br>판매관리비 3,600만원</div><div class="bartrack"><div class="bar" style="width:60%"></div></div><div class="total">영업이익률 5%</div></div></div>
<p class="note">큰 숫자와 막대는 영업이익입니다. 원가와 판매관리비가 매출보다 빠르게 늘어난 가상 예시이며 실제 기업의 수치가 아닙니다.</p>
</div>

이때 **영업이익률 = 영업이익 ÷ 매출액 × 100**을 계산하면 매출 규모가 달라도 비교하기 편합니다. 작년에는 100원을 팔아 영업이익 10원이 남았고, 올해는 5원이 남은 셈입니다. 영업이익률은 10%에서 5%로 **5%포인트** 낮아졌습니다.

장사가 더 바빠져도 원재료나 상품 매입 가격이 오르거나, 할인 판매와 광고 지출이 늘면 수익성은 나빠질 수 있습니다. 반대로 같은 매출에서도 원가를 줄이거나 이익이 많이 남는 제품의 비중이 커지면 영업이익이 늘 수 있습니다.

그렇다고 비용 증가를 무조건 나쁘게 볼 일은 아닙니다. 신제품 개발이나 새 매장 준비에 먼저 비용을 썼을 수도 있습니다. 중요한 것은 매출 증가라는 결과만 보지 않고 **어떤 비용이 늘었는지, 그 지출이 앞으로 성과로 이어질지**를 묻는 것입니다.

## 삼성전자 2025년 실적에서는 순이익이 영업이익보다 큽니다

실제 손익계산서를 보면 앞의 가게처럼 아래로 갈수록 숫자가 줄기만 하는 것은 아닙니다. 삼성전자의 **2025년 연간 연결재무제표**를 보겠습니다. 분기 실적이나 현재 전망이 아닌, 한 해가 끝난 뒤 감사받은 실적입니다.

| 항목 | 2025년 금액 |
|---|---:|
| 매출액 | 333.61조원 |
| 매출원가 | 202.24조원 |
| 매출총이익 | 131.37조원 |
| 판매비와 관리비 | 87.77조원 |
| 영업이익 | 43.60조원 |
| 당기순이익 | 45.21조원 |

출처: [삼성전자 2025년 연결재무제표 손익계산서](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=9). 원문의 백만원 단위를 조원으로 환산해 소수 둘째 자리까지 표시했습니다. 반올림 때문에 표시된 금액끼리 계산하면 미세한 차이가 날 수 있습니다.

순이익 45.21조원이 영업이익 43.60조원보다 큽니다. 영업이익 아래에서 금융수익·금융비용, 기타수익·기타비용, 관계기업·공동기업 손익 등이 추가로 반영되기 때문입니다. 이 항목들의 순합계가 약 **플러스 5.88조원**이고, 법인세비용 약 **4.27조원**을 차감하면 순이익으로 이어집니다.

<div class="eb" role="figure" aria-label="삼성전자2025 연결 실적: 영업이익43.60조원에 영업이익아래손익순합계5.88조원을 더하고 법인세4.27조원을 빼면 당기순이익45.21조원. 반올림금액">
<p class="kicker">삼성전자 / 2025년 연간 연결 실적 / 단위: 조원</p>
<div class="figtitle">영업이익 아래에는<br>더해지는 수익도 있습니다.</div>
<div class="ledger"><div class="row key"><span>영업이익</span><b>43.60</b></div><div class="row"><span>금융·기타손익 등<small>관련 수익과 비용을 합친 순금액</small></span><b>+5.88</b></div><div class="row"><span>법인세비용차감전순이익</span><b>49.48</b></div><div class="row cost"><span>법인세비용</span><b>-4.27</b></div><div class="row key"><span>당기순이익</span><b>45.21</b></div></div>
<p class="note">기타영업외수익·비용, 관계기업·공동기업 순손익 지분, 금융수익·비용을 합산했습니다. 각 금액은 소수 둘째 자리까지 반올림했습니다. 지배주주 순이익과 비지배지분 순이익을 합친 연결 전체 순이익입니다.</p>
</div>

이 사례에서 기억할 것은 ‘삼성전자는 순이익이 더 크다’라는 결론보다 **영업이익과 순이익 사이에 무엇이 있는지 확인하는 순서**입니다. 금융수익을 전부 예금 이자라고 생각하거나, 영업이익 아래의 손익을 모두 일회성이라고 생각해서도 안 됩니다. 성격과 지속성은 세부 내역을 봐야 합니다.

## 실적표를 볼 때는 기간·범위·이익의 내용을 맞춥니다

숫자의 뜻을 알았다면 이제 같은 조건으로 비교하는 차례입니다. 저는 실적표를 열면 세 가지를 먼저 확인하려 합니다.

**첫째, 같은 기간인가요?** 3분기 한 분기의 실적과 1~3분기 누적 실적은 다릅니다. 계절성이 있는 기업은 직전 분기보다 지난해 같은 분기와 비교하는 것이 유용할 수 있습니다. 전년 대비와 전분기 대비 중 무엇을 말하는지도 살펴야 합니다.

**둘째, 연결 기준인가요, 별도 기준인가요?** 연결재무제표는 지배하는 종속기업을 포함해 하나의 경제적 실체처럼 보고 내부 거래 등을 제거합니다. 별도재무제표는 해당 회사 자체를 기준으로 합니다. 같은 회사명이라고 두 기준의 숫자를 섞으면 안 됩니다.

연결 순이익 아래에 **지배기업 소유주 귀속 순이익**과 **비지배지분 귀속 순이익**이 나뉘어 있기도 합니다. 연결된 자회사 중 다른 주주가 가진 몫을 구분한 것입니다. [PER](/p/per-explained/)이나 [ROE](/p/roe-explained/)를 볼 때도 내가 읽는 이익이 어느 주주 범위에 해당하는지 맞춰야 합니다.

**셋째, 왜 늘거나 줄었나요?** 매출이 늘었다면 판매량·가격·제품 구성 중 무엇이 달라졌는지, 영업이익이 줄었다면 어떤 원가나 비용이 늘었는지 확인합니다. 순이익만 크게 움직였다면 이자·환율 관련 손익, 자산 처분, 세금 등 영업이익 아래 항목도 봅니다. 영업이익에도 일회성 비용이 들어갈 수 있으므로, 영업이익이라는 이름만으로 매년 반복되는 이익이라고 단정하지는 않습니다.

이 질문은 기업의 IR 실적자료나 사업보고서의 설명, 재무제표 주석에서 이어갈 수 있습니다. 모든 줄을 한 번에 해독하려 하기보다, **크게 변한 항목의 이유를 찾는 것**부터 시작하면 조금 덜 막막합니다.

## 정리

매출액은 얼마나 팔았는지, 영업이익은 영업에 든 비용을 반영해 얼마나 남겼는지, 순이익은 다른 손익과 세금 등까지 반영한 최종 결과를 보여줍니다. 매출이 늘어도 비용이 더 빠르게 늘면 영업이익은 줄 수 있고, 다른 수익이 더해지면 순이익이 영업이익보다 커질 수도 있습니다.

실적 기사에서 ‘이익 증가’를 보면 이제 **어느 이익이, 어떤 이유로 늘었는지**부터 확인하려 합니다. 같은 기간과 연결·별도 기준을 맞추는 것도 함께요.

여기까지 알면 다음 질문이 남습니다. 순이익이 났다면 그 돈은 회사 통장에도 들어와 있을까요? 꼭 그렇지는 않습니다. 외상으로 팔아도 매출과 이익이 잡힐 수 있고, 재고나 설비에 현금이 쓰이기도 합니다. **2편에서는 영업현금흐름을 통해 흑자인 회사에 현금이 부족할 수 있는 이유**를 살펴보겠습니다.

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
