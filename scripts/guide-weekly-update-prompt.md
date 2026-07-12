# 마비노기 모바일 공략 서재 주간 갱신 작업 (문서용)

> 실제 자동 실행은 Claude 스케줄드 태스크 2개가 담당한다:
> - `mabi-guide-weekly-collect` (매주 월 00:10): 수집·갱신·정제까지만. **커밋·푸시 금지 (반자동 B안)**
> - `mabi-guide-monday-notify` (매주 월 08:01): 결과를 푸시 알림
> 배포는 사용자가 검토 후 "공략 갱신분 올려줘"라고 지시할 때만 수행한다.
> 태스크 원본: C:\Users\sj861\.claude\scheduled-tasks\

## 목표
`C:\Project\Blog\static\tools\mabi-guide\` 의 직업별 공략집 HTML을 최근 1주일치 에반 갤러리 여론으로 갱신한다. (배포는 별도 승인)

## 절차

### 1. 수집
- 대상: 디시인사이드 에반(마비노기 모바일) 마이너 갤러리 `https://gall.dcinside.com/mgallery/board/lists/?id=enban`
- 방법: curl + UA 헤더(`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36`)로 검색 URL 호출:
  `.../lists/?id=enban&s_type=search_subject_memo&s_keyword=<URL인코딩 키워드>`
- 주의: 이 검색은 키워드당 최근 ~20건만 반환한다. 직업별로 키워드를 여러 개 던져 합집합을 만든다.
- 직업별 기본 키워드(각각 "X", "X 룬", "X 세공" 3종 이상): 사제, 힐러, 수도(수도사), 음유, 악사, 댄서, 검술, 대검, 기사, 검방, 도적, 듀블, 격투(격가), 궁수, 석궁, 장궁, 법사(빙창), 화법, 빙결, 전격, 암술
- 본문: 글 페이지의 write_div ~ "OutLink.renderOutLinkWarning" 사이 텍스트.
- 댓글: POST `https://gall.dcinside.com/board/comment/`, 헤더 `X-Requested-With: XMLHttpRequest` + `Referer: <글URL>`, 데이터 `id=enban, no=<글번호>, cmt_id=enban, cmt_no=<글번호>, e_s_n_o=<글 페이지의 hidden input 값>, comment_page=1, sort=D, _GALLTYPE_=M`. 닉네임 "댓글돌이"는 광고봇이므로 버린다.
- 출력은 반드시 UTF-8 파일로 저장 후 Read로 읽는다(콘솔 직접 출력 시 인코딩 깨짐).
- 지난 갱신 이후(최근 7일) 글만 대상으로 한다.

### 2. 판단·집필
- 직업별로 새 정보가 기존 공략집과 달라졌는지 판단한다(메타 변경, 세공/룬 정배 변화, 티어 반전, 신규 패치 등).
- 변화가 있는 직업의 HTML만 수정한다. 기존 문체·구조(한눈에 보는 결론 → 장 → 출처)를 유지하고, 새 근거 글은 출처 목록에 추가한다(글번호·링크 형식 동일).
- 변화가 없으면 그 직업은 건드리지 않는다.
- 수정한 권과 서재(index.html)의 "기준일" 표기를 오늘 날짜로 갱신한다.

### 3. 정제 (필수)
- 모든 수정 후 반드시 실행: `python C:\Project\Claude\공략집\_sanitize.py C:\Project\Blog\static\tools\mabi-guide`
- 실행 후 잔여 비속어 스캔(씨발/좆/병신/존나/새끼 등)에서 0건임을 확인한다. 새 표현이 나오면 _sanitize.py에 규칙을 추가하고 재실행한다.
- 이 블로그는 애드센스 수익화 대상이므로 비속어가 남으면 절대 안 된다.

### 4. 올인원 재생성
- 수정된 권이 1개라도 있으면: `C:\Project\Claude\공략집\` 원본에도 동일 수정 반영 후 `python C:\Project\Claude\공략집\_build_allinone.py` 실행, 산출물을 정제해 `static/tools/mabi-guide/allinone.html`로 복사한다(첫 줄에 `<meta name="robots" content="noindex">` 유지).

### 5. 배포
- `cd C:\Project\Blog && git pull --rebase` 후 변경 파일만 스테이징:
  `git add static/tools/mabi-guide`
- 커밋 메시지: `공략 서재 주간 갱신 (YYYY-MM-DD): <갱신된 직업 목록 또는 '변경 없음 확인'>`
- push. 변경이 전혀 없으면 커밋하지 않고 로그만 남긴다.

### 6. 로그
- `C:\blog-memo\_automation.log` 에 시작/갱신 직업/종료를 한 줄씩 기록한다.

## 금지사항
- 소개 포스트(content/posts/mabi-guide-library)는 수정하지 않는다.
- static/tools/mabi-guide 밖의 파일은 수정하지 않는다 (원본 공략집 폴더와 로그 제외).
- 근거 없는 내용을 지어내지 않는다. 자료가 없으면 "자료 없음"으로 둔다.
