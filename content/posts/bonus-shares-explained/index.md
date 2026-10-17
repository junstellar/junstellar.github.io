---
title: "무상증자란? 주식 수와 주가는 어떻게 달라질까"
description: "무상증자의 뜻과 기업이 실시하는 이유부터 권리락에 따른 기준가격 조정, 발표와 신주 상장 전후의 주가 변화까지 정리합니다. 알테오젠의 30% 무상증자와 노터스의 급등락 사례로 원리와 실제 시장 반응을 구분해 봅니다."
slug: "bonus-shares-explained"
date: 2026-10-17T10:00:00+09:00
draft: false
image: "bonus-shares-cover.png"
categories: ["AI 투자"]
tags: ["무상증자", "무상증자 주가", "권리락", "알테오젠 무상증자", "주식 기초"]
---

<style>
.article-content{container-type:inline-size}
.bs{--paper:#f7f4ec;--ink:#183e39;--muted:#526b65;--card:#fffef9;--line:#cbd7cc;--teal:#16766b;--coral:#b34c39;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:14px;margin:32px 0;padding:28px;line-height:1.7;word-break:keep-all;overflow-wrap:anywhere}
.bs *{box-sizing:border-box}.bs p{margin:0}.bs .kicker{font-size:12px;letter-spacing:.05em;font-weight:800;color:var(--teal);margin-bottom:10px}.bs .figtitle{font-size:26px;font-weight:800;line-height:1.4;margin-bottom:24px}.bs .cols{display:grid;grid-template-columns:1fr 1fr;gap:18px}.bs .card{background:var(--card);border:1px solid var(--line);padding:22px;border-radius:8px;min-width:0}.bs .card .label{font-size:13px;color:var(--muted)}.bs .big{font-size:38px;line-height:1.2;font-weight:900;letter-spacing:-.04em;margin:12px 0;color:var(--teal)}.bs .math{font-size:18px;margin-top:10px}.bs .total{border-top:1px dashed var(--line);margin-top:18px;padding-top:12px;font-weight:800;font-size:21px}.bs .note{font-size:12px;color:var(--muted);margin-top:18px;line-height:1.7}.bs .strip{background:var(--card);padding:14px 18px;border-left:4px solid var(--coral);font-size:16px;margin-top:20px}.bs .ledger{height:88px;display:flex;margin:18px 0 12px;border-radius:6px;overflow:hidden;font-size:14px;font-weight:800}.bs .ledger span{display:flex;align-items:center;justify-content:center;text-align:center;padding:4px}.bs .capital{background:#146f63;color:#fff}.bs .reserve{background:#d9e8c8;color:#244537}.bs .events{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.bs .event{border-top:4px solid var(--teal);background:var(--card);padding:18px 14px;font-size:14px}.bs .event:last-child{border-color:var(--coral)}.bs .event strong{display:block;font-size:27px;line-height:1.3;margin:14px 0}.bs .date{font-size:12px;font-weight:800;color:var(--muted)}.bs .event:last-child strong{color:var(--coral)}.bs-intro{font-size:13px;color:var(--body-text-color);opacity:.75;margin-bottom:24px}
[data-scheme=dark] .bs{--paper:#233c36;--ink:#f0f5ed;--muted:#b9cec0;--card:#2b453d;--line:#526e60;--teal:#a1e4d1;--coral:#ffb7a3}
.bs .capital{font-size:12px;padding:2px}
@container(max-width:580px){.bs{padding:22px 18px}.bs .cols,.bs .events{grid-template-columns:1fr}.bs .figtitle{font-size:23px}.bs .big{font-size:34px}}
@media(max-width:600px){.bs{padding:22px 18px}.bs .cols,.bs .events{grid-template-columns:1fr}.bs .figtitle{font-size:23px}}
</style>

<p class="bs-intro">내 주식에 이런 일이 생기면 · 첫 번째 이야기 / 자료 확인: 2026.10.17</p>

## 무상증자는 주주에게 추가 납입 없이 새 주식을 배정하는 것입니다

**무상증자는 회사가 잉여금 등을 자본금으로 옮기고, 그에 해당하는 새 주식을 기존 주주에게 추가 대금 없이 배정하는 것**입니다. ‘무상’은 주주가 새 주식을 받기 위해 돈을 더 내지 않는다는 뜻이고, ‘증자’는 회사의 자본금이 늘어난다는 뜻입니다.

예를 들어 100% 무상증자라면 기존 1주에 새 주식 1주를 줍니다. 받을 자격을 갖춘 주주가 100주를 가지고 있었다면, 새 주식 100주가 더해져 총 200주가 됩니다.

여기서 저는 ‘자본금이 늘어난다’는 부분이 헷갈렸습니다. 회사에 새 돈이 들어오는 걸까요? **무상증자는 그렇지 않습니다. 회사 장부 안에서 자본의 구성을 바꾸는 일입니다.**

<div class="bs" id="bs-capital" role="group" aria-label="무상증자 전후 자기자본 내 구성 변화: 자본금 2억과 잉여금 등 8억이 자본금 4억과 잉여금 등 6억으로 바뀌며 합계는 10억 유지">
<p class="kicker">무상증자의 뜻 / 가상의 회사 장부</p><p class="figtitle">잉여금을 자본금으로 옮기고<br>새 주식을 발행합니다.</p>
<div class="cols"><div class="card"><p class="label">이전 · 자기자본 총 10억원</p><div class="ledger"><span class="capital" style="width:20%">자본금<br>2억</span><span class="reserve" style="width:80%">잉여금 등 8억</span></div></div><div class="card"><p class="label">이후 · 자기자본 총 10억원</p><div class="ledger"><span class="capital" style="width:40%">자본금<br>4억</span><span class="reserve" style="width:60%">잉여금 등 6억</span></div></div></div>
<p class="strip">자본금은 2억원 증가하지만, 회사 밖에서 새 돈이 들어오지는 않습니다.</p><p class="note">다른 변동과 발행 비용을 제외한 예시입니다. 자기자본은 회사 장부의 금액이며 주식시장의 시가총액과 다릅니다. 잉여금도 통장에 별도로 쌓여 있는 현금을 뜻하지 않습니다.</p>
</div>

유상증자와 비교하면 이해가 쉽습니다. **유상증자는 새 주식을 발행하면서 투자자에게 납입을 받아 자금을 조달하고, 무상증자는 회사 안의 재원을 자본금으로 옮깁니다.** 이름은 비슷하지만 회사에 새 자금이 들어오는지에서 차이가 납니다.

피자로 비유하면, 무상증자는 같은 피자를 더 많은 조각으로 나누는 쪽에 가깝습니다. 조각이 늘어난 만큼 한 조각의 크기는 작아집니다. 주식에서도 수량과 한 주의 가격을 함께 봐야 하는 이유입니다.

## 회사가 무상증자를 하는 이유

회사는 주식 수를 늘리고 한 주의 거래가격을 낮춰, 투자자들이 좀 더 쉽게 거래하도록 하려는 목적으로 무상증자를 실시하기도 합니다. 여기서 말하는 **유동성 개선**은 회사의 현금이 늘어난다는 뜻이 아니라, 시장에서 주식을 사고팔기 쉬워진다는 뜻입니다.

투자자에게 회사를 알리고 주주들의 관심을 높이는 계기가 되기도 합니다. 시장에서는 이를 회사의 성장이나 주주 친화적인 태도에 대한 신호로 해석할 수 있습니다. 다만 그것은 해석이지, 무상증자 발표만으로 미래 실적이 좋아졌다는 증거는 아닙니다. [자본시장연구원, 무상증자의 유동성·신호 가설 설명](https://www.kcmi.re.kr/report/report_view?report_no=1503)

저는 이 대목을 **‘회사가 기대하는 효과’와 ‘실제로 벌어진 결과’로 나눠 읽는 편이 낫겠다**고 생각했습니다. 거래를 활발하게 만들겠다는 취지가 있어도 효과가 오래갈지는 별개이고, 주주를 위한 정책이라는 설명만으로 이익이 늘어나는 것도 아니니까요.

## 주식 수가 늘면 기준가격은 어떻게 바뀔까요

한 주에 새 주식 한 주를 배정하는 100% 무상증자를 가정해 보겠습니다. 1만원짜리 주식 100주를 가진 주주는 신주까지 합쳐 200주를 갖게 됩니다. 다른 가격 변동이 없다면 한 주의 이론가격은 5,000원으로 낮아집니다.

<div class="bs" id="bs-price" role="group" aria-label="100% 무상증자 가정: 100주 곱하기 1만원과 200주 곱하기 5천원은 모두 100만원">
<p class="kicker">주식 수와 가격 / 100% 무상증자 가정</p><p class="figtitle">주식 수는 두 배,<br>한 주의 이론가격은 절반.</p>
<div class="cols"><div class="card"><p class="label">무상증자 전</p><p class="big">100주</p><p class="math">× 10,000원</p><p class="total">평가금액 100만원</p></div><div class="card"><p class="label">신주까지 반영한 이론 비교</p><p class="big">200주</p><p class="math">× 5,000원</p><p class="total">평가금액 100만원</p></div></div>
<p class="strip">새 주식까지 포함하면, 가격 조정만으로 평가금액이 줄거나 늘지는 않습니다.</p>
<p class="note">모든 주식에 동일 비율 배정, 다른 가격 변동 없음, 세금·거래비용 제외 가정입니다. 자기주식 배정 제외 등 개별 회사의 조건은 단순화했습니다.</p>
</div>

계산은 <strong>기존 가격 ÷ (1 + 신주 배정비율)</strong>입니다. 30%라면 1.3으로, 100%라면 2로 나눕니다. 실제 거래소 기준가격에는 호가 단위 등 세부 규칙이 적용될 수 있습니다.

이 가격 조정과 연결되는 말이 **권리락**입니다. 무상증자의 권리락일부터 주식을 사는 사람에게는 이번 신주를 받을 권리가 붙지 않습니다. 그래서 그 권리가 빠진 상태에 맞춰 거래의 기준가격을 조정합니다. 신주가 계좌에 들어와 거래되기 시작하는 것은 그보다 뒤의 일입니다.

중요한 것은 **기준가격과 실제 거래가격이 같지는 않다**는 점입니다. 5,000원으로 기준을 맞췄더라도 실제 시장에서는 매수·매도 주문에 따라 그보다 높거나 낮은 가격에 거래될 수 있습니다. 다음부터는 그 시장 반응을 따로 보겠습니다.

## 무상증자 발표 뒤 주가가 오르거나 내리는 이유

무상증자는 그 자체로 회사의 이익이나 자산을 늘리는 일이 아닙니다. 그런데도 발표 뒤 주가가 오르는 경우가 있습니다. 투자자들이 거래 활성화를 기대하거나 회사의 결정을 긍정적으로 받아들여 매수하기 때문일 수 있습니다. 낮아진 주당 가격을 보고 종목 자체가 저렴해졌다고 느끼는 경우도 있습니다.

반대로 기대가 이미 가격에 반영돼 있었다면 발표 후에도 별 반응이 없을 수 있습니다. 기대가 약해지거나 단기 차익을 실현하려는 매도가 많아지면 주가는 하락할 수 있습니다. **무상증자는 주가를 움직이는 계기가 될 수 있지만, 상승 방향을 정해 놓는 제도는 아닙니다.**

이 흐름은 시점을 나눠 보면 덜 헷갈립니다.

<div class="bs" id="bs-stages" role="group" aria-label="무상증자 결정 발표, 권리락, 신주 상장의 세 단계별 주가 영향">
<p class="kicker">주가를 읽는 순서 / 세 시점을 구분하세요</p><p class="figtitle">발표에 대한 반응과<br>권리락의 가격 조정은 다릅니다.</p>
<div class="events"><div class="event"><p class="date">① 결정 발표</p><strong>기대의 변화</strong><p>배정비율·취지를 보고 투자자들이 매수하거나 매도합니다.</p></div><div class="event"><p class="date">② 권리락</p><strong>기준가격 조정</strong><p>신주를 받을 권리가 빠집니다. 실제 거래가격은 주문에 따라 달라집니다.</p></div><div class="event"><p class="date">③ 신주 상장</p><strong>신주 거래 시작</strong><p>새 주식도 팔 수 있게 됩니다. 매도와 매수 수요가 함께 가격에 영향을 줍니다.</p></div></div>
<p class="note">전형적인 절차를 설명한 도해입니다. 단계별 상승·하락을 예측한 것이 아니며, 구체적인 날짜와 조건은 해당 공시로 확인해야 합니다.</p>
</div>

신주가 상장될 때는 거래할 수 있는 주식이 늘어납니다. 받은 주식을 팔려는 주문이 매수 수요보다 강하면 가격에 부담이 될 수 있습니다. 그렇다고 ‘신주 상장일에는 무조건 하락한다’고 단정할 수는 없습니다. 이미 알려진 일정이라는 점, 새로 들어오는 매수 수요, 그 사이 나온 실적이나 다른 뉴스도 함께 작용합니다.

자본시장연구원의 2022년 보고서에서도 당시 무상증자 열풍에서 나타난 주가 상승과 거래 활성화가 단기에 그친 현상을 지적했습니다. 이 결과를 모든 무상증자에 적용할 수는 없지만, 발표 직후의 상승만 보고 지속적인 효과까지 기대해서는 안 된다는 참고가 됩니다. [분석 보고서](https://www.kcmi.re.kr/report/report_view?report_no=1503)

## 최근 사례는 알테오젠의 30% 무상증자입니다

알테오젠은 2026년 7월 16일, 기존 주식 1주당 새 주식 0.3주를 배정하는 무상증자를 공고했습니다. 배정기준일은 8월 6일, 보통주 신주 상장일은 8월 26일이었습니다. 재원은 주식을 액면가보다 높게 발행하면서 생긴 자본잉여금인 ‘주식발행초과금’이었습니다. [회사 공고](https://www.alteogen.com/kr/sub/ir/notice.php?bid=3&idx=331&mode=view) · [추가상장 공시](https://spn.stockplus.com/news/api/v1/disclosure_views/koscom/499594)

앞에서 본 정의가 공시에는 이렇게 적히는 것입니다. 주주에게 돈을 더 받는 것이 아니라 회사의 주식발행초과금을 자본금으로 옮기고, 신주를 배정합니다. 받을 자격을 갖춘 주주가 100주를 보유했다면 30주를 더 받아 총 130주가 됩니다.

30% 배정일 때의 가격 조정을 이해하려고, 주가를 1만 3,000원으로 **가정**해 계산해 봤습니다.

| 구분 | 무상증자 전 | 신주를 포함한 이론 비교 |
|---|---:|---:|
| 주식 수 | 100주 | 130주 |
| 한 주의 가격 | 13,000원 | 10,000원 |
| 주식 수 × 가격 | 130만원 | 130만원 |

*표의 가격은 알테오젠의 실제 주가가 아닙니다. 동일 비율 배정과 다른 가격 변동이 없는 상황을 가정하고, 세금·거래비용은 제외했습니다.*

이 사례는 실제 공시의 배정비율을 계좌의 주식 수와 연결해 보는 예입니다. 알테오젠의 이후 주가가 어떻게 움직였는지 설명하려면 별도로 실제 시세와 같은 기간의 사업 뉴스를 살펴봐야 합니다. **30% 무상증자라는 숫자는 주식 배정비율이지 주가 상승률이 아닙니다.**

## 노터스 사례는 가격 조정 이후의 급등락을 보여줍니다

실제 시장 반응이 얼마나 커질 수 있는지는 2022년 노터스 사례에서 볼 수 있습니다. 당시 회사는 1주당 신주 8주를 배정하는 **800% 무상증자**를 발표했습니다. 100주를 가진 적격 주주라면 새 주식 800주를 더 받아 총 900주가 되는 구조입니다. [당시 무상증자 결정 보도](https://www.edaily.co.kr/news/read?mediaCodeNo=257&newsId=02115606632327280)

권리락이 발생한 5월 31일부터 6월 9일까지 주가는 6거래일 연속 상한가를 기록했습니다. 이후 6월 10일 하루 거래가 정지됐고, 거래가 재개된 6월 13일에는 하루 만에 28.21% 하락했습니다. [이데일리, 2022.6.14 당시 거래 경과](https://www.edaily.co.kr/News/Read?mediaCodeNo=257&newsId=01656406632361720)

<div class="bs" id="bs-knotus" role="group" aria-label="노터스 2022년 무상증자와 권리락 이후 급등락 사건 순서">
<p class="kicker">실제 시장 반응 / 노터스 · 2022년</p><p class="figtitle">권리락으로 기준을 조정한 뒤에도<br>주가는 크게 움직였습니다.</p>
<div class="events"><div class="event"><p class="date">5월 9일 · 결정 발표</p><strong>1주당 +8주</strong><p>기존 주식 100주에 신주 800주를 더 배정하는 구조</p></div><div class="event"><p class="date">5월 31일~6월 9일</p><strong>6연속 상한가</strong><p>권리락 이후 주가 급등<br>6월 10일 하루 거래 정지</p></div><div class="event"><p class="date">6월 13일 · 거래 재개</p><strong>하루 -28.21%</strong><p>기준가격 조정이 아닌<br>시장에서의 실제 하락</p></div></div>
<p class="note">가격 차트가 아닌 사건 순서도입니다. 출처: 이데일리 2022.5.9·6.14 보도. 특정 투자자의 매매 수익률을 나타내지 않습니다.</p>
</div>

제가 이 사례에서 구분해서 본 것은 **5월 31일의 권리락과 6월 13일의 하락이 서로 다른 일**이라는 점입니다. 권리락은 신주 배정을 반영해 가격 기준을 조정한 것이고, 그 뒤의 급등락은 바뀐 기준 위에서 실제 거래가격이 움직인 것입니다.

노터스를 무상증자 때문에 망한 회사로 볼 수는 없습니다. 이 사례는 기업의 파산이 아니라, 무상증자 이벤트를 둘러싸고 주가가 크게 출렁였던 기록입니다. 당시의 모든 등락을 무상증자 하나로 설명할 수도 없습니다. 다만 **주식 수가 늘어나는 원리를 이해하는 것과, 그 종목의 이후 주가를 예측하는 것은 다른 문제**라는 점은 잘 보여줍니다.

## 정리

무상증자는 회사 내부의 재원을 자본금으로 옮기고, 기존 주주에게 추가 납입 없이 새 주식을 배정하는 방식입니다. 회사는 거래 활성화 등을 기대하며 실시하지만, 그 자체로 회사에 새 자금이 들어오거나 이익이 늘어나지는 않습니다.

주가에 미치는 영향은 두 가지로 나눠 이해하면 됩니다. **하나는 늘어나는 주식 수를 반영한 기준가격 조정이고, 다른 하나는 기대와 매수·매도에 따른 실제 시장가격의 변화입니다.** 전자는 원리를 계산할 수 있지만 후자의 방향은 정해져 있지 않습니다.

저는 다음에 무상증자 공시를 보면 배정비율만 보지 않고, 언제 권리락이 발생하고 언제 신주가 상장되는지도 함께 보려고 합니다. [DART](https://dart.fss.or.kr/)나 [KIND](https://kind.krx.co.kr/)에서 회사명과 ‘무상증자 결정’을 검색해 정정공시까지 확인할 수 있습니다. 회사의 실적과 다른 공시도 함께 봐야 가격 변화의 이유를 덜 혼동할 것 같습니다.

다음 이야기: **권리락이란? 주식을 언제 사야 무상증자를 받을까요?**

---

⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
