---
title: "사람 대신 AI를 쓰면, 회사는 돈을 더 벌까? · AI 수익화 교과서 ④"
description: "메타의 AI 조직 개편과 아마존의 인력 전망에서 출발해, AI가 사람의 일을 맡으면 실제로 돈이 남는지 살펴봅니다. Klarna의 비용 절감과 쇼핑몰 검색 실험으로 AI 도입의 효과와 한계를 읽어봅니다."
slug: "ai-adoption-roi"
date: 2026-10-06T00:00:00+09:00
draft: false
image: "ai-revenue-4-cover.jpg"
categories: ["AI 투자"]
tags: ["AI 투자", "AI 수익화", "기업 AI 도입", "AI 생산성", "AI 투자수익률"]
---

<style>
.article-content{container-type:inline-size}
.ar4{--paper:#f6f3ea;--card:#fffef9;--ink:#193b3a;--muted:#586d68;--line:#cbd6ce;--green:#136d67;--coral:#a94835;--violet:#6854a1;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:12px;padding:30px;margin:32px 0;line-height:1.75;word-break:keep-all;overflow-wrap:anywhere}
.ar4 *{box-sizing:border-box}.ar4 p{margin:0}.ar4 .eyebrow{font-size:11px;font-weight:800;letter-spacing:.06em;color:var(--green);margin-bottom:12px}.ar4 .fig-title{font-size:26px;font-weight:800;line-height:1.4;margin-bottom:22px;letter-spacing:-.03em}.ar4 .cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.ar4 .cards.two{grid-template-columns:repeat(2,minmax(0,1fr))}.ar4 .card{background:var(--card);padding:18px;border:1px solid var(--line);border-top:4px solid var(--green);min-width:0;font-size:14px}.ar4 .card b{display:block;font-size:19px;margin:8px 0}.ar4 .card.violet{border-top-color:var(--violet)}.ar4 .card.coral{border-top-color:var(--coral)}.ar4 .number{font-size:33px!important;color:var(--green);line-height:1.3}.ar4 .small,.ar4 .note{font-size:12px;color:var(--muted)}.ar4 .note{margin-top:18px}.ar4 .band{background:var(--card);border-left:4px solid var(--coral);padding:16px;margin-top:18px;font-size:15px}.ar4 .badge{display:inline-block;background:var(--green);color:var(--paper);padding:3px 10px;border-radius:4px;font-size:12px;font-weight:700;margin-bottom:12px}.ar4 .row{display:grid;grid-template-columns:34px minmax(0,1fr);gap:10px;padding:15px 0;border-bottom:1px solid var(--line);font-size:15px}.ar4 .sign{font-size:25px;font-weight:800;color:var(--green)}.ar4 .minus .sign{color:var(--coral)}.ar4 .row b{display:block}.ar4 .row small{font-size:12px;color:var(--muted)}
[data-scheme=dark] .ar4{--paper:#233731;--card:#2c423c;--ink:#edf4ed;--muted:#b8cdc2;--line:#526e61;--green:#9cddcb;--coral:#ffb399;--violet:#cbbaff}
@container(max-width:600px){.ar4{padding:22px 18px}.ar4 .cards,.ar4 .cards.two{grid-template-columns:1fr}.ar4 .fig-title{font-size:23px}}
@media(max-width:600px){.ar4{padding:22px 18px}.ar4 .cards,.ar4 .cards.two{grid-template-columns:1fr}.ar4 .fig-title{font-size:23px}}
</style>

식당에 자동 조리기계를 들이면 “이제 적은 인원으로도 가게를 돌릴 수 있겠네”라는 기대가 생깁니다. 하지만 음식이 제때 나오는지 확인하고, 주문이 잘못 들어왔을 때 처리하고, 기계를 관리하는 일까지 없어지는 것은 아닙니다.

메타와 아마존이 AI를 업무에 도입하는 모습을 보면 비슷한 질문이 떠오릅니다. **사람이 하던 일을 AI에 맡기면, 회사는 인건비를 아끼고 돈을 더 벌 수 있을까요?**

AI를 판매하는 회사만큼 중요한 것은 AI를 업무에 사용하는 회사입니다. 직원에게 AI 도구를 주는 데서 더 나아가, 팀의 구성과 일하는 방식까지 바꾸려는 기업들은 무엇을 얻고 있을까요?

이미 비용 절감이나 구매 증가를 보여주는 사례는 있습니다. 다만 **AI가 일을 해냈다는 것과, 그 일을 회사가 더 적은 비용으로 끝냈다는 것은 다릅니다.** 메타와 아마존의 시도에서 출발해 그 차이를 살펴보겠습니다.

## 01 메타와 아마존은 왜 사람의 일을 AI에 맡기려 할까요?

아마존의 앤디 재시 CEO는 2025년 6월 직원들에게 보낸 글에서, 생성형 AI와 에이전트를 활용하면 일부 업무에는 더 적은 사람이, 다른 업무에는 더 많은 사람이 필요해질 것이라고 설명했습니다. 향후 몇 년 동안 AI에 따른 효율화로 회사의 사무직 인력 전체가 줄어들 것으로 예상한다고도 밝혔습니다. **AI를 단순한 편의 도구가 아니라, 필요한 인력과 일하는 방식을 바꾸는 기술로 본 것입니다.** 이는 당시 경영진의 전망이지, 그만큼의 절감액이 이미 실현됐다는 뜻은 아닙니다. [아마존 공식 발표, 2025년 6월](https://www.aboutamazon.com/news/company-news/amazon-ceo-andy-jassy-on-generative-ai)

메타에서는 조직을 실제로 바꾸려는 시도가 나왔습니다. 로이터가 2026년 8월 보도한 ‘Project OT’는 AI 에이전트와 소규모 인력 중심으로 업무를 재편하는 프로젝트였습니다. 사람이 전혀 없는 회사가 아니라, **더 적은 사람이 AI와 함께 일하고 그 결과를 감독하는 조직**을 구상한 것입니다. 메타는 프로젝트의 존재를 확인하면서, 비용 절감뿐 아니라 팀 재설계와 우선순위가 높은 업무로의 인력 이동이 포함됐다고 설명했습니다. [로이터 취재 기사 재게시본, 2026년 8월 26일](https://www.devdiscourse.com/article/international/3968118-special-report-mark-zuckerberg-had-a-bold-plan-to-replace-meta-staff-with-ai-heres-how-it-imploded)

기업이 기대하는 계산은 어렵지 않습니다. AI가 반복 업무를 맡으면 같은 일을 적은 인원으로 처리하거나, 같은 인원으로 더 많은 제품과 서비스를 만들 수 있다는 것입니다.

그런데 실제 업무에서는 ‘결과물을 만드는 일’과 ‘문제없이 끝내는 일’ 사이에 거리가 있습니다. 메타의 시도에서도 바로 그 문제가 드러났습니다.

## 02 AI가 일을 맡으면 사람이 할 일은 없어질까요?

로이터는 메타 내부에서 AI로 생성되는 코드가 크게 늘었지만, 기대한 생산성 효과가 충분히 나타나지 않았다는 문제 제기가 나왔다고 보도했습니다. 신뢰성 문제와 장애 대응 부담도 거론됐습니다. 메타는 예정했던 두 번째 구조조정 계획을 취소했고, 모든 시나리오를 실행하려던 것은 아니라고 설명했습니다. 다만 로이터도 경영진이 방향을 바꾼 정확한 원인은 확인하지 못했습니다. **이를 ‘AI 때문에 모든 계획이 실패했다’고 단정할 수는 없습니다.** [같은 로이터 기사](https://www.devdiscourse.com/article/international/3968118-special-report-mark-zuckerberg-had-a-bold-plan-to-replace-meta-staff-with-ai-heres-how-it-imploded)

여기서 생각해볼 문제는 코드의 양 자체가 아닙니다. 코드가 빨리 만들어져도 사람이 검토하고, 기존 시스템에 연결하고, 오류를 고쳐야 한다면 그 시간도 회사의 비용입니다. 고객상담에서도 AI가 빨리 답했지만 고객이 다시 문의하거나 사람이 잘못된 처리를 되돌려야 한다면 비슷한 일이 생깁니다.

<div class="ar4" id="ar4-workflow" role="group" aria-label="AI가 결과물을 만든 뒤에도 확인, 시스템 연결, 예외 처리가 남는 업무 과정">
<p class="eyebrow">FIGURE 01 / AI가 만든 뒤에도 일은 남습니다</p><p class="fig-title">답변과 코드가 나왔다고<br>업무가 끝난 것은 아닙니다.</p>
<div class="cards"><div class="card"><span class="small">1 · 결과물 만들기</span><b>AI가 초안을 만듭니다</b><p>답변·문서·코드를 빠르게 작성합니다.</p></div><div class="card violet"><span class="small">2 · 실제 업무에 적용하기</span><b>확인하고 연결합니다</b><p>정확성·보안을 검토하고 기존 시스템에 적용합니다.</p></div><div class="card coral"><span class="small">3 · 문제없이 마무리하기</span><b>오류와 예외를 처리합니다</b><p>재문의·오작동·잘못된 처리를 해결합니다.</p></div></div>
<div class="band">처음 결과물이 나오는 속도보다, 검수와 수정까지 끝낸 전체 시간과 비용을 봅니다.</div>
<p class="note">일반적인 업무를 단순화한 개념도입니다. 단계별로 AI와 사람이 나누는 역할은 업무에 따라 달라집니다.</p>
</div>

이 때문에 AI의 도입 비용을 따져야 합니다. 구독료뿐 아니라 사내 자료 정리, 시스템 연결, 직원 교육에 드는 비용이 있고, 운영을 시작한 뒤에도 검수와 오류 처리 비용이 이어질 수 있습니다. 처음 한 번 드는 비용과 매달 반복되는 비용을 나눠서 봐야 합니다.

직원이 두 시간을 아꼈다고 해서 그 두 시간의 급여가 바로 통장에서 빠져나가지 않게 되는 것도 아닙니다. **그 시간에 더 많은 주문을 처리했는지, 야근이나 외주를 줄였는지**까지 이어져야 돈의 변화가 보입니다.

그렇다고 사람이 확인해야 한다는 이유만으로 AI가 쓸모없다는 뜻은 아닙니다. 확인하는 데 드는 수고가 처음부터 직접 하는 수고보다 충분히 작다면 효과는 남습니다. 관건은 사람이 완전히 사라졌느냐가 아니라, **같은 품질의 일을 끝내는 데 총비용이 줄었느냐**입니다.

## 03 실제로 비용을 아낀 회사도 있나요?

결제·후불결제 서비스를 제공하는 Klarna(클라르나)는 AI를 고객상담에 사용합니다. 회사는 2025년 연차보고서에서 AI가 상담 채팅의 **80%를 처리했고, 약 5,900만 달러의 비용을 절감했다**고 설명했습니다. 회사가 보고한 운영 효과입니다. [2025년 연차보고서, 본문 184쪽](https://s205.q4cdn.com/644747736/files/doc_financials/2025/q4/Klarna-Group-plc-20-F-2025.pdf#page=188)

그런데 같은 해 고객서비스·운영비 총액은 전년보다 **2% 늘었습니다.** 비용을 아꼈다는데 왜 지출은 늘었을까요? 함께 봐야 할 것은 커진 사업 규모입니다. 같은 기간 **거래 건수는 25% 증가**했습니다. [같은 보고서, 본문 133쪽](https://s205.q4cdn.com/644747736/files/doc_financials/2025/q4/Klarna-Group-plc-20-F-2025.pdf#page=137)

<div class="ar4" id="ar4-klarna" role="group" aria-label="Klarna의 회사 보고 AI 절감 효과와 2025년 거래 건수 및 고객서비스 운영비 변화">
<p class="eyebrow">FIGURE 02 / 지출을 덜 늘리는 것도 효과입니다</p><p class="fig-title">일이 많아졌는데<br>비용은 조금만 늘었다면?</p>
<span class="badge">Klarna · 2025년 연간</span>
<div class="card"><span class="small">회사가 보고한 AI 상담 비용 절감 효과</span><b class="number">약 5,900만 달러</b><p>전년보다 비용이 이만큼 줄었다거나, 이만큼의 AI 순이익이 생겼다는 뜻은 아닙니다.</p></div>
<div class="cards two" style="margin-top:14px"><div class="card"><span class="small">거래 건수 · 전년 대비</span><b class="number">+25%</b></div><div class="card coral"><span class="small">고객서비스·운영비 · 전년 대비</span><b class="number">+2%</b></div></div>
<p class="note">출처: Klarna 2025년 연차보고서. 두 증가율의 차이 전부를 AI의 효과로 분리한 수치는 아닙니다.</p>
</div>

식당으로 치면 손님이 크게 늘었는데 주방 운영비는 조금만 늘어난 상황과 비슷합니다. AI의 가치는 지난달보다 지출을 줄이는 데만 있지 않습니다. **사업이 성장할 때 추가로 필요했을 비용을 억제하는 데도 있을 수 있습니다.** 다만 사업 규모에 따른 다른 효율화도 작용하므로, Klarna의 두 증가율 차이를 모두 AI 덕분이라고 계산해서는 안 됩니다.

Klarna는 사람 상담을 선택할 수 있는 경로도 유지한다고 설명합니다. 간단한 문의는 AI가 맡고 까다로운 문의는 사람이 처리하는 방식 역시 비용과 품질을 함께 맞추는 선택일 수 있습니다. ‘사람이 남아 있다’와 ‘AI 효과가 없다’는 같은 말이 아닙니다. [SEC에 제출한 회사 설명](https://www.sec.gov/Archives/edgar/data/2003292/000162828025034998/filename1.htm)

여기까지는 덜 쓰는 이야기였습니다. 그런데 AI로 이익을 얻는 길이 꼭 인력을 줄이는 데만 있을까요?

## 04 사람을 줄이지 않고 더 많이 팔 수는 없을까요?

온라인 쇼핑몰에서 원하는 상품을 검색했는데 엉뚱한 결과만 나온다고 생각해보세요. 살 마음이 있어도 상품을 찾지 못하면 다른 곳으로 가게 됩니다. AI가 검색어의 뜻을 더 잘 이해한다면, 직원 수를 줄이지 않아도 구매가 늘어날 가능성이 있습니다.

대형 해외직구 플랫폼에서 이를 시험했습니다. 아랍어·일본어·폴란드어 검색을 이용하는 약 **185만 명**을 무작위로 나눠, 한쪽에는 기존 번역 기반 검색을, 다른 쪽에는 생성형 AI로 검색어의 뜻을 해석·번역하는 방식을 적용했습니다. AI 적용 집단의 **이용자당 구매액은 약 2.9% 높았습니다.** 2024년 5~6월, 언어별로 9일씩 진행한 실험입니다. [「Generative AI and Sales Productivity」, 2026년 6월 개정본의 실험 설계·표 4](https://arxiv.org/html/2510.12049v6)

<div class="ar4" id="ar4-sales" role="group" aria-label="기존 검색과 AI 의미 해석 검색을 무작위로 비교한 온라인 소매업 실험">
<p class="eyebrow">FIGURE 03 / 인건비가 아닌 구매에서 나타난 변화</p><p class="fig-title">검색어를 더 잘 이해하면<br>고객이 더 살까요?</p>
<div class="cards two"><div class="card"><span class="small">비교 집단</span><b>기존 검색</b><p>검색어를 기본 번역하는 방식</p></div><div class="card violet"><span class="small">AI 적용 집단</span><b>뜻을 해석한 검색</b><p>생성형 AI가 검색어의 의미를 해석하고 번역</p></div></div>
<div class="band"><strong>이용자당 구매액 약 +2.9%</strong><br>AI 적용 집단과 비교 집단의 차이</div>
<p class="note">약185만 명 무작위 비교, 2024년5~6월 언어별9일 실험. 구매액은 플랫폼의 회계상 매출이나 순이익이 아닙니다. 출처: 논문 표4.</p>
</div>

이것은 AI가 회사의 지출뿐 아니라 고객의 구매에도 영향을 줄 수 있다는 사례입니다. 다만 구매액에는 입점 판매자의 거래도 포함되고, 전체 AI 도입 비용을 관찰한 연구는 아니므로 회사의 순이익이나 투자수익률이 2.9% 높아졌다고 읽을 수는 없습니다.

또 같은 연구에서 광고 제목과 마케팅 알림을 AI로 바꾼 경우에는 구매액 효과가 통계적으로 뚜렷하지 않았습니다. 단일 기업의 짧은 실험이고 일부 저자가 해당 기업의 직원·자문역이라는 범위도 있습니다. **어디에 AI를 붙이든 매출이 늘어나는 것은 아닙니다.** [같은 논문의 표 4·결론·이해관계 공개](https://arxiv.org/html/2510.12049v6)

투자자로서 주목할 부분은 AI 사용 자체보다, 그것이 고객의 어떤 불편을 해결했느냐입니다. 고객이 원하는 상품을 찾게 하고, 상담을 기다리다 떠나는 일을 줄이고, 주문을 정확하게 처리하는 개선도 기업이 AI로 돈을 버는 길이 될 수 있습니다.

## 05 투자자는 AI 도입 발표에서 무엇을 확인해야 할까요?

메타의 조직 개편, 아마존의 인력 전망, Klarna의 비용 절감 보고, 쇼핑몰의 구매 실험은 서로 다른 단계의 이야기입니다. **앞으로 기대하는 효과와 이미 관찰된 변화를 구분해서 읽는 것**이 출발점입니다.

‘AI를 도입했다’거나 ‘직원을 줄였다’는 발표만으로 성공을 판단하기는 어렵습니다. 감원은 조직 정리나 투자 재원 확보 때문일 수도 있고, 직원 수가 그대로여도 처리하는 주문이 늘었다면 효과가 있을 수 있습니다.

| 발표에서 본 내용 | 이어서 확인할 질문 |
|---|---|
| AI로 더 적은 인원이 일하게 된다 | 경영진의 계획인가, 실제 운영 결과인가? |
| 문서와 코드가 더 빨리 만들어진다 | 검수·수정까지 포함해도 일이 빨리 끝나는가? |
| 비용을 절감했다 | 전년보다 지출이 줄었나, 늘어날 지출을 피했나? |
| 고객의 구매가 늘었다 | 추가 판매의 비용과 AI 운영비를 빼도 이익이 남나? |
| 시범 도입이 잘됐다 | 범위를 넓힌 뒤에도 품질과 비용 효과가 유지되나? |

회사의 이익이 좋아졌다고 해서 전부 AI 효과인 것도 아닙니다. 가격 인상이나 경기 회복이 함께 작용할 수 있습니다. 반대로 경쟁사도 같은 도구로 비용을 줄여 가격을 낮춘다면, 개선 효과의 일부는 기업의 이익보다 고객의 혜택으로 돌아갈 수 있습니다.

결국 중요한 것은 AI가 사람을 몇 명 대신했느냐 하나가 아닙니다. **고객이 받는 품질을 유지하면서, 회사가 덜 쓰거나 더 벌게 됐는가. 그리고 그 변화가 반복되는가.** 이 질문에 답하는 실적을 찾아야 합니다.

## 정리

사람 대신 AI를 쓰면 무조건 돈이 남는 것도, 사람이 여전히 필요하면 AI 도입이 실패한 것도 아닙니다.

- **메타·아마존의 시도는 일하는 방식이 바뀌고 있음을 보여줍니다.** 다만 조직 개편과 인력 전망 자체가 이익의 증거는 아닙니다.
- **AI가 만든 결과물을 실제 업무로 완성하는 비용까지 봐야 합니다.** 검수·연결·오류 처리가 늘면 기대한 절감 효과가 줄어듭니다.
- **덜 쓰는 것뿐 아니라 더 파는 효과도 있습니다.** 비용 증가를 억제하거나 고객의 구매를 돕는 방식으로도 AI가 돈과 연결될 수 있습니다.

AI 도입 기업을 볼 때는 <strong>‘사람을 얼마나 줄였나?’보다 ‘같은 일을 끝내는 비용과 고객이 받는 가치가 어떻게 달라졌나?’</strong>를 먼저 묻고 싶습니다.

마지막 5편에서는 지금까지의 내용을 묶어, AI 기업의 실적 발표를 읽을 때 확인할 다섯 가지 질문으로 정리하겠습니다.

---

자료 기준: **2026년 10월 6일**. 아마존은 2025년 6월 경영진 발표, 메타는 2026년 8월 로이터 취재 보도와 그 안에 실린 회사 답변, Klarna는 2025년 연간 보고서를 사용했습니다. 소매업 사례는 2024년 실험의 2026년 6월 개정 논문을 바탕으로 합니다.

> ⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
