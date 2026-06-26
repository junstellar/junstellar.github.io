<#
  memo-to-post.ps1
  -----------------
  C:\blog-memo 안의 새 메모(.md)를 Hugo 블로그 초안(draft) 글로 변환한다.
  매일 밤 11시 작업 스케줄러가 이 스크립트를 실행한다.

  동작 요약:
    1) PATH 갱신 후 git pull (두 PC 안전: 올리기 전 최신본 받아옴)
    2) C:\blog-memo\*.md 를 하나씩 content\posts\ 로 변환 (draft = true)
    3) 파일명이 겹치면 -2, -3 ... 붙여 둘 다 보존
    4) 처리한 메모는 _published\ 로 이동 (재처리 방지, 원본은 보존)
    5) 커밋/푸시는 하지 않는다 (공개는 사용자가 직접 "커밋해" 할 때)

  메모를 넣은 날만 글이 생긴다. 빈 폴더면 아무 일도 안 한다.
#>

$ErrorActionPreference = "Stop"

# ---- 경로 설정 ----------------------------------------------------------
$BlogDir   = "C:\Project\Blog"
$MemoDir   = "C:\blog-memo"
$PostsDir  = Join-Path $BlogDir "content\posts"
$DoneDir   = Join-Path $MemoDir "_published"
$LogFile   = Join-Path $MemoDir "_automation.log"

function Log($msg) {
    $line = "[{0}] {1}" -f (Get-Date -Format "yyyy-MM-dd HH:mm:ss"), $msg
    Write-Output $line
    Add-Content -Path $LogFile -Value $line -Encoding utf8
}

# 스케줄러는 새 환경에서 도니 PATH를 직접 채워 hugo/git을 찾게 한다
$env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" +
            [System.Environment]::GetEnvironmentVariable("Path","User")

Log "=== memo-to-post 시작 ==="

# ---- 폴더 준비 ----------------------------------------------------------
foreach ($d in @($PostsDir, $DoneDir)) {
    if (-not (Test-Path $d)) { New-Item -ItemType Directory -Path $d -Force | Out-Null }
}

# ---- 1) 최신본 받아오기 (remote 있을 때만, 실패해도 계속) ----------------
Set-Location $BlogDir
$hasRemote = (& git remote) -contains "origin"
if ($hasRemote) {
    try {
        & git pull --rebase --autostash 2>&1 | ForEach-Object { Log "git: $_" }
    } catch {
        Log "git pull 실패(무시하고 계속): $($_.Exception.Message)"
    }
} else {
    Log "원격(origin) 없음 - git pull 건너뜀"
}

# ---- 2) 메모 수집 (최상위 .md 만, _published 등 하위폴더 제외) ----------
$memos = @(Get-ChildItem -Path $MemoDir -Filter "*.md" -File -ErrorAction SilentlyContinue |
           Where-Object { $_.Name -notlike "_*" })

if ($memos.Count -eq 0) {
    Log "새 메모 없음 - 종료"
    Log "=== memo-to-post 끝 ==="
    return
}

Log "메모 $($memos.Count)개 발견"

# ---- 슬러그/제목 헬퍼 ---------------------------------------------------
function Get-Slug([string]$name) {
    # 파일명에서 .md 제거, 공백/특수문자 정리
    $s = [System.IO.Path]::GetFileNameWithoutExtension($name)
    $s = $s -replace "[\\/:*?""<>|]", "-"
    $s = $s -replace "\s+", "-"
    return $s.Trim("-")
}

# ---- 3) 변환 -----------------------------------------------------------
$created = 0
foreach ($memo in $memos) {
    try {
        $raw = Get-Content -Path $memo.FullName -Raw -Encoding utf8

        # 날짜: 파일명 앞 yyyy-MM-dd 패턴이 있으면 사용, 없으면 수정시각
        if ($memo.BaseName -match '^(\d{4}-\d{2}-\d{2})') {
            $dateStr = $matches[1]
            $dateObj = [datetime]::ParseExact($dateStr, "yyyy-MM-dd", $null)
        } else {
            $dateObj = $memo.LastWriteTime
        }
        $isoDate = $dateObj.ToString("yyyy-MM-ddTHH:mm:ssK")

        # 제목: 본문 첫 번째 H1(# ...) 있으면 사용, 없으면 파일명
        $title = $null
        foreach ($ln in ($raw -split "`n")) {
            if ($ln -match '^\s*#\s+(.+?)\s*$') { $title = $matches[1]; break }
        }
        if (-not $title) {
            $title = (Get-Slug $memo.Name) -replace '^\d{4}-\d{2}-\d{2}-?', ''
            if (-not $title) { $title = "메모" }
        }
        # 제목에 따옴표가 있으면 escape
        $titleEsc = $title -replace '"', '\"'

        # 대상 파일명 (슬러그) + 충돌 시 -2, -3 ...
        $slug = Get-Slug $memo.Name
        $target = Join-Path $PostsDir ("{0}.md" -f $slug)
        $n = 2
        while (Test-Path $target) {
            $target = Join-Path $PostsDir ("{0}-{1}.md" -f $slug, $n)
            $n++
        }

        # front matter + 본문
        $fm = @"
---
title: "$titleEsc"
date: $isoDate
draft: true
tags: []
---

"@
        Set-Content -Path $target -Value ($fm + $raw) -Encoding utf8
        Log "초안 생성: $(Split-Path $target -Leaf)  <-  $($memo.Name)"
        $created++

        # 4) 원본 메모는 _published 로 이동 (재처리 방지)
        $dest = Join-Path $DoneDir $memo.Name
        $dn = 2
        while (Test-Path $dest) {
            $dest = Join-Path $DoneDir ("{0}-{1}{2}" -f $memo.BaseName, $dn, $memo.Extension)
            $dn++
        }
        Move-Item -Path $memo.FullName -Destination $dest
    }
    catch {
        Log "오류 ($($memo.Name)): $($_.Exception.Message)"
    }
}

Log "초안 $created개 생성 완료. content\posts\ 에서 확인 후 커밋하면 공개됩니다."
Log "=== memo-to-post 끝 ==="
