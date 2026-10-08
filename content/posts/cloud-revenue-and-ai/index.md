---
title: "챗GPT와 클로드가 성장하면, 왜 빅테크도 돈을 벌까 · AI 수익화 교과서 ③"
description: "OpenAI·앤트로픽은 클라우드 사용료를 내고도 이익을 남길 수 있을까요? AI 서비스를 파는 회사와 컴퓨팅을 공급하는 AWS·Azure·구글 클라우드의 관계, 각각의 매출과 비용을 살펴봅니다."
slug: "cloud-revenue-and-ai"
date: 2026-10-02T00:00:00+09:00
draft: false
image: "ai-revenue-3-cover.jpg"
categories: ["AI 투자"]
tags: ["AI 투자", "AI 수익화", "AWS", "Azure", "Google Cloud"]
---

<style>
.article-content{container-type:inline-size}
.ar3{--paper:#f6f3ea;--card:#fffef9;--ink:#193b3a;--muted:#586d68;--line:#cbd6ce;--green:#136d67;--coral:#a94835;background:var(--paper);color:var(--ink);border:1px solid var(--line);border-radius:10px;padding:30px;margin:32px 0;line-height:1.75;word-break:keep-all;overflow-wrap:anywhere}
.ar3 *{box-sizing:border-box}.ar3 p{margin:0}.ar3 .eyebrow{font-size:11px;font-weight:800;letter-spacing:.08em;color:var(--green);margin-bottom:12px}.ar3 .fig-title{font-size:26px;font-weight:800;line-height:1.4;margin-bottom:22px;letter-spacing:-.03em}.ar3 .cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.ar3 .cards.two{grid-template-columns:repeat(2,minmax(0,1fr))}.ar3 .card{background:var(--card);padding:18px;border:1px solid var(--line);border-top:4px solid var(--green);min-width:0;font-size:14px}.ar3 .card b{display:block;font-size:20px;margin:10px 0}.ar3 .card .number{font-size:29px;color:var(--green);line-height:1.4}.ar3 .small,.ar3 .note{font-size:12px;color:var(--muted)}.ar3 .note{margin-top:18px}.ar3 .band{background:var(--card);border-left:4px solid var(--coral);padding:16px;margin-top:16px;font-size:15px}.ar3 .row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:14px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line);font-size:15px}.ar3 .row strong{font-size:25px;color:var(--green)}.ar3 .row small{display:block;font-size:12px;color:var(--muted)}.ar3 .unknown{font-weight:800;color:var(--coral);font-size:18px}
[data-scheme=dark] .ar3{--paper:#233731;--card:#2c423c;--ink:#edf4ed;--muted:#b8cdc2;--line:#526e61;--green:#9cddcb;--coral:#ffb399}
.ar3 .cost{margin-top:18px!important;padding-top:14px;border-top:1px dashed var(--line)}
.ar3 .flow{display:grid;gap:0}.ar3 .step{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:17px 20px}.ar3 .step b{display:block;font-size:19px;margin-bottom:4px}.ar3 .step p{font-size:14px}.ar3 .connector{text-align:center;padding:8px;font-size:13px;font-weight:700;color:var(--green)}
@container(max-width:600px){.ar3{padding:22px 18px}.ar3 .cards,.ar3 .cards.two{grid-template-columns:1fr}.ar3 .fig-title{font-size:23px}.ar3 .row strong{font-size:21px}}
@media(max-width:600px){.ar3{padding:22px 18px}.ar3 .cards,.ar3 .cards.two{grid-template-columns:1fr}.ar3 .fig-title{font-size:23px}.ar3 .row strong{font-size:21px}}
</style>

음식점이 식재료를 사 오고 임대료를 낸다고 해서, 돈을 버는 쪽이 식재료 업체와 건물주뿐인 것은 아닙니다. 손님은 재료 그 자체가 아니라 완성된 음식과 서비스를 사기 때문입니다. 음식점도 비용을 치르고 남길 수 있어야 장사를 이어갑니다.

챗GPT와 클로드도 비슷합니다. 이용자는 글을 쓰고, 코드를 만들고, 업무를 처리하는 능력에 돈을 냅니다. OpenAI와 앤트로픽은 그 서비스를 팔고, 서비스를 돌리는 데 필요한 컴퓨터를 확보합니다. 이 과정에 AWS·Azure·Google Cloud 같은 클라우드 사업자가 참여합니다.

**AI 회사와 클라우드 회사는 한쪽만 돈을 벌 수 있는 관계가 아닙니다. 서로 다른 것을 팔고, 각각의 비용을 감당하는 두 사업이 연결돼 있습니다.**

[2편](/p/ai-inference-cost/)에서 AI 서비스의 비용을 살펴봤다면, 이번에는 그 비용의 거래 상대를 보겠습니다. 먼저 “그러면 OpenAI와 앤트로픽에는 남는 게 없나?”라는 질문부터 풀어보겠습니다.

## 01 OpenAI와 앤트로픽도 고객에게 서비스를 팔아 매출을 올립니다

챗GPT에 코드를 고쳐 달라고 할 때 우리가 원하는 것은 GPU를 몇 초 빌리는 일이 아닙니다. 오류를 찾아 설명하고, 쓸 수 있는 코드를 만들어주는 결과입니다. 모델 회사는 컴퓨팅 자원에 모델의 성능과 제품 기능을 결합해 개인·기업에게 판매합니다.

돈을 받는 방법은 개인 구독, 기업용 계약, 개발자가 프로그램에서 모델을 호출할 때 내는 API 사용료 등입니다. 단순히 컴퓨터 사용료를 대신 받아 전달하는 회사가 아니라, **고객이 계속 돈을 낼 만한 AI 서비스를 만드는 회사**인 셈입니다.

실제 매출 발표도 있습니다. OpenAI는 **2026년 3월 31일 발표 당시 월 매출 20억 달러**를 올리고 있다고 밝혔습니다. 앤트로픽은 **5월 28일 발표에서 그달 연환산 매출 규모가 470억 달러를 넘었다**고 설명했습니다. 뒤의 숫자는 당시 매출 속도를 연간으로 표현한 것이며, 두 수치는 시점과 측정 방식이 달라 그대로 비교할 수 없습니다. [OpenAI 발표](https://openai.com/index/accelerating-the-next-phase-ai/), [앤트로픽 발표](https://www.anthropic.com/news/series-h)

그렇다면 두 회사가 이미 순이익도 내고 있다는 뜻일까요? **매출이 있다는 답과 회사 전체가 흑자라는 답은 다릅니다.** 위 발표는 매출 규모를 보여주지만, 모든 비용을 반영한 같은 기간의 순이익까지 제시하는 자료는 아닙니다. 이 자료만으로 현재 두 회사의 흑자·적자를 확정할 수는 없습니다.

다만 컴퓨터 사용료를 낸다는 사실 자체가 적자의 증거는 아닙니다. 고객에게 받은 돈으로 서비스 운영비뿐 아니라 모델 연구개발과 인건비 등도 감당할 수 있는지가 관건입니다. 비용을 낸 뒤 남길 수 있다면 모델 회사에도 이익이 생깁니다.

여기서 다음 질문이 나옵니다. 그렇게 중요한 컴퓨터를 왜 다른 회사에서 빌릴까요?

## 02 AI를 잘 만드는 것과 컴퓨터를 대규모로 운영하는 것은 다른 일입니다

AI 모델을 학습시키고 수많은 이용자의 요청에 답하려면 연산 장비가 필요합니다. 장비만 사면 끝나는 것도 아닙니다. 전력과 냉각, 빠른 네트워크, 고장 대응과 안정적인 운영도 갖춰야 합니다.

**데이터센터는 이런 장비와 시설이 모인 장소이고, 클라우드는 그 안의 계산 능력이나 저장 공간 등을 고객에게 제공하는 서비스**입니다. 건물의 빈방을 빌리는 것보다, 준비된 컴퓨터를 필요한 조건으로 이용하는 것에 가깝습니다.

모델 회사가 이를 모두 직접 마련할 수도 있지만, 외부 공급자를 쓰면 이미 구축된 자원과 운영 역량을 활용할 수 있습니다. 모델 개발과 제품 개선을 하면서 필요한 컴퓨팅을 확보하는 선택입니다. 그렇다고 비용이 항상 더 싸거나 공급자에 대한 의존이 사라지는 것은 아닙니다.

실제로 OpenAI는 **2025년 11월 AWS와의 계약 발표에서 컴퓨팅 자원 사용을 즉시 시작한다**고 밝혔습니다. 발표에는 챗GPT의 답변 생성과 차세대 모델 학습을 지원할 수 있는 인프라라는 설명도 들어 있습니다. [OpenAI·AWS 공식 발표](https://openai.com/index/aws-and-openai-partnership/)

앤트로픽도 **2026년 5월 발표에서 AWS를 주요 클라우드 제공자이자 학습 파트너로 명시**했습니다. 동시에 Google·Broadcom 등과의 컴퓨팅 확대를 설명했습니다. OpenAI 역시 Microsoft·Oracle·AWS·CoreWeave·Google Cloud 등 여러 파트너를 활용한다고 밝혔습니다. 한 모델 회사가 한 클라우드에만 묶인 단순한 구도는 아닙니다. [앤트로픽 발표](https://www.anthropic.com/news/series-h), [OpenAI 인프라 설명](https://openai.com/index/accelerating-the-next-phase-ai/)

따라서 AI 서비스가 성장하면, 모델 회사의 매출뿐 아니라 **그 서비스를 위해 구매하는 컴퓨팅 수요도 커질 수 있습니다.** 이것이 챗GPT·클로드의 성장과 빅테크 실적을 연결하는 고리입니다. 다만 연산 효율, 자체 장비 활용, 가격 조건에 따라 클라우드 지출이 늘어나는 폭은 달라집니다.

<div class="ar3" id="ar3-money-flow" role="group" aria-label="고객의 AI 이용료와 모델 회사의 컴퓨팅 구매가 이어지는 관계">
<p class="eyebrow">FIGURE 01 / 연결되어 있지만 서로 다른 거래입니다</p><p class="fig-title">고객은 AI 서비스를 사고,<br>AI 회사는 컴퓨팅을 삽니다.</p>
<div class="flow"><div class="step"><b>개인·기업 고객</b><p>글쓰기·코딩·업무 처리에 쓸 AI 서비스에 돈을 냅니다.</p></div><div class="connector">↓ 구독료 · API 사용료 · 기업 계약</div><div class="step"><b>OpenAI·앤트로픽 등 모델 회사</b><p>서비스 매출을 올리고, 그 서비스를 제공하는 데 필요한 비용을 부담합니다.</p></div><div class="connector">↓ 여러 비용 중 하나인 컴퓨팅 구매</div><div class="step"><b>AWS·Azure·Google Cloud 등</b><p>연산 자원을 공급해 매출을 올리고, 장비와 시설을 운영하는 비용을 부담합니다.</p></div></div>
<div class="band">이용료 전액이 클라우드로 넘어가는 것은 아닙니다.<br>양쪽 회사 모두 자기 매출에서 비용을 감당해야 합니다.</div>
<p class="note">모델 회사에 직접 결제하는 경로를 단순화했습니다. 거래 시점과 금액은 계약마다 다르며, 위아래 매출을 더해 최종 고객의 AI 지출로 계산하지 않습니다.</p>
</div>

## 03 컴퓨터 사용료를 내고도 남겨야 모델 회사의 사업이 됩니다

클라우드 회사가 매출을 올린다고 해서 모델 회사의 이익이 사라지는 것은 아닙니다. 음식점과 식재료 업체가 서로 다른 비용 구조를 갖듯, 두 회사의 이익이 생기는 조건도 다릅니다.

모델 회사에는 **고객이 지불하는 가격과 서비스를 제공하는 비용 사이의 차이**가 중요합니다. 같은 일을 더 적은 연산으로 처리하거나, 더 유용한 기능을 제공해 유료 고객을 확보하면 수익성을 개선할 여지가 있습니다. 반대로 가격을 낮추는데 사용 비용은 줄지 않는다면 고객이 늘어도 부담이 커질 수 있습니다.

이때 현재 서비스의 운영비를 뺀 뒤 돈이 남더라도 회사 전체 흑자는 아닐 수 있습니다. 다음 모델을 개발하는 연구비와 다른 운영비도 있기 때문입니다. “답변 한 건을 제공하며 남기는 돈”과 “회사의 최종 이익”을 구분해야 합니다.

클라우드 회사도 사용료를 받기만 하는 것은 아닙니다. 서버와 시설을 마련하고, 전력·냉각·운영 비용을 감당해야 합니다. 장비가 고객의 유료 작업에 얼마나 쓰이는지, 어떤 가격으로 공급하는지가 중요합니다.

<div class="ar3" id="ar3-two-businesses" role="group" aria-label="모델 회사와 클라우드 회사가 파는 가치와 각각 감당하는 비용">
<p class="eyebrow">FIGURE 02 / 한쪽의 이익이 다른 쪽의 적자를 뜻하지 않습니다</p><p class="fig-title">서로 다른 것을 팔고,<br>각자의 비용을 감당합니다.</p>
<div class="cards two"><div class="card"><span class="small">모델 회사</span><b>AI의 능력과 제품</b><p>고객에게 받는 돈<br>구독 · API · 기업용 서비스</p><p class="cost">감당할 비용<br>컴퓨팅 · 모델 연구개발 · 인건비와 운영비</p></div><div class="card"><span class="small">클라우드 회사</span><b>컴퓨팅과 운영 서비스</b><p>고객에게 받는 돈<br>컴퓨팅 이용 · 용량 계약 등</p><p class="cost">감당할 비용<br>장비 · 시설 · 전력 · 냉각과 운영비</p></div></div>
<div class="band">두 회사가 모두 이익을 낼 수 있는 구조입니다.<br>현재 흑자인지는 각 회사의 실제 손익을 따로 확인해야 합니다.</div>
<p class="note">사업 구조를 비교한 도해입니다. 비용의 회계 처리와 인식 시점은 다르며, 실제 기업의 손익 계산식이나 비용 비중을 뜻하지 않습니다.</p>
</div>

결국 “누가 구독료를 더 많이 가져가나”만으로는 어느 사업이 좋은지 알 수 없습니다. **고객에게 어떤 가치를 제공하고, 그 가치를 만드는 데 얼마가 드는가**를 각각 봐야 합니다. 모델 성능이 좋아져도 너무 비싸게 서비스하면 어려울 수 있고, 대규모 컴퓨터를 확보해도 고객이 충분히 쓰지 않으면 어려울 수 있습니다.

## 04 클라우드는 실제로 이익을 내지만 AI 수익을 독차지하는 것은 아닙니다

그렇다면 컴퓨팅을 공급하는 사업의 이익은 확인될까요? 아마존의 AWS를 예로 보면, **2026년 2분기 매출은 약 422억 달러, 부문 영업이익은 약 166억 달러**였습니다. 단순히 계약만 발표된 것이 아니라 실제 매출과 영업흑자가 확인됩니다. [아마존 공식 실적 발표](https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-Second-Quarter-Results/default.aspx)

다만 AWS에는 AI용 컴퓨팅뿐 아니라 일반 기업의 서버·저장·데이터베이스 서비스도 들어갑니다. 166억 달러를 전부 챗GPT·클로드에서 남긴 이익으로 볼 수는 없습니다. 이 숫자가 확인해주는 것은 **클라우드 사업 자체에 수익 기반이 있다**는 점입니다.

또 한 회사의 영업흑자가 앞으로 늘리는 모든 설비의 성공을 보장하지도 않습니다. 고객 수요를 과대평가하거나 공급 가격이 낮아지면 투자 부담이 커질 수 있습니다. 이 부분은 [5편의 빅테크 AI 투자와 회수](/p/how-to-read-ai-earnings/)에서 이어서 살펴봤습니다.

AI 회사와 클라우드 회사의 역할이 완전히 나뉘는 것도 아닙니다. 빅테크는 자체 AI 모델과 제품을 개발하고, 외부 모델을 자사 플랫폼에서 판매하기도 합니다. 앤트로픽은 Claude가 AWS·Google Cloud·Azure 세 플랫폼에서 제공된다고 설명합니다. **모델 회사가 컴퓨터를 구매하는 거래와, 클라우드 플랫폼을 통해 모델을 판매하는 거래가 함께 있는 셈입니다.** [앤트로픽의 플랫폼 제공 설명](https://www.anthropic.com/news/series-h)

그래서 투자자가 볼 것은 어느 한쪽의 독식보다 각 사업의 경쟁력입니다. 모델 회사는 고객이 계속 선택할 성능·편의성과 비용 효율을 갖췄는지, 클라우드 회사는 필요한 자원을 경쟁력 있는 가격에 공급하면서 비용을 감당하는지입니다. 상대방의 성장이 기회가 될 수 있지만, 자신의 이익까지 대신 보장해주지는 않습니다.

## 정리

챗GPT와 클로드의 뒤에는 두 가지 사업이 있습니다. **고객에게 AI 서비스를 파는 사업과, 그 서비스를 돌릴 컴퓨팅을 공급하는 사업**입니다.

OpenAI·앤트로픽이 클라우드에 비용을 낸다고 돈을 못 버는 구조는 아닙니다. 실제 서비스 매출을 올리고 있으며, 이익을 남기려면 컴퓨팅과 연구개발 등 전체 비용을 감당해야 합니다. 클라우드 회사 역시 매출에서 장비·시설 운영 비용을 감당해야 합니다.

따라서 “AI 회사는 적자고 빅테크만 돈을 번다”는 식으로 나눌 일이 아닙니다. **AI 수요가 두 사업에 기회를 만들고, 각 회사가 그 기회를 이익으로 바꾸는 능력은 따로 확인해야 합니다.**

그다음에는 돈을 내는 고객에게 질문이 돌아갑니다. 이 서비스를 도입한 기업은 지출한 비용보다 더 큰 효과를 얻고 있을까요? [4편에서는 메타·아마존 등의 시도와 AI 도입 효과](/p/ai-adoption-roi/)를 살펴봤습니다.

---

자료 확인일: **2026년 10월 8일**. OpenAI의 3월 매출 발표, 앤트로픽의 5월 연환산 매출 발표, AWS의 2분기 실적은 시점과 기준이 다릅니다. 최신 매출 순위나 같은 기간의 수익성 비교로 사용하지 않았습니다. 본문에 인용한 매출 발표만으로 두 모델 회사의 현재 순이익을 확정하지 않았습니다.

> ⚠️ 이 글은 AI를 활용해 투자 관련 내용을 공부하며 정리한 글입니다. 특정 종목이나 투자 방식에 대한 권유가 아니며, 내용에 오류가 있거나 최신 정보와 다를 수 있습니다. 실제 투자 전에는 공식 자료를 직접 확인하시기 바랍니다. 투자 판단과 그 결과에 대한 책임은 투자자 본인에게 있습니다.
