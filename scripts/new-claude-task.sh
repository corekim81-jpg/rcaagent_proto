#!/usr/bin/env bash
# 배치 위치: scripts/new-claude-task.sh
#
# 로컬 터미널을 벗어나지 않고 GitHub 클라우드 자동화(claude-auto-task.yml)를
# 트리거하는 이슈를 생성합니다. gh CLI(https://cli.github.com/)가 설치·로그인
# 되어 있어야 합니다 (gh auth login).
#
# 사용법:
#   ./scripts/new-claude-task.sh "제목" "요청 내용을 자유롭게 적기"
#
# 예:
#   ./scripts/new-claude-task.sh "add /health endpoint" \
#     "GET /health 는 200과 {\"status\": \"ok\"} 를 반환해야 한다. 테스트도 작성."

set -euo pipefail

if [ $# -lt 1 ]; then
  echo "사용법: $0 \"제목\" [\"본문\"]" >&2
  exit 1
fi

TITLE="$1"
BODY="${2:-요청 내용을 이슈 본문에 채워주세요.}"

if ! command -v gh >/dev/null 2>&1; then
  echo "gh CLI가 설치되어 있지 않습니다. https://cli.github.com/ 참고." >&2
  exit 1
fi

gh issue create \
  --title "[Claude] ${TITLE}" \
  --body "${BODY}" \
  --label claude-task

echo "이슈가 생성되었습니다. GitHub Actions에서 자동으로 처리를 시작합니다."
