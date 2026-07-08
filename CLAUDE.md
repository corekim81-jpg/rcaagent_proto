# 프로젝트 규칙 (Claude Code 자동화용)

이 파일은 GitHub Actions에서 실행되는 Claude Code(및 로컬 Claude Code)가 따라야 할
프로젝트 규칙을 정의합니다. 배치 위치: 저장소 루트 `CLAUDE.md`.

## 언어/스택
- Python 3.12

## 개발 방식
- TDD를 따른다: 기능 구현 전 실패하는 테스트를 먼저 작성한다.
- 테스트 프레임워크: `pytest`
- 린터: `ruff` (`ruff check .`)

## 커밋 전 필수 체크
커밋하기 전 아래 두 명령이 모두 통과해야 한다. 하나라도 실패하면 커밋하지 않고 원인을
수정한 뒤 다시 검사한다.

```bash
ruff check .
pytest
```

## 커밋 / PR 규칙
- 커밋 메시지는 무엇을, 왜 바꿨는지 한 줄로 명확히 쓴다.
- 이슈에서 트리거된 작업은 커밋 메시지 또는 PR 본문에 `Closes #<issue-number>` 를 포함해
  머지 시 이슈가 자동으로 닫히도록 한다.
- `main` 브랜치에는 직접 push하지 않는다 (branch protection으로 강제 권장).

## 디렉터리 규칙
- (프로젝트 구조가 잡히면 여기에 소스/테스트 디렉터리 규칙을 추가하세요.)

## 두 가지 작업 방식

이 프로젝트는 로컬 작업과 클라우드(GitHub Actions) 자동화를 함께 씁니다. 둘 다 이
CLAUDE.md 규칙과 동일한 lint/test 기준(`ruff check .`, `pytest`)을 따릅니다.

### 1) 로컬 (VSCode / 터미널)
직접 붙어서 봐야 하는 작업, 복잡한 리팩터링 등 상시 작업에 사용합니다.

```bash
git clone https://github.com/corekim81-jpg/rcaagent_proto.git
cd rcaagent_proto
claude              # 터미널에서 Claude Code 실행 (VSCode 통합 터미널에서도 동일)
```

커밋 전에는 항상 아래로 CI와 동일한 검사를 미리 돌린다:

```bash
./scripts/check.sh
```

### 2) 클라우드 (GitHub 이슈 -> 자동 PR)
범위가 명확하고 리스크 낮은 작업, 자리를 비웠을 때 맡겨두는 작업에 사용합니다.
GitHub에서 "Claude Task" 템플릿으로 이슈를 만들거나(`claude-task` 라벨 자동 적용),
로컬 터미널을 벗어나지 않고 아래 스크립트로도 트리거할 수 있습니다 (gh CLI 필요):

```bash
./scripts/new-claude-task.sh "add /health endpoint" \
  "GET /health 는 200과 {\"status\": \"ok\"} 를 반환해야 한다. 테스트도 작성."
```

이슈가 만들어지면 `.github/workflows/claude-auto-task.yml`이 브랜치 생성 -> TDD 구현
-> lint/test -> 커밋 -> PR 오픈까지 GitHub 서버에서 자동으로 처리한다. 사람은 PR을
검토하고 merge하기만 하면 된다.
