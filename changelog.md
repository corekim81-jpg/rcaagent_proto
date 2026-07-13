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
