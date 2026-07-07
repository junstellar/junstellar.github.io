# 🚀 AI 게임 랩 (static/games)

혼자 · AI로 · 공개빌드로 만드는 브라우저 미니게임 모음.
접속 주소: **https://junstellar.github.io/games/**

`static/` 아래라 Hugo 빌드 없이 그대로 서빙됩니다.

## 새 게임 추가하는 법 (2단계)

1. **`_template/` 폴더를 복사**해 `<게임id>/` 로 이름 바꾸기 (예: `2048/`)
2. **`games.js` 배열에 한 줄 추가**:
   ```js
   { id:"2048", title:"2048", emoji:"🔢", desc:"한 줄 설명", tags:["퍼즐"], status:"live", accent:"#4f8cff" }
   ```
   → 허브(`index.html`)에 카드가 자동으로 뜬다. **`id` 는 폴더 이름과 같아야 함.**

`status`: `"live"`(플레이 가능) | `"wip"`(준비중 — 잠긴 카드로 표시)

## 구조

| 파일 | 역할 |
|------|------|
| `index.html` | 허브. `games.js`를 읽어 카드 그리드를 자동 생성 |
| `games.js`   | **게임 목록. 여기만 고치면 됨** |
| `shared.css` | 공통 테마(허브+모든 게임) |
| `share.js`   | 공통 결과 공유 기능 — `window.GameShare` |
| `stats.js`   | 공통 기록(누적 점수·연속 출석) — `window.GameStats` (localStorage, 계정 없음) |
| `_template/` | 새 게임 시작용 복붙 뼈대 |
| `<id>/`      | 게임별 폴더(자체 완결형 HTML) |

## 공유 기능 (바이럴 내장)

게임이 끝나면 이렇게 부르면 됩니다:
```js
GameShare.share({
  text: "🎨 ... 4/5\n" + GameShare.grid([true,true,false,true,true]),
  url:  "https://junstellar.github.io/games/<id>/"
});
```
`navigator.share` 지원 시 네이티브 공유, 아니면 클립보드 복사 + 토스트 알림.
`GameShare.grid([true,false,...])` → `"🟩🟥..."` 이모지 그리드 문자열.

## 이미지 게임(guess-image) 이미지 넣는 법

문제 이미지는 로컬 GPU(ComfyUI / draw-local 스킬)로 뽑아
`guess-image/img/` 에 넣는다. 파일명은 `guess-image/index.html` 의
`ROUNDS` 배열 `img` 경로와 맞춘다.
이미지가 없어도 "준비중" placeholder가 떠서 게임은 정상 작동한다.
