# known-pitfalls.md

같은 에러가 두 번 발생하면 여기에 기록한다. 작업 시작 전, 특히 git/worktree/MCP를
건드리는 작업 전에는 먼저 이 파일부터 훑어본다.

## git / worktree

- **worktree를 만들 때는 로컬 `main`이 최신인지 먼저 확인할 것.** `.claude/skills/`처럼
  untracked가 아니라 git에 커밋된 파일이어도, 로컬 `main`이 `origin/main`보다 뒤처져
  있으면 `git worktree add ... main`이 그 오래된 스냅샷으로 만들어져서 최신 파일(예:
  스킬 파일)이 빠진 채로 생성된다. 항상 `git checkout main && git pull` 먼저.
- **같은 브랜치를 두 worktree에 동시에 체크아웃할 수 없다.** 여러 worktree를 만들 때는
  서로 다른 브랜치 이름을 쓴다 (`main`처럼 이미 어딘가 물려있을 수 있는 브랜치는 피할 것).
- **untracked 파일은 새 worktree로 안 따라온다.** `git worktree add`는 커밋된(tracked)
  내용만 새 작업 디렉터리로 가져온다. 프로젝트 스킬처럼 여러 worktree에서 공유해야
  하는 파일은 반드시 git에 커밋해둔다 (`.gitignore`로 로컬 전용 파일만 따로 뺀다).

## MCP

- **`npx` vs `uvx` 구분.** Node/npm 기반 MCP 서버(`playwright` 등)는 `npx`로 실행하지만,
  Python 기반 서버(예: 공식 `fetch` reference 서버인 `mcp-server-fetch`)는 PyPI 패키지라
  `uvx`로 실행해야 한다. `npx`로 등록하면 "Failed to connect"가 뜬다.
- **MCP 서버 이름/경로가 실제 패키지 이름과 겹치면 안 된다.** 로컬 폴더 이름을 `mcp/`로
  만들면 `from mcp.server.fastmcp import FastMCP`가 pip으로 설치한 진짜 `mcp` 패키지
  대신 그 로컬 폴더를 가리켜버린다 (`import mcp; mcp.__file__`이 `None`이면 이 문제다).
- **MCP 서버는 세션 시작 시점에 로드된다.** `claude mcp add`로 새로 등록하거나 스킬
  파일을 고친 뒤에는, 기존 대화창이 아니라 `claude`를 완전히 새로 시작해야 반영된다.
- **트리거 확인은 명시적으로.** 간단한 계산(예: 47+89)은 도구 없이도 답할 수 있어서,
  도구가 실제로 호출됐는지 확인하려면 "add 도구 써서"처럼 도구 이름을 명시해서
  물어봐야 한다.
- **`/` 슬래시는 CLI 내장 명령어 조회다.** 등록 안 된 이름 앞에 `/`를 붙이면(`/ship-feature`
  같은 프로젝트 스킬) 모델한테 가지도 않고 바로 "Unknown command"가 뜬다. 프로젝트
  스킬은 슬래시 없이 자연어로 설명해서 description 매칭으로 트리거해야 한다.

## E2E 테스트 전 체크리스트

- 동일 증상 재발 방지를 위해, 큰 작업 전에는 이 파일부터 훑고 시작한다.
