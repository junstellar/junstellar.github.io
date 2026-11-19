---
title: "부채비율이란? 계산법과 100%·200%의 의미"
description: "부채비율의 뜻과 계산법, 100%와 200%가 의미하는 바를 설명합니다. 삼성전자 재무제표와 가상 기업 도해로 부채와 차입금의 차이, 자본 감소가 비율에 미치는 영향, 회사의 빚을 판단할 때 함께 볼 항목을 알아봅니다."
slug: "debt-ratio-explained"
date: 2026-11-19T00:00:00+09:00
draft: false
image: "debt-cover.jpg"
categories: ["AI 투자"]
tags: ["부채비율", "부채비율 계산", "재무제표 보는 법", "자기자본", "재무 건전성"]
---

<style>
.article-content{container-type:inline-size}.db-intro{font-size:13px;opacity:.75}.db{--paper:#f7f4ec;--ink:#193e37;--muted:#526b65;--card:#fffef9;--line:#cbd7cc;--teal:#16766b;--coral:#ad4d36;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:14px;margin:32px 0;padding:28px;line-height:1.7;word-break:keep-all;overflow-wrap:anywhere}.db *{box-sizing:border-box}.db p{margin:0}.db .kicker{font-size:12px;font-weight:800;color:var(--teal);margin-bottom:10px}.db .figtitle{font-size:26px;line-height:1.4;font-weight:800;margin-bottom:22px}.db .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}.db .card{background:var(--card);border:1px solid var(--line);border-top:4px solid var(--teal);border-radius:9px;padding:20px;min-width:0}.db .label{font-size:15px;font-weight:700;color:var(--muted)}.db .big{font-size:36px;font-weight:900;line-height:1.3;letter-spacing:-.04em;margin:17px 0;color:var(--teal)}.db .note{font-size:12px;color:var(--muted);margin-top:18px}.db .warm{border-top-color:var(--coral)}.db .warm .big{color:var(--coral)}.db .calc{font-size:15px;line-height:1.9;border-top:1px dashed var(--line);padding-top:12px}.db .strip{margin-top:18px;padding:14px 18px;background:var(--card);border-left:4px solid var(--coral);font-size:15px}.db .stack{display:flex;height:66px;margin:18px 0 22px;border-radius:8px;overflow:hidden;font-size:18px;font-weight:800;text-align:center;line-height:66px}.db .own{background:#dce9bd;color:#244435;width:33.333%}.db .debt{background:#16766b;color:#fffef9;width:66.667%}
[data-scheme=dark] .db{--paper:#233c36;--ink:#f0f5ed;--muted:#b9cec0;--card:#2b453d;--line:#526e60;--teal:#a1e4d1;--coral:#ffb7a3}
@container(max-width:580px){.db{padding:22px 18px}.db .grid{grid-template-columns:1fr}.db .figtitle{font-size:23px}.db .stack{font-size:15px}}
@media(max-width:600px){.db{padding:22px 18px}.db .grid{grid-template-columns:1fr}.db .figtitle{font-size:23px}}
</style>

<p class="db-intro">회사의 빚 읽는 법 · 첫 번째 이야기 / 자료 확인: 2026.11.19</p>

## 부채비율은 자기자본에 비해 부채가 얼마나 많은지 나타냅니다

<strong>부채비율은 부채총계를 자기자본으로 나눈 뒤 100을 곱한 값</strong>입니다. 회사가 가진 자본에 비해 다른 사람에게 이행해야 할 의무가 얼마나 큰지 보는 재무구조 지표입니다.

작은 가게를 차리면서 주인이 1억원을 넣고 은행에서 2억원을 빌렸다고 해보겠습니다. 비용이나 다른 거래가 아직 없다면 가게의 자산은 3억원, 부채는 2억원, 자기자본은 1억원입니다. 이 가게의 부채비율은 200%입니다.

저는 처음에 200%라는 숫자를 보면 ‘가진 것보다 빚이 두 배나 많은 건가?’ 싶었습니다. 그런데 나누는 대상이 자산이 아니라 자기자본이라는 점을 놓친 것이었습니다. 이번 글은 이 차이부터 풀어보겠습니다.

앞 시리즈에서는 [이익](/p/revenue-operating-net-income/)과 [영업현금흐름](/p/operating-cash-flow-explained/), [투자 후 남은 현금](/p/free-cash-flow-explained/)을 살펴봤습니다. 이제 그 회사가 얼마나 많은 부채를 안고 있는지, 숫자 하나만으로 위험을 판단해도 되는지 이어가겠습니다.

## 부채비율 200%는 자산의 200%가 빚이라는 뜻이 아닙니다

계산식은 간단합니다.

**부채비율 = 부채총계 ÷ 자기자본 × 100**

여기서 자기자본은 재무상태표의 **자본총계**로 생각하면 됩니다. 주주가 낸 돈뿐 아니라 회사에 쌓인 이익과 다른 자본 항목들도 포함됩니다. 자본금만 가져다 계산하면 다른 결과가 나옵니다. 자산에서 부채를 뺀 금액이 자본이라는 관계도 함께 기억하면 좋습니다. [SEC의 재무상태표·부채비율 기초 설명](https://www.sec.gov/investor/pubs/begfinstmtguide.htm)

<div class="db" role="figure" aria-label="가상 가게 자산3억원은 자기자본1억원과 부채2억원으로 구성. 부채를 자기자본으로 나누면200퍼센트, 자산으로 나누면 약66.7퍼센트.">
<p class="kicker">가게를 처음 차린 시점 / 다른 거래가 없는 가정</p><div class="figtitle">자산 3억원 중 빚은 2억원.<br>그런데 부채비율은 200%입니다.</div>
<div class="stack"><div class="own">자본 1억원</div><div class="debt">부채 2억원</div></div>
<div class="grid"><div class="card"><div class="label">부채 ÷ 자기자본</div><div class="big">200%</div><div class="calc">2억원 ÷ 1억원 × 100<br>이 글에서 말하는 부채비율</div></div><div class="card warm"><div class="label">부채 ÷ 자산</div><div class="big">66.7%</div><div class="calc">2억원 ÷ 3억원 × 100<br>자산 중 부채가 차지하는 비중</div></div></div>
<p class="note">막대는 자산을 구성하는 자본과 부채의 비중입니다. 66.7%는 반올림한 값입니다. 두 비율은 분모가 다릅니다.</p></div>

부채비율이 <strong>100%</strong>이면 부채와 자기자본이 같습니다. <strong>200%</strong>이면 부채가 자기자본의 두 배입니다. 자본이 플러스이고 ‘자산 = 부채 + 자본’ 관계를 적용하면, 부채비율 100%일 때 부채는 자산의 절반을 차지합니다.

따라서 부채비율이 100%를 넘었다고 곧바로 자산보다 부채가 많다는 뜻은 아닙니다. 해외 자료에서 비슷한 이름의 지표를 볼 때도 부채를 자본으로 나눈 것인지 자산으로 나눈 것인지 계산식을 확인하는 편이 정확합니다.

## 부채에는 은행 대출 말고도 여러 항목이 있습니다

부채비율을 읽으면서 가장 먼저 구분할 것은 **부채 전체와 이자를 내는 차입금이 같지는 않다**는 점입니다.

상품을 외상으로 들여오면 아직 지급하지 않은 대금이 매입채무로 잡힙니다. 직원에게 줄 비용이나 납부할 세금도 부채에 포함될 수 있습니다. 고객에게 돈을 먼저 받고 나중에 제품을 넘겨야 하는 의무도 부채로 표시될 수 있습니다. 은행 대출만 합친 숫자가 아닙니다.

| 부채의 예 | 어떤 의무인가요? | 볼 때의 질문 |
|---|---|---|
| 차입금·회사채 | 돈을 빌리고 원금과 이자 등을 지급하는 의무 | 금리와 만기는 어떤가요? |
| 매입채무 | 외상으로 산 상품 등의 대금 | 언제 지급해야 하나요? |
| 선수금·계약부채 | 먼저 받은 대가에 대응해 상품·서비스 등을 제공할 의무 | 앞으로 이행할 비용과 조건은 무엇인가요? |
| 미지급비용·세금 등 | 이미 발생했지만 아직 지급하지 않은 금액 등 | 지급 시점과 규모는 어떤가요? |

이 표는 부채를 안전한 것과 위험한 것으로 나눈 표가 아닙니다. 대출이 아니어도 결제하거나 의무를 이행하는 데 자금이 필요합니다. 다만 **왜 생겼고 어떻게 이행하는지**가 다르므로 부채총계 하나에 모두 같은 의미를 붙이면 안 됩니다.

특히 고객에게 먼저 받은 돈을 ‘공짜 자금’이라고 생각해서는 안 됩니다. 제품을 만들거나 서비스를 제공할 비용이 뒤따르고, 계약에 따라 환불 등의 부담도 생길 수 있습니다.

## 삼성전자 재무제표로 직접 계산해 보겠습니다

앞 시리즈에서 사용한 **삼성전자 2025년 연결재무제표**를 이어 보겠습니다. 손익계산서가 한 해의 성적이라면, 여기서는 **2025년 12월 31일 시점**의 부채와 자본을 보는 것입니다.

단위: 조원, 비율은 %

| 연결 재무상태표 항목 | 2024년 말 | 2025년 말 |
|---|---:|---:|
| 부채총계 | 112.34 | 130.62 |
| 자본총계 | 402.19 | 436.32 |
| 부채비율 | **27.9** | **29.9** |

2025년 말의 계산은 <strong>130.62조원 ÷ 436.32조원 × 100 = 약 29.9%</strong>입니다. 표의 비율은 반올림 전 원문 금액으로 계산했습니다. 연결 부채총계에 맞춰 자본도 비지배지분을 포함한 연결 자본총계를 사용했습니다. [삼성전자 연결재무상태표 부채](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=7), [자본](https://images.samsung.com/is/content/samsung/assets/global/ir/docs/2025_con_quarter04_all.pdf#page=8)

부채 내역에는 단기차입금뿐 아니라 매입채무·미지급비용·선수금·세금 등 여러 항목이 들어 있습니다. **부채총계 130.62조원을 전부 은행에서 빌린 돈으로 읽으면 안 됩니다.**

이 사례의 목적은 삼성전자의 투자 매력을 판정하는 데 있지 않습니다. 실제 재무제표에서 부채총계와 자본총계를 찾아 같은 기준으로 나눠 보는 것입니다. 증권 앱의 비율과 다르다면 연결·별도 기준, 기준일, 자본 범위를 먼저 확인합니다.

## 빚을 더 내지 않아도 부채비율은 오를 수 있습니다

부채비율이 올랐다는 기사를 보면 빚부터 늘었다고 생각하기 쉽습니다. 그런데 분모인 자본이 줄어도 비율은 올라갑니다.

앞의 가게가 자산 3억원, 부채 2억원, 자본 1억원으로 출발했다고 해보겠습니다. 이후 보유한 재고의 가치가 떨어져 5,000만원의 평가손실을 반영했고, 세금 등 다른 변동은 없다고 가정하겠습니다. 자산과 자본이 각각 5,000만원 줄지만 부채는 그대로입니다.

<div class="db" role="figure" aria-label="가상 가게 부채2억원은 그대로지만 평가손실5000만원으로 자본이1억원에서5000만원으로 줄면 부채비율은200퍼센트에서400퍼센트로 상승합니다.">
<p class="kicker">재고 평가손실 5,000만원만 반영한 가상 비교</p><div class="figtitle">빚은 그대로인데<br>부채비율이 두 배가 됐습니다.</div>
<div class="grid"><div class="card"><div class="label">손실 반영 전</div><div class="big">200%</div><div class="calc">자산 3억원<br>부채 2억원<br>자본 1억원</div></div><div class="card warm"><div class="label">손실 반영 후</div><div class="big">400%</div><div class="calc">자산 2억 5,000만원<br>부채 2억원<br>자본 5,000만원</div></div></div><div class="strip">부채의 증가뿐 아니라 손실 등으로 자본이 줄었는지도 확인합니다.</div>
<p class="note">세금과 다른 거래는 제외했습니다. 재고 평가손실을 인식하는 순간 현금 5,000만원이 새로 나갔다는 뜻은 아닙니다.</p></div>

반대로 이익이 회사 안에 쌓여 자본이 늘면 빚을 갚지 않았어도 부채비율이 낮아질 수 있습니다. 그래서 비율의 변화는 부채와 자본의 변화를 나눠 읽어야 합니다.

자본이 아주 작아지면 비율은 크게 튑니다. 자본이 0이면 나눗셈을 할 수 없고, 자본이 음수이면 계산상 음수가 나오더라도 ‘부채 부담이 낮다’는 뜻으로 해석할 수 없습니다. 이때는 비율의 크기보다 자본이 왜 훼손됐는지부터 봐야 합니다.

## 100% 이하면 안전하고 200%가 넘으면 위험할까요

숫자에 선을 하나 그어두면 편하지만, 그 선만으로 모든 회사의 상환 능력을 판단할 수는 없습니다. 업종마다 자산을 보유하는 방식과 결제 관행이 다르고, 부채의 구성과 만기도 다릅니다. 은행·보험처럼 금융부채가 사업의 핵심인 업종을 일반 제조업과 같은 기준으로 단순 비교하는 것도 적절하지 않습니다.

다음 두 회사는 모두 부채 2억원, 자본 1억원으로 부채비율이 200%라고 가정해 보겠습니다. 그런데 가진 현금과 가까운 상환 일정이 다릅니다.

<div class="db" role="figure" aria-label="가상 두 회사 모두 부채2억원 자본1억원으로 부채비율200퍼센트. A는 사용제한 없는현금8000만원 1년내차입금원금상환2000만원, B는 현금1000만원 1년내차입금원금상환1억5000만원. 비율만으로 상환부담을 알수없습니다.">
<p class="kicker">부채 2억원 · 자본 1억원인 가상 회사 두 곳</p><div class="figtitle">똑같은 200%라도<br>다가오는 결제 부담은 다릅니다.</div>
<div class="grid"><div class="card"><div class="label">A 회사 · 부채비율 200%</div><div class="big">8,000만원</div><div class="calc">사용 제한 없는 현금<br><br>1년 내 차입금 원금 상환<br><b>2,000만원</b></div></div><div class="card warm"><div class="label">B 회사 · 부채비율 200%</div><div class="big">1,000만원</div><div class="calc">사용 제한 없는 현금<br><br>1년 내 차입금 원금 상환<br><b>1억 5,000만원</b></div></div></div>
<p class="note">현재 현금과 차입금 원금 만기만 비교한 예시입니다. 앞으로의 영업현금흐름, 이자·다른 부채의 지급, 운영에 필요한 현금, 차환 가능성 등을 함께 봐야 합니다. A의 안전이나 B의 부도를 판정한 예시가 아닙니다.</p></div>

B가 대금을 곧 회수하거나 대출 만기를 연장할 수 있다면 상황은 달라집니다. 반대로 A도 사업에서 큰 현금 유출이 예정돼 있다면 여유가 줄 수 있습니다. **부채비율은 부채와 자본의 크기를 보여줄 뿐, 언제 얼마를 갚고 그 돈을 어디서 마련할지까지 알려주지는 않습니다.**

처음 자료를 볼 때 저는 다음 순서로 확인하려 합니다.

1. **같은 기준의 비율인지 확인합니다.** 연결·별도와 기준일을 맞추고, 지난해 같은 회사 및 비슷한 사업을 하는 회사와 비교합니다.
2. **비율이 변한 이유를 나눠 봅니다.** 부채가 늘었는지, 손실이나 주주환원 등으로 자본이 줄었는지 재무상태표와 설명을 확인합니다.
3. **차입금의 만기와 이자 부담을 확인합니다.** 가까운 시기에 갚을 금액, 금리 조건, 담보와 약정 등은 차입금·유동성 위험 관련 주석에서 살펴봅니다.
4. **현금을 마련할 힘이 있는지 봅니다.** 사용 가능한 현금, [영업현금흐름](/p/operating-cash-flow-explained/), [필요한 투자 지출](/p/free-cash-flow-explained/)을 함께 놓고 생각합니다. 현금처럼 보이는 자산도 사용이 제한돼 있거나 바로 현금화하기 어려울 수 있습니다.

부채비율이 낮으면 다른 조건이 같을 때 자본에 비한 부채 부담은 작습니다. 다만 낮은 비율 하나로 회사가 좋은 투자 대상이 되는 것은 아닙니다. 반대로 차입을 통해 투자하는 회사라면 그 투자가 이자와 상환 부담을 감당할 현금을 만들어내는지 봐야 합니다.

## 정리

부채비율은 **부채총계 ÷ 자기자본 × 100**입니다. 200%는 부채가 자본의 두 배라는 뜻이지, 자산보다 빚이 두 배 많다는 뜻이 아닙니다. 부채에는 대출 외의 여러 의무가 포함되고, 빚을 늘리지 않아도 자본이 줄면 비율은 올라갑니다.

이제 부채비율을 보면 숫자를 안전·위험으로 바로 나누기보다 **무슨 부채가 늘었는지, 자본은 왜 변했는지, 언제 갚아야 하는지**를 이어서 확인하려 합니다. 이익과 현금흐름을 공부한 것이 이 질문에도 연결됩니다.

다음 글에서는 **차입금과 순차입금**을 살펴보겠습니다. 빚이 많아 보여도 현금을 함께 가진 회사는 어떻게 읽는지, ‘순현금 기업’이라는 말은 무엇인지 이어가겠습니다.

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
