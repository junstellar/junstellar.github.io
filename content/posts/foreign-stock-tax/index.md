---
title: "서학개미의 5월 숙제 — 해외주식 양도소득세를 계산하는 법 · 계좌와 세금 교과서 ②"
description: "해외주식 양도소득세 22%와 연 250만원 기본공제, 여러 증권사의 손익통산을 계산기로 익힙니다. 결제일 기준 귀속연도와 다음 해 5월 신고·납부까지, 해외주식 세금 계산에 필요한 내용을 정리했습니다."
slug: "foreign-stock-tax"
date: 2026-09-17T20:00:00+09:00
draft: false
categories: ["AI 투자"]
tags: ["AI 투자", "계좌와 세금", "해외주식 양도소득세", "250만원 기본공제", "손익통산", "해외주식 세금 신고"]
---

<style>
.article-content{container-type:inline-size}
.tx2{--paper:#f5f2e9;--card:#fffdf7;--ink:#193b35;--muted:#586a61;--line:#cbd1c5;--green:#145c46;--lime:#dfec83;--orange:#b34828;--blue:#325c85;color:var(--ink);background:var(--paper);padding:30px;margin:34px 0;border:1px solid var(--line);border-radius:4px;line-height:1.65;word-break:keep-all;overflow-wrap:anywhere}
[data-scheme="dark"] .tx2{--paper:#26332d;--card:#303f37;--ink:#edf2e8;--muted:#bbcabf;--line:#56675c;--green:#97d1ac;--lime:#d5e989;--orange:#ffb39a;--blue:#abcdf0}
.tx2 *{box-sizing:border-box}.tx2 .eyebrow{font-size:11px;font-weight:800;letter-spacing:.13em;color:var(--green);margin:0 0 14px}.tx2 .tx-title{font-size:25px;font-weight:800;line-height:1.4;margin:0 0 12px;letter-spacing:-.04em}.tx2 p{margin:0}.tx2 .note{font-size:12px;color:var(--muted);margin:17px 0 0;line-height:1.7}.tx2 .grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:13px;margin-top:22px}.tx2 .tile{padding:20px;background:var(--card);border:1px solid var(--line);min-width:0}.tx2 .label{display:block;font-size:12px;color:var(--muted);margin-bottom:10px}.tx2 .value{font-size:28px;font-weight:850;letter-spacing:-.04em;line-height:1.35}.tx2 .value small{font-size:13px;font-weight:500;letter-spacing:0}.tx2 .tag{display:inline-block;font-size:12px;padding:3px 8px;border:1px solid var(--line);margin:12px 0 0}.tx2 .green{color:var(--green)}.tx2 .orange{color:var(--orange)}.tx2 .blue{color:var(--blue)}
.tx2-hero{display:grid;grid-template-columns:1.15fr 1fr;gap:24px;align-items:center;padding:36px 30px;background:var(--paper)}.tx2-hero .tx-title{font-size:35px;line-height:1.28;margin:18px 0;letter-spacing:-.055em}.tx2-hero .subtitle{font-size:15px;color:var(--muted)}.tx2 .receipt{background:var(--card);padding:24px 20px;border:1px solid var(--line);border-bottom:5px dotted var(--line);transform:rotate(2deg);box-shadow:5px 7px 0 var(--line)}.tx2 .receipt .row{display:flex;justify-content:space-between;gap:12px;font-size:13px;padding:10px 0;border-bottom:1px dashed var(--line)}.tx2 .receipt .total{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding-top:14px}.tx2 .receipt .total span{font-size:12px}.tx2 .receipt .total b{font-size:30px}.tx2 .band{padding:18px 20px;margin-top:20px;background:var(--card);border-left:4px solid var(--green);font-size:15px}.tx2 .strip{display:flex;height:30px;margin:23px 0 10px;overflow:hidden}.tx2 .exempt{width:31.25%;background:#b8ce73}.tx2 .taxbase{width:68.75%;background:#325c85}.tx2 .legend{display:flex;justify-content:space-between;gap:14px;font-size:12px;color:var(--muted)}.tx2 .ledger{margin-top:20px}.tx2 .ledger-row{display:flex;justify-content:space-between;gap:15px;padding:13px 0;border-bottom:1px solid var(--line);font-size:14px}.tx2 .ledger-row b{white-space:nowrap;font-variant-numeric:tabular-nums}.tx2 .ledger-row.final{border-top:2px solid var(--green);border-bottom:0;margin-top:10px;padding-top:20px;align-items:baseline}.tx2 .ledger-row.final b{font-size:32px;color:var(--green)}
.tx2 .controls{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:24px 0 18px}.tx2 label{font-size:13px;display:block}.tx2 label small{display:block;font-size:11px;color:var(--muted);margin:5px 0}.tx2 input{display:block;width:100%;min-width:0;border:1px solid var(--line);background:var(--card);color:var(--ink);font:inherit;font-size:20px;padding:10px 8px;border-radius:3px}.tx2 input:focus-visible,.tx2 button:focus-visible{outline:3px solid var(--orange);outline-offset:3px}.tx2 .presets{display:flex;gap:8px;flex-wrap:wrap}.tx2 button{font:inherit;font-size:12px;border:1px solid var(--line);padding:8px 11px;min-height:40px;color:var(--ink);background:var(--card);border-radius:20px;cursor:pointer}.tx2 button:hover{border-color:var(--green)}.tx2 .result{background:var(--card);padding:20px;margin-top:20px;border:1px solid var(--line)}.tx2 .result .ledger-row:first-child{padding-top:0}.tx2 .timeline{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:0;margin:25px 0 10px}.tx2 .moment{border-top:3px solid var(--green);padding:18px 16px 10px 0;min-width:0}.tx2 .moment .dot{display:block;width:13px;height:13px;border-radius:50%;background:var(--green);margin-top:-26px;margin-bottom:18px;border:2px solid var(--paper)}.tx2 .moment b{display:block;font-size:20px;line-height:1.5;margin-bottom:8px}.tx2 .moment p{font-size:13px;color:var(--muted)}
@media(max-width:600px){.tx2{padding:22px 18px;margin:28px 0}.tx2-hero{grid-template-columns:1fr;gap:20px}.tx2-hero .tx-title{font-size:31px}.tx2 .receipt{transform:none;margin:0 3px 5px 0}.tx2 .tx-title{font-size:23px}.tx2 .grid{grid-template-columns:1fr}.tx2 .controls{grid-template-columns:1fr;gap:15px}.tx2 label small{display:inline;margin-left:7px}.tx2 input{margin-top:6px}.tx2 .timeline{grid-template-columns:1fr}.tx2 .moment{border-top:0;border-left:3px solid var(--green);padding:0 0 25px 23px;margin-left:5px}.tx2 .moment .dot{margin:0 0 -16px -31px}.tx2 .moment b{padding-left:0}.tx2 .legend{flex-wrap:wrap}.tx2 .value{font-size:27px}}
@container(max-width:600px){.tx2{padding:22px 18px}.tx2-hero{grid-template-columns:1fr;gap:20px}.tx2-hero .tx-title{font-size:31px}.tx2 .receipt{transform:none;margin:0 3px 5px 0}.tx2 .grid{grid-template-columns:1fr}.tx2 .controls{grid-template-columns:1fr}.tx2 .timeline{grid-template-columns:1fr}.tx2 .moment{border-top:0;border-left:3px solid var(--green);padding:0 0 25px 23px;margin-left:5px}.tx2 .moment .dot{margin:0 0 -16px -31px}.tx2 .legend{flex-wrap:wrap}}
.tx2 .receipt b{white-space:nowrap}
</style>

<div class="tx2 tx2-hero">
<div><p class="eyebrow">ACCOUNT &amp; TAX / 02</p><p class="tx-title">계좌는 셋이어도,<br>세금 장부는<br>하나입니다.</p><p class="subtitle">흩어진 매매손익을 한 장에 모으는 법.<br>서학개미의 5월 숙제.</p></div>
<div class="receipt"><p class="eyebrow">한 사람의 연간 정산 / 예시</p><div class="row"><span>A증권사</span><b>+500만원</b></div><div class="row"><span>B증권사</span><b class="orange">-150만원</b></div><div class="row"><span>C증권사</span><b>+100만원</b></div><div class="row"><span>기본공제 · 한 번</span><b>-250만원</b></div><div class="total"><span>예상 세금</span><b class="green">44만원</b></div></div>
</div>

가계부를 세 권 쓴다고 한 달 생활비가 세 번 생기는 것은 아닙니다. 해외주식 세금도 비슷합니다. 증권사마다 흩어진 매매내역을 모아, 지난해 **매도로 확정한 손익을 한 사람의 장부로 결산**합니다. 그 장부를 신고하는 때가 다음 해 5월입니다.

문제는 대부분의 투자자가 여러 종목을 여러 증권사에서 사고판다는 점입니다. 엔비디아에서는 이익이 났지만 테슬라에서는 손실이 났고, A증권사에서는 팔았지만 B증권사에는 아직 보유 중일 수 있습니다. 이 숫자를 한 해의 장부로 합치는 것이 해외주식 양도소득세의 시작입니다.

이번 편에서는 세법 전체를 외우기보다, **무엇을 합치고 무엇을 빼며 언제 신고하는지**를 계산 순서로 보겠습니다. [1편의 계좌별 세후 수익 비교](/p/account-matters/)에서 한 걸음 더 들어가는 이야기입니다.

> 적용 범위: 국내에 계속 5년 이상 주소 또는 거소를 둔 거주자의 일반적인 해외주식·해외 상장 ETF 매매를 가정합니다. 이주·증여·한시적 세제 특례 등은 이번 계산에서 제외합니다.

## 01 아직 팔지 않은 이익에는 보통 세금이 붙지 않습니다

주가가 올랐다고 바로 양도소득세가 생기는 것은 아닙니다. 핵심 기준일은 **매도해서 양도차익이 확정된 날**입니다.

<div class="tx2" role="group" aria-label="양도소득에 포함되는 손익과 제외되는 손익">
<p class="eyebrow">FIGURE 01 / 장부에 넣을 숫자</p><p class="tx-title">앱의 수익률과 세금의 수익은 다릅니다.</p>
<div class="grid"><div class="tile"><span class="label">이익을 보고 매도</span><div class="value green">실현 이익</div><span class="tag">양도손익에 합산</span></div><div class="tile"><span class="label">손실을 보고 매도</span><div class="value orange">실현 손실</div><span class="tag">통산 대상이면 차감</span></div><div class="tile"><span class="label">가격은 변했지만 계속 보유</span><div class="value">평가손익</div><span class="tag">이번 양도손익에 미포함</span></div><div class="tile"><span class="label">보유 중 받은 배당금</span><div class="value blue">배당소득</div><span class="tag">양도소득과 별도 계산</span></div></div>
<p class="note">일반적인 주식 매매 기준입니다. 손실 상계에는 같은 과세연도·통산 대상이라는 조건이 붙습니다.</p>
</div>

따라서 화면에 표시된 평가손익과 세금 계산용 양도손익은 다를 수 있습니다. 해외주식 세금은 **평가의 문제가 아니라 실현의 문제**입니다.

연말에는 **주문일과 결제일이 다르다는 점**을 특히 확인하세요. 일반적인 해외주식 거래의 양도 시기는 대금이 청산되는 결제일을 기준으로 판단합니다. 12월 말에 주문했어도 결제가 다음 해라면 귀속연도가 달라질 수 있으므로, 이용 증권사의 시장별 연말 결제 일정을 확인해야 합니다.

## 02 계산 순서는 네 칸이면 됩니다

해외주식 양도소득세의 기본 구조는 다음과 같습니다.

> 양도소득금액 = 매도금액 - 취득금액 - 필요경비
>
> 과세표준 = 양도소득금액 - 기본공제 250만원 (음수이면 0)
>
> 산출세액 = 과세표준 × 22%

여기서 22%는 국세 20%와 지방소득세를 합친 일반적인 세율입니다. 실제 신고에서는 환율 적용일, 거래비용, 주식 종류와 납세자 요건에 따라 달라질 수 있으므로 아래 계산은 이해를 위한 단순 예시입니다.

### 가정으로 계산해보겠습니다

다음 조건을 가정하겠습니다.

- 2026년 한 해 동안 해외주식을 매도했습니다.
- 매도금액과 취득금액을 원화 기준으로 정리한 순이익은 800만원입니다.
- 다른 국내·국외 주식 양도손익은 없습니다.
- 필요경비와 개인별 특례는 단순화를 위해 제외합니다.

<div class="tx2" role="group" aria-label="양도소득 800만원에서 기본공제 250만원을 빼고 550만원에 22퍼센트를 적용하면 세금 121만원">
<p class="eyebrow">FIGURE 02 / 800만원의 계산서</p><p class="tx-title">22%를 곱하기 전에, 먼저 빼줍니다.</p>
<div class="strip" aria-hidden="true"><div class="exempt"></div><div class="taxbase"></div></div><div class="legend"><span>기본공제 250만원 / 31.25%</span><span>과세표준 550만원 / 68.75%</span></div>
<div class="ledger"><div class="ledger-row"><span>① 한 해 통산한 양도소득</span><b>800만원</b></div><div class="ledger-row"><span>② 기본공제</span><b>-250만원</b></div><div class="ledger-row"><span>③ 세율을 곱할 금액</span><b>550만원</b></div><div class="ledger-row final"><span>④ 550만원 × 22%</span><b>121만원</b></div></div><p class="note">국세 110만원 + 지방소득세 11만원. 다른 통산 대상 주식 손익·특례가 없는 예시입니다.</p>
</div>

800만원을 벌었다고 800만원 전체에 22%를 곱하는 것이 아닙니다. 먼저 250만원을 빼고, 남은 금액에 세율을 적용합니다.

## 03 250만원은 증권사마다 한 번씩 주는 쿠폰이 아닙니다

가장 흔한 오해가 있습니다.

> “A증권사에서 250만원, B증권사에서 250만원씩 공제받을 수 있나요?”

아닙니다. 기본공제는 증권사별이 아니라 **납세자 한 명의 한 과세연도 기준**입니다. 증권사를 세 곳 사용해도 해외주식 양도소득을 합산한 뒤 기본공제는 연 250만원을 한 번 적용합니다.

<div class="tx2" id="tx2-calculator">
<p class="eyebrow">FIGURE 03 / 내 손으로 합쳐보기</p><p class="tx-title">증권사를 더해도 공제는 한 번.</p><p style="font-size:14px;color:var(--muted)">같은 해 매도로 확정한 원화 손익을 넣어보세요. 손실은 음수로 입력합니다.</p>
<div class="controls"><label for="tx2-a">A증권사 <small>단위: 만원</small><input id="tx2-a" type="number" min="-1000000" max="1000000" step="any" value="500"></label><label for="tx2-b">B증권사 <small>단위: 만원</small><input id="tx2-b" type="number" min="-1000000" max="1000000" step="any" value="-150"></label><label for="tx2-c">C증권사 <small>단위: 만원</small><input id="tx2-c" type="number" min="-1000000" max="1000000" step="any" value="100"></label></div>
<div class="presets"><button type="button" data-tx2="500,-150,100">본문 예시</button><button type="button" data-tx2="250,250,0">두 곳에서 250만원씩</button><button type="button" data-tx2="500,-300,0">손실을 합치면?</button></div>
<div class="result" aria-live="polite" aria-atomic="true"><div class="ledger-row"><span>합친 양도손익</span><b id="tx2-sum">450만원</b></div><div class="ledger-row"><span>기본공제 후 과세표준</span><b id="tx2-base">200만원</b></div><div class="ledger-row final"><span>예상 세금 · 지방세 포함</span><b id="tx2-tax">44만원</b></div><p class="note" id="tx2-detail">국세 40만원 + 지방소득세 4만원</p></div>
<p class="note">기본공제 250만원을 전부 사용할 수 있는 일반적인 해외주식 매매의 학습용 계산입니다. 입력값은 필요경비를 반영한 원화 양도손익이며, 다른 과세 대상 국내주식·특례는 제외합니다. 세금이 0이라는 결과가 신고 의무 면제를 뜻하지는 않습니다. 입력값은 서버로 전송하지 않습니다.</p>
<noscript><p class="note">자바스크립트를 켜면 값을 바꿔 계산할 수 있습니다. 기본 예시: 500 - 150 + 100 = 450만원, (450 - 250) × 22% = 44만원.</p></noscript>
</div>

위 계산에서 A증권사의 500만원만 보고 세금을 계산하면 안 됩니다. 같은 과세연도에 발생한 통산 대상 양도손익을 먼저 합쳐야 합니다.

반대로 아직 팔지 않은 평가손실은 표에 넣을 수 없습니다. 손실을 세금 계산에 반영하려면 실제 매도로 손실을 확정해야 합니다. 그렇다고 세금만을 이유로 필요하지 않은 매매를 하라는 뜻은 아닙니다. 거래비용, 가격 변동, 투자 판단을 함께 고려해야 합니다.

## 04 국내주식 손실도 무조건 합쳐지는 것은 아닙니다

국세청은 일정한 과세 대상 국내주식과 국외주식 사이의 손익통산을 허용하고 있습니다. 하지만 **모든 국내주식 손익이 자동으로 해외주식과 합쳐지는 것은 아닙니다.**

예를 들어 국내 상장주식을 장내에서 매도한 소액주주의 일반적인 거래차익은 양도소득세 과세 대상이 아닙니다. 이런 비과세 국내주식 손실을 해외주식 이익에서 빼는 식으로 계산하면 안 됩니다.

반면 국내 비상장주식이나 과세 대상 국내주식의 양도손익은 요건에 따라 국외주식과 통산될 수 있습니다. 결국 확인해야 할 질문은 <strong>“양도소득세 과세 대상인 손익인가?”</strong>입니다.

## 05 신고는 다음 해 5월입니다

국외주식은 예정신고 의무가 없고, 양도한 다음 해 5월에 확정신고하는 구조입니다.

예를 들어 2026년 1월 1일부터 12월 31일까지 확정한 양도손익은 2027년 5월에 신고·납부합니다. 국세청의 확정신고 기간은 통상 5월 1일부터 5월 31일까지이며, 말일이 휴일이면 다음 영업일까지 연장될 수 있습니다.

<div class="tx2" role="group" aria-label="2026년 매도, 2027년 거래내역 취합, 2027년 5월 신고와 납부">
<p class="eyebrow">FIGURE 04 / 두 해에 걸친 일정</p><p class="tx-title">올해 판 주식, 내년 5월에 정산합니다.</p>
<div class="timeline"><div class="moment"><span class="dot" aria-hidden="true"></span><span class="label">손익을 확정하는 해</span><b>2026년<br>1월–12월</b><p>그해 귀속 양도손익을 합산합니다. 연말에는 결제일을 확인합니다.</p></div><div class="moment"><span class="dot" aria-hidden="true"></span><span class="label">자료를 모으는 때</span><b>2027년<br>신고 전</b><p>모든 증권사의 계산자료를 모으고, 빠진 거래가 없는지 살펴봅니다.</p></div><div class="moment"><span class="dot" aria-hidden="true"></span><span class="label">신고와 납부</span><b>2027년<br>5월</b><p>국세와 지방소득세 신고·납부를 각각 확인합니다.</p></div></div>
<p class="note">국외주식은 예정신고가 면제됩니다. 법정 확정신고 기간은 다음 해 5월 1일–31일이며, 휴일 등 기한 특례와 해당 연도 공지를 확인하세요.</p>
</div>

신고 대상인데 신고하지 않으면 무신고·납부지연 가산세 문제가 생길 수 있습니다. 금액이 작아 보인다고 신고 의무가 사라지는 것은 아닙니다. 정확한 신고기한과 가산세는 신고 시점의 국세청 안내를 확인해야 합니다.

## 06 여러 증권사를 쓴 사람의 실제 준비 순서

5월이 되어 홈택스부터 열면 오히려 어렵습니다. 연초에 다음 순서로 자료를 모아두는 편이 낫습니다.

### 1. 모든 증권사의 연간 거래내역을 받습니다

증권사 앱이나 홈페이지에서 해외주식 양도소득금액 계산자료, 거래내역, 손익계산서 중 해당 메뉴를 찾습니다. 증권사마다 명칭과 제공 시점이 다를 수 있으므로 한 곳의 자료만 보고 끝내면 안 됩니다.

### 2. 매도한 종목만 추립니다

보유 중인 평가손익과 배당금은 양도소득 계산표에서 분리합니다. 매도한 종목의 취득가액, 양도가액, 수수료, 환율 적용 내역을 확인합니다.

### 3. 증권사별 금액을 한 장부로 합칩니다

A증권사의 이익과 B증권사의 손실을 따로 신고하는 것이 아닙니다. 같은 납세자의 같은 과세연도 양도손익으로 합쳐 기본공제를 한 번 적용합니다.

### 4. 증권사 계산값을 그대로 복사하지 말고 비교합니다

증권사마다 환율 적용 방식이나 거래비용 표시 방식이 달라 보일 수 있습니다. 차이가 있으면 거래내역 원문과 계산 기준을 확인하고, 해결되지 않으면 국세청이나 세무 전문가에게 문의합니다.

### 5. 신고 후 납부까지 확인합니다

양도소득세 신고와 납부는 별개의 절차입니다. 신고서를 제출한 뒤에는 **국세뿐 아니라 개인지방소득세도 신고·납부했는지** 확인하세요. 증권사의 신고 대행을 이용했다면 대행 범위와 본인이 납부할 항목을 확인하는 것이 좋습니다.

## 07 연말에 손실 종목을 팔면 절세인가요?

수익 난 종목과 손실 난 종목을 같은 해에 매도하면 통산 대상 양도손익이 줄어 세금이 낮아질 수 있습니다. 하지만 이것은 “세금이 줄어드니 무조건 팔자”는 공식이 아닙니다.

손실 종목을 팔고 곧바로 다시 사는 전략은 가격 변동과 거래비용, 투자 판단의 문제를 동반합니다. 손실을 확정한 뒤에도 그 종목을 계속 보유하고 싶은지, 매도와 재매수 사이의 시장 위험을 감당할 수 있는지 먼저 물어야 합니다.

절세는 투자의 목적이 아니라 **투자 결과를 정리하는 방법 중 하나**입니다. 세금 22만원을 줄이려다가 투자 판단에서 더 큰 손실을 만들면 계산의 의미가 사라집니다.

## 정리

- 해외주식 양도소득세는 주가가 오른 시점이 아니라 **매도해 이익이 확정된 시점**을 기준으로 계산합니다.
- 한 해의 양도손익을 합친 뒤 **250만원 기본공제**를 한 번 적용합니다. 증권사마다 따로 공제받는 쿠폰이 아닙니다.
- 일반적인 외국법인 주식 양도차익은 기본공제 초과분에 국세와 지방소득세를 합쳐 <strong>22%</strong>를 적용합니다.
- 다른 증권사의 손실도 같은 과세연도의 통산 대상이라면 합칠 수 있지만, 평가손실은 합칠 수 없습니다.
- 국내주식 손실도 모두 해외주식 이익과 합쳐지는 것은 아닙니다. **양도소득세 과세 대상인지**를 확인해야 합니다.
- 국외주식은 예정신고 없이 다음 해 5월에 확정신고·납부합니다.
- 5월 전에 모든 증권사의 거래내역을 모아 하나의 장부로 합치는 것이 가장 중요합니다.

앞 편 [「500만원 벌었는데, 내 돈은 얼마일까?」](/p/account-matters/)에서는 같은 수익이라도 계좌에 따라 손에 남는 돈이 달라지는 이유를 살펴봤습니다. 이번 편의 결론은 그 계산표를 직접 만드는 법입니다. 다음 편에서는 이 구조 위에 **2026년 ISA 제도 개편**이 무엇을 더하고 무엇을 없애는지 확인하겠습니다.

## 계산의 근거

자료 확인: **2026년 9월 17일.** 세법은 개정될 수 있으므로 실제 신고 때는 해당 귀속연도의 국세청 안내와 법령을 다시 확인해야 합니다.

1. [국세청 세액계산요령 — 국외주식 과세 및 국내·국외주식 손익통산](https://g.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&mi=12274)
2. [국세청 양도소득세 법정 신고기한 — 국외주식 확정신고](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=7708&mi=2315)
3. [국세청 국외주식 관련 주요 Q&A — 확정신고 대상과 홈택스 신고·납부](https://www.nts.go.kr/nts/na/ntt/selectNttInfo.do?nttSn=1350890)
4. [삼성증권 해외주식 양도소득세 안내](https://www.samsungpop.com/ux/kor/trading/overseasStock/overseasStockDealGuide/transferTax.do) — 계산 예시·원화 환산 설명 참고. 이 페이지의 국내·국외주식 손익통산 불가 문구는 국세청의 2020년 이후 안내와 달라, 통산 범위는 위 국세청 자료를 따랐습니다.

<script>
(function(){var root=document.getElementById('tx2-calculator');if(!root)return;var fields=['tx2-a','tx2-b','tx2-c'].map(function(id){return document.getElementById(id)});var fmt=new Intl.NumberFormat('ko-KR',{maximumFractionDigits:4});function money(v){return fmt.format(v)+'만원'}function update(){var valid=fields.every(function(el){return el.value.trim()!==''&&el.validity.valid&&Number.isFinite(el.valueAsNumber)});if(!valid){['tx2-sum','tx2-base','tx2-tax'].forEach(function(id){document.getElementById(id).textContent='입력 확인'});document.getElementById('tx2-detail').textContent='세 칸에 범위 내 숫자를 입력해주세요. 거래가 없으면 0을 입력하세요.';return}var sum=fields.reduce(function(acc,el){return acc+el.valueAsNumber},0);var base=Math.max(sum-250,0);document.getElementById('tx2-sum').textContent=money(sum);document.getElementById('tx2-base').textContent=money(base);document.getElementById('tx2-tax').textContent=money(base*.22);document.getElementById('tx2-detail').textContent=base===0?'기본공제 후 과세표준이 0입니다. 신고 의무는 별도로 확인하세요.':'국세 '+money(base*.2)+' + 지방소득세 '+money(base*.02)}fields.forEach(function(el){el.addEventListener('input',update)});root.querySelectorAll('[data-tx2]').forEach(function(button){button.addEventListener('click',function(){button.dataset.tx2.split(',').forEach(function(value,i){fields[i].value=value});update()})});update()})();
</script>

> ⚠️ 이 글은 개인 학습을 위한 설명이며 세무 자문이 아닙니다. 본문의 계산은 특정 조건을 가정한 예시이며, 환율·거래비용·상품 유형·개인별 손익에 따라 실제 결과가 달라질 수 있습니다. 세법과 시행령은 개정될 수 있으므로 실제 신고 전 국세청 또는 세무 전문가에게 확인하시기 바랍니다. 투자 판단과 신고 의무 이행은 본인의 몫입니다.
