---
title: "구글, 제미나이 3.5 플래시에 '컴퓨터 유즈' 내장… \"성능은 GPT급, 가격은 3분의 1\""
description: "구글이 제미나이 3.5 플래시에 화면을 직접 보고 클릭·입력하는 '컴퓨터 유즈'를 기본 내장했다. 관찰·판단·실행을 반복하는 자동화 에이전트 기능을 정리했다."
slug: "gemini-3-5-flash-computer-use"
date: 2026-06-28T10:00:00+09:00
draft: true
categories: ["AI 트렌드"]
tags: ["AI", "구글", "제미나이", "컴퓨터유즈"]
---

구글이 지난 6월 24일 자사 생성형 AI 모델 '제미나이 3.5 플래시(Gemini 3.5 Flash)'에 화면을 직접 보고 조작하는 '컴퓨터 유즈(Computer Use)' 기능을 기본 내장한다고 발표했다. 별도의 전용 모델을 거치지 않고 주력 모델 자체가 브라우저·모바일·데스크톱 화면을 인식해 클릭과 입력을 수행하는 형태로, 현재 퍼블릭 프리뷰 단계로 제공된다.

컴퓨터 유즈는 AI가 화면을 스크린샷처럼 캡처해 인식한 뒤, 화면 속 버튼이나 입력창 같은 UI 요소를 판단하고 해당 좌표를 실제로 클릭·입력하는 기능이다. 관찰(observe)·판단(think)·실행(act) 과정을 반복하며 사람이 컴퓨터로 수행하는 작업을 대신한다. 구글은 이 기능을 통해 개발자가 브라우저뿐 아니라 모바일·데스크톱 환경에서 작동하는 자동화 에이전트를 만들 수 있다고 설명했다.

다만 화면 조작 기능 자체가 새로운 것은 아니다. 앞서 앤트로픽이 2024년 10월 클로드(Claude)에 '컴퓨터 유즈'를 도입했고, 오픈AI도 2025년 초 '오퍼레이터(Operator)'로 유사 기능을 선보인 바 있다. 구글 역시 그동안 'Gemini 2.5 Computer Use'라는 별도 모델로 관련 기능을 제공해 왔다. 이번 발표의 핵심은 기능의 신규성이 아니라, 별도 모델로 분리돼 있던 기능을 주력 Flash 모델에 통합하고 100만 토큰 규모의 컨텍스트와 결합했다는 점이다. 이로써 연속 소프트웨어 테스트 등 장시간 자동화 작업에 활용도가 높아졌다는 평가다.

업계의 관심이 집중된 부분은 성능 대비 가격이다. 구글에 따르면 제미나이 3.5 플래시는 컴퓨터 조작 성능 평가인 'OSWorld Verified' 벤치마크에서 78.4%를 기록해 경쟁 모델인 GPT-5.5와 유사한 수준을 보였다. 반면 이용 요금은 입력·출력 모두 약 3분의 1 수준으로 책정됐다.

| 항목 | Gemini 3.5 Flash (Computer Use) | GPT-5.5 |
|---|---|---|
| 컴퓨터 조작 | 본체에 네이티브 내장 | 지원 (Operator 계열) |
| OSWorld Verified 벤치 | 78.4% | 약 79%대(근접) |
| 입력 가격 (100만 토큰) | $1.50 | $5.00 |
| 출력 가격 (100만 토큰) | $9.00 | $30.00 |
| 컨텍스트 | 100만 토큰 | — |
| 조작 범위 | 브라우저·모바일·데스크톱 | 주로 브라우저 |

이 같은 가격 경쟁력으로 인해 발표 직후 국내외 기술 콘텐츠 제작자들이 실전 테스트 영상을 잇따라 공개하며 화제가 되고 있다. 초최신 주제로 검색 유입이 집중되는 시점인 데다, '성능은 대등하고 가격은 3분의 1'이라는 직관적 구도, 그리고 오픈AI·앤트로픽·구글 간 경쟁 구도가 맞물린 결과로 분석된다. 같은 날 구글은 크롬용 제미나이에 화면 영역을 지정하는 'Select from screen' 기능도 함께 추가했다.

보안 측면에서 구글은 프롬프트 인젝션 공격을 막기 위한 적대적 학습을 적용했으며, 민감하거나 되돌릴 수 없는 작업에 대해서는 사용자 확인을 요구하는 선택적 안전장치를 제공한다고 밝혔다.

한편 해당 기능은 현재 정식 출시(GA)가 아닌 퍼블릭 프리뷰 단계로, 구글은 정식 전환 시점을 공식적으로 밝히지 않았다. Gemini API 체인지로그에도 'preview'로 표기돼 있어, 실제 고객 데이터나 결제가 수반되는 업무에 적용하기 전에는 현재 상태를 재확인할 필요가 있다는 지적이 나온다. 기능은 Gemini API와 Gemini Enterprise Agent Platform을 통해 이용할 수 있다.

---

출처: [구글 공식 블로그](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-computer-use-gemini-3-5-flash/) · [Gemini API 체인지로그](https://ai.google.dev/gemini-api/docs/changelog) · [TechTimes (6/25)](https://www.techtimes.com/articles/319071/20260625/gemini-computer-use-baked-gemini-35-flash-screen-control-now-pairs-search-maps.htm) · [9to5Google (6/24)](https://9to5google.com/2026/06/24/gemini-chrome-select-screen/) · [The Next Web](https://thenextweb.com/news/google-gemini-3-5-flash-computer-use-built-in-tool)
