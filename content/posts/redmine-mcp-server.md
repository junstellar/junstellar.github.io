---
title: "Redmine MCP 서버 직접 만들기 — 일주일의 기록"
slug: "redmine-mcp-server"
date: 2026-06-29T22:00:00+09:00
draft: false
categories: ["AI"]
tags: ["MCP", "ClaudeCode", "Python", "Redmine", "MCP서버"]
---

> 💻 **바로 설치:** `pipx install git+https://github.com/junstellar/redmine-mcp-jun.git`

Claude Code가 사내 Redmine을 직접 읽고 쓰게 만들고 싶었다. 그런데 우리 Redmine은 사설망에 있어 Atlassian·GitHub 같은 외부 SaaS 커넥터를 못 쓴다. 그래서 내 PC에서만 도는 로컬 MCP 서버를 직접 만들었다. 단일 파일에서 시작해 pip 패키지로 키운 일주일의 기록이다.

## MCP가 뭔지, 도구를 어떻게 짰나

MCP(Model Context Protocol)는 'AI와 외부 도구를 잇는' 표준이다. USB처럼, 표준만 맞추면 어떤 도구든 LLM에 꽂아 쓸 수 있다.

서버를 클라이언트에 붙이는 방식은 크게 둘이다. **stdio**는 서버를 사용자 PC에서 로컬 프로세스로 띄워 같은 PC 안에서만 주고받는 방식이고, **HTTP(원격)**는 서버를 따로 호스팅해 네트워크로 붙는 방식이다. 원격 방식은 한 번 띄워두면 여러 명이 같이 쓰기 좋지만, 서버 운영과 인증·키 관리를 따로 챙겨야 한다. 나는 사내에서 내가 직접 설치해 쓸 거라, 키가 내 PC 밖으로 안 나가고 설치도 간단한 **stdio 방식**으로 했다.

내가 만들 Redmine 연동에서 코드보다 먼저 한 일은 "LLM이 이걸로 뭘 할 수 있어야 하나"를 적어보는 거였다. 막상 적어보니 평소 Redmine에서 하는 일이 그리 많지 않았다 — 내 일감 확인, 이슈 검색·열람, 이슈 만들기, 댓글 달기, 위키 보고 고치기 정도. 거기에 맞춰 도구 10개를 추렸다.

| 도구 | 역할 |
|---|---|
| `list_projects` / `list_issues` / `get_issue` | 프로젝트·이슈 조회 |
| `create_issue` / `add_comment` | 이슈 생성·댓글 |
| `list_wiki_pages` / `get_wiki` / `update_wiki` | 위키 |
| `get_my_today` | '오늘 내 일감' 단축 |
| `list_enumerations` | 우선순위·상태 ID |

여기서 하나 배웠다. `get_my_today`처럼 자주 쓰는 흐름은 전용 도구로 빼두면 LLM이 훨씬 잘 골라 쓴다. 그리고 만들면서 챙긴 세 가지 — 도구 설명은 풍부하게(짧으면 엉뚱한 걸 부른다), 입력 스키마는 빡빡하게, 응답은 JSON 그대로 넘기기.

## 진짜 어려운 건 코드가 아니라 배포였다

처음엔 파일 하나(약 420줄)로 빠르게 동작부터 확인했다. 정작 시간을 잡아먹은 건 "남 PC에 어떻게 깔지"였다. OS별 경로 분기에, Python 3.12의 PEP 668로 `pip install`이 막히는 환경까지 겹쳤다. 결국 pip 패키지로 갈아엎고 pipx 설치로 정리하니, 어느 OS든 두 줄로 끝났다.

가장 신경 쓴 건 Claude 설정 파일(`.claude.json`)을 건드리는 부분이었다. 다른 MCP 설정도 같이 든 공유 파일이라, 수정 전 무조건 백업을 뜨게 했다(실제로 한 번 사고 났는데 바로 복구됐다). 실행 경로도 `python` 대신 절대경로로 박아 파이썬 버전이 바뀌어도 안 깨지게 했다.

| 막힘 | 해결 |
|---|---|
| PEP 668로 `pip install` 거부 | pipx로 전환 |
| 파이썬 업그레이드 후 MCP 안 뜸 | 실행 명령을 절대경로로 |
| 설정 머지하다 다른 항목 날림 | 수정 전 백업 강제 |
| LLM이 단축 도구 안 부르고 우회 | description에 키워드 보강 |

## 정리

MCP 서버 만들기 자체는 의외로 쉽다(파이썬 400줄). 어려운 건 *배포*, *키 관리*, 그리고 *LLM이 잘 골라 쓰게 만드는 description 튜닝* — 이 셋이다. 미리 고민하고 들어가면 며칠이면 된다.

필요한 사람을 위해 코드는 레포에 올려뒀으니([github.com/junstellar/redmine-mcp-jun](https://github.com/junstellar/redmine-mcp-jun), MIT) 받아 써도 된다. 그래도 한 번쯤은 **직접 만들어보는 걸 추천한다.** 새 일감이 등록되면 알려주는 알림, 들어온 일감을 자동으로 분석해 회신 댓글을 다는 봇처럼 — 자기한테 필요한 걸 직접 붙여보면 훨씬 많이 남는다.
