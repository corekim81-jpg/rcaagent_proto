# handoff.md

최근 세션 요약. 최근 10개만 남기고 가장 오래된 것부터 지운다. 계속 참고할 가치가
있는 중요한 내용은 지우기 전에 `changelog.md`로 옮긴다.

## 세션 기록

1. **MCP 도구 테스트** — `mcp__demo__add` 도구를 로드하고 47 + 89 = 136 계산 (2026-07-13).
2. **문서 세트 도입** — `plan.md`/`to-do.md`/`changelog.md`/`known-pitfalls.md`/
   `handoff.md`를 추가하고 `CLAUDE.md`에 언제 읽고/쓰는지 규칙을 추가함.
3. **MCP 실습 완료** — `fetch`(uvx), `demo_mcp.py`(직접 작성한 FastMCP 서버, `add` 도구)
   둘 다 `claude mcp add`로 연결하고 실제 도구 호출까지 확인함. 중간에 `npx` vs `uvx`,
   폴더명이 `mcp` 패키지와 겹치는 문제를 겪음 (`known-pitfalls.md` 참고).
4. **git worktree 병렬 작업 실습** — `is_even`, `reverse_string`을 서로 다른 worktree에서
   동시에 이슈~PR까지 진행. 이후 로컬 `main`이 오래돼서 새 worktree에 스킬 파일이
   빠지는 문제를 겪고 fast-forward로 해결함.
5. **`ship-feature` 스킬 개선** — 처음엔 이슈 없이 브랜치+PR만 하도록 만들었다가,
   사용자 요청으로 이슈 생성 단계를 추가하고, "매번 PR까지 해달라고 말 안 해도
   기본값으로 끝까지 진행"하도록 description을 더 적극적으로 고침.
