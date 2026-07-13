# plan.md

전체 그림. 자주 안 바뀜 — 바뀌면 여기부터 고친다.

## 이 저장소가 뭐 하는 곳인가

Claude Code(로컬 대화형 + GitHub Actions 자동화)로 작업하는 방식을 실험하고 정착시키는
연습용 저장소. 실제 기능의 가치보다 **워크플로우 자체**(TDD, 이슈-브랜치-PR 흐름,
스킬, worktree 병렬 작업, MCP 연결)를 검증하는 게 목적이다.

## 두 가지 작업 방식 (CLAUDE.md 참고)

1. **로컬**: `ship-feature` 스킬(`.claude/skills/ship-feature/SKILL.md`)로 이슈 생성 →
   브랜치 → TDD → lint/test → 커밋 → 푸시 → PR을 한 세션 안에서 전부 처리.
2. **클라우드**: GitHub 이슈에 `claude-task` 라벨이 붙으면
   `.github/workflows/claude-auto-task.yml`이 GitHub Actions에서 동일한 흐름을 대신 처리.

## 지금까지 쌓인 것

- 작은 유틸 함수들 (`add`, `average`/`median`, `count_words`, `is_palindrome`,
  `is_even`, `reverse_string`, `is_prime`, `flatten`) — 전부 TDD로 작성, 각자 이슈+PR로
  들어옴. 새 함수 추가 요청은 기본적으로 이 패턴을 따른다.
- `app.py`: `/version` 엔드포인트 하나 있는 최소 Flask 앱.
- `.claude/skills/ship-feature/`: 로컬 워크플로우 자동화 스킬 (git에 커밋됨 — 모든
  브랜치/worktree에 자동으로 딸려온다).
- `demo_mcp.py`: FastMCP로 만든 최소 MCP 서버 예제 (`add` 도구 하나).

## 앞으로 방향

- 정해진 큰 로드맵은 없음 — 이 저장소는 "다음에 뭘 실험해볼까"를 계속 추가해가는
  연습장에 가깝다. 실제로 무엇을 할지는 `to-do.md`를 본다.
