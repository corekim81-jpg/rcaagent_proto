# changelog.md

중요한 마일스톤만 남긴다. `handoff.md`에서 10개 넘어가 지워지기 전에, 계속 참고할
가치가 있는 내용은 여기로 옮겨온다.

## 완료된 마일스톤

- **프로젝트 규칙 확립**: `CLAUDE.md`에 TDD, `ruff`/`pytest` 커밋 전 필수 체크,
  로컬/클라우드 두 가지 작업 방식 정의.
- **클라우드 자동화 구축**: `.github/workflows/claude-auto-task.yml` — 이슈에
  `claude-task` 라벨이 붙으면 GitHub Actions에서 브랜치-구현-PR까지 자동 처리.
- **`ship-feature` 스킬 도입**: 로컬 세션에서 이슈 생성부터 PR까지 자동화하는
  프로젝트 스킬을 만들고, git에 커밋해서 모든 브랜치/worktree에서 쓸 수 있게 함
  (`.claude/skills/ship-feature/SKILL.md`).
- **git worktree 병렬 작업 검증**: 서로 다른 기능(`is_even`, `reverse_string`)을
  두 개의 worktree에서 동시에 진행해 브랜치 전환 없이 병렬로 이슈~PR까지 완료됨을
  확인.
- **MCP 연결 실습**: `fetch`(공식 reference 서버, `uvx`로 실행)와 `demo_mcp.py`
  (직접 만든 FastMCP 최소 서버)를 각각 `claude mcp add`로 연결해 도구 호출까지 확인.
- **문서 세트 + today/handoff 스킬 도입**: `plan.md`/`to-do.md`/`changelog.md`/
  `known-pitfalls.md`/`handoff.md`를 추가하고, 이를 실제로 읽고/쓰는 `today`(세션 시작
  브리핑)·`handoff`(세션 마무리 기록) 스킬을 만들어 세션 간 맥락 단절을 줄임.
- **Claude Code harness 3종 실습**: Context7/Serena MCP 연결에 더해, hooks
  (`PostToolUse`로 커밋 전 `ruff check .` 자동 실행), 권한 allow/deny(셸 문법 차이로
  인한 오탐 포함), 백그라운드 작업/Task 서브에이전트까지 직접 설정하고 검증함.
