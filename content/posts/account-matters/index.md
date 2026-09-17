---
title: "500만원 벌었는데, 내 돈은 얼마일까? · 계좌와 세금 교과서 ①"
description: "국내 상장 해외 ETF·미국 상장 ETF·ISA의 세금을 비교합니다. 수익 500만원의 세후 금액, 250만원 기본공제와 ISA 비과세 차이를 계산기로 확인하고 절세 계좌를 고르는 기준을 알아보세요."
slug: "account-matters"
date: 2026-09-16T20:00:00+09:00
draft: false
image: "tax-series-1-cover.png"
categories: ["AI 투자"]
tags: ["AI 투자", "계좌와 세금", "ISA", "ETF 세금", "절세 계좌", "해외주식 양도소득세"]
---

<style>
.taxfig{--tf-ink:#193b35;--tf-sub:#586a61;--tf-line:#cbd1c5;--tf-green:#145c46;--tf-lime:#dfec83;--tf-paper:#e9ece0;--tf-card:#fffdf7;--tf-blue:#325c85;--tf-red:#b34828;--tf-finish:#145c46;--tf-finish-ink:#fffdf7;color:var(--tf-ink);margin:2.2em 0;line-height:1.8;word-break:keep-all}
[data-scheme="dark"] .taxfig{--tf-ink:#e8ede6;--tf-sub:#9fb0a6;--tf-line:#44514a;--tf-green:#6fbf9c;--tf-lime:#c9dd6b;--tf-paper:#2f3a35;--tf-card:#26302b;--tf-blue:#7aa9d8;--tf-red:#e0846a;--tf-finish:#17503e;--tf-finish-ink:#eaf5ee}
.taxfig *{box-sizing:border-box}
.taxfig .tf-box{background:var(--tf-card);border:1px solid var(--tf-line);border-radius:10px;padding:26px 28px}
.taxfig .tf-head{display:flex;justify-content:space-between;gap:14px;align-items:baseline;margin-bottom:20px;flex-wrap:wrap}
.taxfig .tf-head h4{margin:0;font-size:1.05em;font-weight:800}
.taxfig .tf-unit{font-size:.78em;color:var(--tf-sub)}
.taxfig .tf-bar{margin:18px 0}
.taxfig .tf-barlab{display:flex;justify-content:space-between;gap:12px;font-size:.86em;margin-bottom:7px}
.taxfig .tf-barlab strong{font-size:1.28em}
.taxfig .tf-barlab small{display:block;font-size:.85em;color:var(--tf-sub)}
.taxfig .tf-track{height:22px;display:flex;overflow:hidden;border-radius:3px;background:var(--tf-paper)}
.taxfig .tf-net{background:var(--tf-red);height:100%}
.taxfig .tf-bar.us .tf-net{background:var(--tf-blue)}
.taxfig .tf-bar.isa .tf-net{background:var(--tf-green)}
.taxfig .tf-tax{height:100%;background:repeating-linear-gradient(135deg,#c36445 0,#c36445 3px,#efd7c9 3px,#efd7c9 7px)}
.taxfig .tf-legend{display:flex;gap:18px;font-size:.78em;color:var(--tf-sub);margin-top:16px;flex-wrap:wrap}
.taxfig .tf-dot{width:11px;height:11px;display:inline-block;background:var(--tf-green);margin-right:5px;vertical-align:middle}
.taxfig .tf-dot.tax{background:#c36445}
.taxfig .tf-diff{margin-top:22px;padding-top:18px;border-top:1px solid var(--tf-line);display:flex;align-items:center;gap:20px;flex-wrap:wrap}
.taxfig .tf-diff b{font-size:2.2em;letter-spacing:-.04em;line-height:1.1;white-space:nowrap}
.taxfig .tf-diff p{margin:0;font-size:.86em}
.taxfig .tf-grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.taxfig .tf-tag{font-size:.72em;letter-spacing:.05em;color:var(--tf-sub);display:block}
.taxfig .tf-card h4{margin:7px 0 18px;font-size:1em}
.taxfig .tf-line{display:flex;justify-content:space-between;gap:10px;font-size:.84em;padding:8px 0}
.taxfig .tf-line b{font-size:1.15em;white-space:nowrap}
.taxfig .tf-line.ded b{color:var(--tf-green)}
.taxfig .tf-line.base{border-top:1px solid var(--tf-line)}
.taxfig .tf-res{margin-top:12px;padding-top:13px;border-top:2px solid var(--tf-ink);display:flex;justify-content:space-between;align-items:center;font-size:.84em}
.taxfig .tf-res b{font-size:1.85em;letter-spacing:-.03em}
.taxfig .tf-note{font-size:.8em;color:var(--tf-sub);margin:12px 0 0;line-height:1.65}
.taxfig .tf-assume{border-left:3px solid var(--tf-green);padding:14px 18px;background:var(--tf-paper);border-radius:0 8px 8px 0;margin:22px 0;font-size:.85em}
.taxfig .tf-assume b{display:block;margin-bottom:5px}
.taxfig .tf-assume p{margin:0}
.taxfig .tf-pull{font-size:1.45em;line-height:1.55;font-weight:800;letter-spacing:-.02em;border-top:2px solid var(--tf-green);padding-top:20px;margin:30px 0}
.taxfig .tf-lab{background:var(--tf-paper);border:1px solid var(--tf-line);border-radius:10px;padding:26px 28px}
.taxfig .tf-labtop{display:flex;justify-content:space-between;gap:16px;align-items:baseline;flex-wrap:wrap}
.taxfig .tf-labtop h4{margin:0;font-size:1.05em;font-weight:800}
.taxfig .tf-amt{font-size:1.9em;font-weight:900;white-space:nowrap}
.taxfig .tf-amt small{font-size:.5em}
.taxfig input[type=range]{display:block;width:100%;margin:20px 0 8px;accent-color:var(--tf-green);height:26px}
.taxfig .tf-rlab{display:flex;justify-content:space-between;font-size:.78em;color:var(--tf-sub)}
.taxfig .tf-presets{display:flex;gap:8px;flex-wrap:wrap;margin:16px 0 22px}
.taxfig .tf-presets button{background:transparent;border:1px solid var(--tf-sub);border-radius:30px;padding:5px 15px;font:inherit;font-size:.84em;color:var(--tf-ink);cursor:pointer}
.taxfig .tf-presets button[aria-pressed=true]{background:var(--tf-ink);color:var(--tf-card)}
.taxfig .tf-out{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.taxfig .tf-out div{border-top:2px solid var(--tf-ink);padding-top:11px}
.taxfig .tf-out span{display:block;font-size:.78em;min-height:3.2em}
.taxfig .tf-out b{font-size:1.6em}
.taxfig .tf-out small{font-size:.78em}
.taxfig .tf-insight{font-size:.92em;margin:20px 0 0;line-height:1.75}
.taxfig .tf-check{display:grid;grid-template-columns:42px 1fr;gap:14px;padding:24px 0;border-top:1px solid var(--tf-line)}
.taxfig .tf-check:last-child{border-bottom:1px solid var(--tf-line)}
.taxfig .tf-num{font-size:1.7em;color:var(--tf-green);font-weight:900;line-height:1.2}
.taxfig .tf-check h4{margin:0 0 8px;font-size:1.05em}
.taxfig .tf-check p{margin:0;font-size:.92em}
.taxfig .tf-acc{border-top:1px solid var(--tf-ink)}
.taxfig .tf-accrow{display:grid;grid-template-columns:160px 1fr;gap:22px;padding:20px 0;border-bottom:1px solid var(--tf-line)}
.taxfig .tf-accrow h4{margin:0;font-size:1.02em}
.taxfig .tf-accrow small{color:var(--tf-sub);font-size:.8em}
.taxfig .tf-accrow p{margin:0;font-size:.9em}
.taxfig .tf-finish{background:var(--tf-finish);color:var(--tf-finish-ink);border-radius:10px;padding:34px 36px;margin:34px 0}
.taxfig .tf-finish p{margin:0;font-size:1.28em;line-height:1.75;letter-spacing:-.02em}
.taxfig .tf-finish strong{color:var(--tf-lime)}
@media(max-width:760px){.taxfig .tf-grid3,.taxfig .tf-out{grid-template-columns:1fr}.taxfig .tf-box,.taxfig .tf-lab{padding:20px 18px}.taxfig .tf-accrow{grid-template-columns:1fr;gap:6px}.taxfig .tf-pull{font-size:1.2em}.taxfig .tf-finish{padding:24px 22px}.taxfig .tf-finish p{font-size:1.1em}.taxfig .tf-out span{min-height:0}}
</style>

매도 버튼을 눌렀습니다. 수익은 **+500만원**.

이제 500만원을 쓸 수 있을까요?

아직 계산이 하나 남았습니다. **세금**입니다. 어떤 ETF를 어느 계좌에서 샀는지에 따라, 같은 500만원에서도 손에 남는 돈이 달라집니다.

앞선 45편에서는 무엇을 살지 고민했습니다. [반도체](/p/what-is-hbm/), 전력, 지수, 순환매, [금리](/p/how-to-read-rates/), [로봇](/p/what-is-physical-ai/)까지. 이번 시리즈는 매수 화면에서 종목 이름 옆에 있는, 평소엔 그냥 넘겼던 항목을 봅니다.

**계좌 선택.** 별것 아닌 설정처럼 보이지만, 수익의 마지막 숫자를 바꿉니다.

## 47만 3천원은 어디서 사라졌을까

같은 미국 지수를 따라가는 ETF에 투자해 **세전 매매차익 500만원**을 얻었다고 해봅시다. 국내 상장 ETF를 일반계좌에서 샀다면 세금은 77만원, 일반형 ISA에서 샀다면 29만 7천원입니다.

**같은 국내 상장 ETF인데 계좌만 바꿔도 47만 3천원이 달라집니다.** 여기에 미국 상장 ETF를 일반계좌에서 산 경우까지 나란히 놓아보겠습니다.

<div class="taxfig">
<div class="tf-assume"><b>이 비교의 약속</b><p>한국 거주 개인의 단순 예시입니다. 분배금 없이 세전 매매차익 500만원을 마지막 한 과세연도에 전부 실현하며, 국내 상장 ETF의 과세대상 이익도 500만원이라고 가정합니다. 다른 금융소득·주식 양도손익은 없고 연 250만원 기본공제를 전부 쓸 수 있습니다. ISA는 일반형으로 3년 이상 유지한 뒤 해지·정산하며, 계좌 전체의 누적 과세대상 순이익이 500만원입니다. 수수료·환율·추적오차에 따른 상품 간 차이는 제외했고, 세율은 지방소득세 포함입니다.</p></div>
<div class="tf-box">
<div class="tf-head"><h4>500만원을 세후 수익과 세금으로 나누면</h4><span class="tf-unit">막대 전체 = 세전 매매차익 500만원</span></div>
<div class="tf-bar"><div class="tf-barlab"><span>국내 상장 해외 ETF<small>일반계좌</small></span><span><strong>423만원</strong><small>세금 77만원</small></span></div><div class="tf-track"><div class="tf-net" style="width:84.6%"></div><div class="tf-tax" style="width:15.4%"></div></div></div>
<div class="tf-bar us"><div class="tf-barlab"><span>미국 상장 ETF<small>일반계좌</small></span><span><strong>445만원</strong><small>세금 55만원</small></span></div><div class="tf-track"><div class="tf-net" style="width:89%"></div><div class="tf-tax" style="width:11%"></div></div></div>
<div class="tf-bar isa"><div class="tf-barlab"><span>국내 상장 해외 ETF<small>일반형 ISA</small></span><span><strong>470.3만원</strong><small>세금 29.7만원</small></span></div><div class="tf-track"><div class="tf-net" style="width:94.06%"></div><div class="tf-tax" style="width:5.94%"></div></div></div>
<div class="tf-legend"><span><i class="tf-dot"></i>단색 = 세후 수익</span><span><i class="tf-dot tax"></i>빗금 = 세금</span></div>
<div class="tf-diff"><b>47.3만원</b><p>이 예시의 최대 세후 수익 차이.<br>세전 이익 500만원의 약 9.5%입니다.</p></div>
<p class="tf-note">원금을 포함한 계좌 잔액이 아니라 ‘수익 중 남는 금액’입니다. 투자수익률이 9.5%포인트 높아진다는 뜻은 아닙니다.</p>
</div>
</div>

여기에는 **두 가지 비교가 섞여 있습니다.** 국내 상장 ETF의 일반계좌와 ISA를 비교하면 **계좌의 차이**가 보이고, 일반계좌에서 국내 상장 ETF와 미국 상장 ETF를 비교하면 **상품의 과세 방식 차이**가 보입니다.

같은 지수를 따라가도 같은 상품은 아닙니다. "무엇을 따라가는가"만큼 **"어떤 상품을 어디에 담았는가"가** 중요한 이유입니다.

## 15.4%가 22%보다 세금을 더 낸다고?

일반계좌 두 개만 보겠습니다. 국내 상장 해외 ETF에는 **15.4%**, 미국 상장 ETF 매매차익에는 **22%가** 적용됩니다. 숫자만 보면 15.4% 쪽이 유리해 보입니다.

그런데 세금은 **77만원 대 55만원**입니다. **이 예시에서는 낮은 세율 쪽이 22만원을 더 냅니다.**

세율을 곱하기 전에 **빼주는 금액**이 다르기 때문입니다.

<div class="taxfig">
<div class="tf-grid3">
<div class="tf-box tf-card"><span class="tf-tag">국내 상장 해외 ETF · 일반계좌</span><h4>공제 없이 계산</h4><div class="tf-line"><span>세전 이익</span><b>500만원</b></div><div class="tf-line ded"><span>빼주는 금액</span><b>없음</b></div><div class="tf-line base"><span>과세대상</span><b>500만원</b></div><div class="tf-line"><span>적용 세율</span><b>× 15.4%</b></div><div class="tf-res"><span>세금</span><b>77만원</b></div><p class="tf-note">전체 이익 대비 15.4%.<br>과세대상 이익이 매매차익과 같다는 가정입니다.</p></div>
<div class="tf-box tf-card"><span class="tf-tag">미국 상장 ETF · 일반계좌</span><h4>250만원을 빼고 계산</h4><div class="tf-line"><span>세전 이익</span><b>500만원</b></div><div class="tf-line ded"><span>연 기본공제</span><b>− 250만원</b></div><div class="tf-line base"><span>과세대상</span><b>250만원</b></div><div class="tf-line"><span>적용 세율</span><b>× 22%</b></div><div class="tf-res"><span>세금</span><b>55만원</b></div><p class="tf-note">전체 이익 대비 11%.<br>공제는 종목마다·계좌마다 따로 주어지지 않습니다.</p></div>
<div class="tf-box tf-card"><span class="tf-tag">국내 상장 해외 ETF · 일반형 ISA</span><h4>200만원까지 비과세</h4><div class="tf-line"><span>누적 순이익</span><b>500만원</b></div><div class="tf-line ded"><span>비과세 한도</span><b>− 200만원</b></div><div class="tf-line base"><span>초과분</span><b>300만원</b></div><div class="tf-line"><span>적용 세율</span><b>× 9.9%</b></div><div class="tf-res"><span>세금</span><b>29.7만원</b></div><p class="tf-note">전체 이익 대비 5.94%.<br>200만원은 매년 새로 생기는 한도가 아닙니다.</p></div>
</div>
<p class="tf-pull">세율은 마지막 곱셈입니다.<br>먼저 봐야 할 것은 ‘얼마에 곱하는가’입니다.</p>
</div>

미국 상장 ETF의 매매차익은 **양도소득**으로, 국내 상장 해외 ETF의 과세대상 매매차익은 **배당소득**으로 다룹니다. 같은 미국 지수에서 번 돈이라도 세법상 이름이 달라지면 계산법이 달라집니다.

그리고 한 가지 주의할 점이 있습니다. 국내 상장 ETF는 **보유기간 과세 구조**라서, 실제 세금이 단순히 "매매차익 × 15.4%"와 다를 수 있습니다. 위 계산은 과세대상 이익이 매매차익과 같다고 가정한 것입니다.

## 그럼 ISA가 늘 유리할까

500만원짜리 표 하나로는 답할 수 없습니다. **금액을 바꾸면 순위가 바뀝니다.** 아래 막대를 직접 움직여 보세요.

<div class="taxfig">
<div class="tf-lab">
<div class="tf-labtop"><h4><label for="tf-profit">세전 매매차익을 바꿔보세요</label></h4><output for="tf-profit" class="tf-amt" id="tf-amount">500 <small>만원</small></output></div>
<input id="tf-profit" type="range" min="100" max="1500" step="10" value="500">
<div class="tf-rlab"><span>100만원</span><span>1,500만원</span></div>
<div class="tf-presets"><button type="button" data-tfv="250" aria-pressed="false">250만원</button><button type="button" data-tfv="500" aria-pressed="true">500만원</button><button type="button" data-tfv="1000" aria-pressed="false">1,000만원</button></div>
<div class="tf-out" aria-live="polite"><div><span>국내 상장 해외 ETF<br>일반계좌 · 세후 수익</span><b id="tf-dom">423</b> <small>만원</small></div><div><span>미국 상장 ETF<br>일반계좌 · 세후 수익</span><b id="tf-us">445</b> <small>만원</small></div><div><span>국내 상장 해외 ETF<br>일반형 ISA · 세후 수익</span><b id="tf-isa">470.3</b> <small>만원</small></div></div>
<p class="tf-insight" id="tf-insight">500만원에서는 일반형 ISA의 세후 수익이 가장 큽니다. 일반계좌끼리는 250만원 기본공제를 쓰는 미국 상장 ETF가 앞섭니다.</p>
<p class="tf-note">계산식(단위 만원) — 국내 일반 = 이익 × 84.6% / 미국 일반 = 이익 − max(이익 − 250, 0) × 22% / 일반형 ISA = 이익 − max(이익 − 200, 0) × 9.9%. 매매차익 전액이 과세대상인 가정이며 분배금·다른 소득·손실·비용을 반영하지 않은 학습용 비교입니다.</p>
</div>
</div>

**250만원에서는 미국 상장 ETF의 양도소득세가 0원입니다.** 기본공제 안에 들어가니까요.

**1,000만원에서는 일반계좌끼리의 순위가 뒤집힙니다.** 국내 상장 해외 ETF가 846만원, 미국 상장 ETF가 835만원입니다. 정해진 250만원 공제가 수익 전체에서 차지하는 비중이 줄어들기 때문입니다.

### 금액만 변수가 아닙니다 — 언제 실현했는지도 바뀝니다

미국 상장 ETF에서 다른 주식 양도손익 없이 기본공제를 전부 쓸 수 있다고 해봅시다.

| 어떻게 실현했나 | 세금 |
|---|---|
| 한 과세연도에 500만원을 한 번에 | **55만원** |
| 두 과세연도에 250만원씩 나눠서 | **0원** |

같은 500만원인데 **파는 시점만 나눴을 뿐**입니다. 기본공제가 **해마다** 주어지기 때문입니다.

> 이건 실현 시점만 바꾼 별도 예시입니다. 실제로 원하는 가격에 나눠 매도할 수 있다는 보장은 없고 거래비용도 제외했습니다. 그리고 **ISA의 200만원 비과세 한도는 가입기간 전체 기준**입니다. "연간 공제"와 "계좌 전체 비과세"를 같은 시계로 읽으면 안 됩니다.

**계좌에는 영구적인 등수가 없습니다.** 얼마를 벌었는지, 언제 실현했는지, 공제가 남았는지를 넣어야 내 계산이 됩니다.

## 매수 전에 확인할 세 가지

모든 세법을 외울 필요는 없습니다. 세 가지 질문으로 시작하면 됩니다.

<div class="taxfig">
<div class="tf-check"><div class="tf-num">1</div><div><h4>빼주는 금액이 있나?</h4><p>250만원 기본공제나 ISA의 비과세 한도처럼, 세금을 계산하기 전에 제외하는 금액이 있는지 봅니다. <b>그 한도가 매년인지, 가입기간 전체인지</b>도 함께 확인합니다.</p></div></div>
<div class="tf-check"><div class="tf-num">2</div><div><h4>손실도 같이 계산해주나?</h4><p>통산 가능한 상품 A에서 300만원을 벌고 B에서 100만원을 잃었다면, ISA에서는 합친 순이익 200만원을 기준으로 계산할 수 있습니다. <b>해외주식은 일반계좌에서도</b> 같은 과세연도의 통산 대상 양도손익을 합칩니다. 반면 일반계좌의 국내 상장 해외 ETF는 다른 ETF의 손실을 이렇게 상계하지 못합니다. 다만 ISA도 상품마다 통산 대상 범위가 달라, 계좌 안의 모든 손실이 무조건 합쳐진다고 읽으면 안 됩니다.</p></div></div>
<div class="tf-check"><div class="tf-num">3</div><div><h4>다른 소득과 합쳐지나?</h4><p>국내 상장 해외 ETF의 과세대상 매매차익은 <b>배당소득</b>이라 금융소득종합과세 판단에 들어갑니다. 이자·배당소득 합계가 연 2,000만원을 넘는 경우를 살펴야 합니다. 반면 해외주식 양도소득은 종합소득과 별도로 계산하고, ISA의 비과세 한도 초과분은 분리과세합니다.</p></div></div>
</div>

세율만 적힌 비교표를 만나면, **이 세 질문이 빠져 있는지부터** 보세요.

## 절세도 중요하지만, 언제 쓸 돈인가요

내년에 쓸 돈과 은퇴 후에 쓸 돈은 다릅니다. **세금만 줄였다가 필요한 때에 꺼내기 불편해진다면, 계좌를 잘 골랐다고 하기 어렵습니다.**

<div class="taxfig">
<div class="tf-acc">
<div class="tf-accrow"><div><h4>일반계좌</h4><small>상품별 과세 방식 확인</small></div><p>해외주식·ETF 직접 투자에 쓸 수 있습니다. 절세계좌의 의무가입기간은 없지만, 매매차익과 분배금에 붙는 세금은 상품마다 다릅니다.</p></div>
<div class="tf-accrow"><div><h4>중개형 ISA</h4><small>3년 이상 유지 가능하다면</small></div><p>국내 상장 ETF로 해외 지수에 투자할 수 있습니다. <b>미국 상장 주식·ETF를 직접 살 수는 없습니다.</b> 일반형은 손익통산 후 200만원까지 비과세, 초과분은 9.9%로 분리과세합니다.</p></div>
<div class="tf-accrow"><div><h4>연금저축 · IRP</h4><small>노후자금이라면</small></div><p>납입 시 세액공제와 운용 중 과세이연을 활용합니다. 다만 연금 외 인출에는 세금 부담이 생길 수 있고 IRP의 중도인출 사유는 제한됩니다. <b>연금저축과 IRP의 인출 규칙은 같지 않습니다.</b></p></div>
</div>
</div>

연금계좌의 인출 조건과 한시 특례, 새로 생기는 제도는 해당 편에서 따로 보겠습니다. 이번 편의 핵심은 계좌를 전부 외우는 게 아니라 **계좌 선택에도 조건이 붙는다는 것**을 아는 데 있습니다.

## 정리

- **같은 세전 500만원이라도 세후 금액이 다릅니다.** 국내 상장 해외 ETF 일반계좌 **423만원**, 미국 상장 ETF 일반계좌 **445만원**, 일반형 ISA **470.3만원**. 최대 차이 **47.3만원**(약 9.5%)입니다.
- **세율이 낮은 쪽이 세금을 더 낼 수 있습니다.** 15.4%가 77만원, 22%가 55만원이었습니다. **세율을 곱하기 전에 빼주는 금액**이 다르기 때문입니다.
- **소득의 이름이 다릅니다.** 미국 상장 ETF 매매차익은 **양도소득**, 국내 상장 해외 ETF의 과세대상 매매차익은 **배당소득**입니다.
- **금액이 바뀌면 순위가 바뀝니다.** 250만원에서는 미국 상장 ETF 세금이 0원이고, 1,000만원에서는 일반계좌끼리 국내 상장 해외 ETF가 역전합니다.
- **실현 시점도 변수입니다.** 500만원을 한 해에 실현하면 55만원, 두 해에 250만원씩 나누면 0원입니다. 기본공제는 해마다 주어집니다. **반면 ISA의 200만원은 가입기간 전체 기준입니다.**
- **매수 전 세 가지를 확인하세요.** ①빼주는 금액이 있나 ②손실도 같이 계산해주나 ③다른 소득과 합쳐지나.
- **절세만 보지 마세요.** 언제 쓸 돈인지가 계좌 선택의 절반입니다.

<div class="taxfig">
<div class="tf-finish"><p>“얼마 오를까?”를 고민했다면,<br>매수 전에 한 번 더 물어보세요.<br><strong>“이 상품을 이 계좌에서 사면, 내 손에는 얼마가 남을까?”</strong></p></div>
</div>

다음 편은 **서학개미의 5월 숙제**입니다. 250만원 공제는 누구 기준일까요? 증권사를 두 곳 쓰면 두 번 받을까요? 해외주식 양도소득세의 계산부터 신고까지 이어가겠습니다.

## 계산의 근거

자료 확인: **2026년 9월 16일.** 아래는 이 글의 계산과 제도 설명에 사용한 자료입니다. 발표된 개편안과 시행 중인 제도는 구분하며, 실제 거래에는 해당 시점의 법령과 적용 요건을 확인해야 합니다.

1. **국내 상장 ETF 과세** — [삼성자산운용 투자설명서](https://m.samsungfund.com/upload/invest/2ETF63-A.pdf)의 과세 항목. 매매차익과 과표증분 등을 비교하는 **보유기간 과세 구조**, 배당소득세와 금융소득종합과세 설명. 실제 세금은 매매차익에 15.4%를 곱한 값과 다를 수 있습니다.
2. **해외주식 양도소득** — [국세청 세액계산요령](https://www.nts.go.kr/nts/cm/cntnts/cntntsView.do?cntntsId=8800&mi=12274), [삼성증권 해외주식 거래 안내](https://samsungpop.com/mbw/trading/foreignStock/tradingGuide.pop). 통산 대상 국내·국외 주식 양도소득을 합산해 연 250만원 공제. 일반적인 외국법인 주식 양도차익 세율은 국세 20%에 지방소득세를 더해 **22%가 됩니다.**
3. **ISA** — [신한투자증권 ISA 안내](https://m.shinhansec.com/mweb/fnin/fisa/ffisa1001), [삼성증권 ISA 안내](https://www.samsungpop.com/mbw/finance/isa/guide.pop). 일반형 비과세 200만원, 초과분 9.9%, 의무가입기간 3년과 투자 가능 상품. 상품마다 통산 대상 손익의 범위가 다릅니다.
4. **연금계좌 인출** — [삼성자산운용 연금투자 가이드북](https://m.samsungfund.com/upload/kodex/newsroom/20250722174437650.pdf), [삼성증권 IRP 안내](https://www.samsungpop.com/mbw/finance/irp.do?cmd=guide&tabInfo=tab2). 세액공제를 받지 않은 연금저축 납입금, 공제받은 납입금, 운용수익, 퇴직금은 인출 시 과세 취급이 다릅니다.

### 이 비교가 단순화한 부분

본문은 **매매차익만** 비교합니다. 분배금의 국내외 원천징수, 외국납부세액 관련 처리, 환율·보수·추적오차, 계좌 가입 자격과 납입한도, 개인별 소득·손익은 반영하지 않았습니다. ISA의 의무가입기간과 실제 만기는 같지 않을 수 있고, 일반형과 서민형 등의 비과세 한도도 다릅니다. 슬라이더 계산은 모든 수익 구간에 대한 계좌 추천이나 개인별 세액 계산이 아닙니다.

> ⚠️ 이 글은 개인 학습 정리이며 **세무 자문이 아닙니다.** 본문의 계산은 특정 조건을 가정한 **예시**이며, 소득 구간·가입 유형·보유 기간·실현 시점에 따라 결과가 달라집니다. 세법과 시행령은 개정될 수 있고, 발표된 개편안이 그대로 시행된다는 보장은 없습니다. 개별 사안은 반드시 **국세청 또는 세무 전문가**에게 확인하시기 바랍니다. 언급한 금융상품과 금융회사 자료는 제도 설명을 위한 예시이며 특정 상품의 매수·매도 권유가 아닙니다. 투자 판단과 그 결과, 신고 의무 이행은 본인의 몫입니다.

<script>
(function(){var s=document.getElementById('tf-profit');if(!s)return;var f=new Intl.NumberFormat('ko-KR',{maximumFractionDigits:2});function u(){var n=Number(s.value),a=n*0.846,b=n-Math.max(n-250,0)*0.22,c=n-Math.max(n-200,0)*0.099;document.getElementById('tf-amount').innerHTML=f.format(n)+' <small>만원</small>';document.getElementById('tf-dom').textContent=f.format(a);document.getElementById('tf-us').textContent=f.format(b);document.getElementById('tf-isa').textContent=f.format(c);var t;if(n<=200){t='이 구간에서는 미국 상장 ETF와 일반형 ISA 모두 예시 세금이 0원입니다. 공제와 비과세 한도 안에 있기 때문입니다.';}else if(n<=250){t='미국 상장 ETF는 250만원 기본공제 안이라 예시 세금이 0원입니다. 일반형 ISA에는 200만원을 넘는 금액에 9.9%가 붙습니다.';}else if(b>c){t='이 금액에서는 미국 상장 ETF의 세후 수익이 가장 큽니다. 250만원 기본공제의 효과가 일반형 ISA보다 크게 작용하는 구간입니다.';}else if(a>b){t='일반형 ISA의 세후 수익이 가장 큽니다. 일반계좌끼리는 국내 상장 해외 ETF가 앞섭니다. 수익이 커질수록 고정된 250만원 공제의 상대적 효과가 줄어듭니다.';}else{t=f.format(n)+'만원에서는 일반형 ISA의 세후 수익이 가장 큽니다. 일반계좌끼리는 250만원 기본공제를 쓰는 미국 상장 ETF가 앞섭니다.';}document.getElementById('tf-insight').textContent=t;Array.prototype.forEach.call(document.querySelectorAll('[data-tfv]'),function(x){x.setAttribute('aria-pressed',String(Number(x.dataset.tfv)===n));});}s.addEventListener('input',u);Array.prototype.forEach.call(document.querySelectorAll('[data-tfv]'),function(x){x.addEventListener('click',function(){s.value=x.dataset.tfv;u();});});u();})();
</script>
