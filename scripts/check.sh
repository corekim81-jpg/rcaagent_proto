#!/usr/bin/env bash
# 배치 위치: scripts/check.sh
#
# 로컬에서 CI(ci.yml)와 동일한 lint/test 검사를 실행합니다.
# 로컬에서 Claude Code(또는 직접) 작업 후 커밋하기 전에 실행해서
# GitHub Actions에서 실패하지 않도록 미리 확인하는 용도입니다.
#
# 사용법: ./scripts/check.sh

set -euo pipefail

echo "==> pip install (ruff, pytest, 프로젝트 의존성)"
python -m pip install --upgrade pip >/dev/null
pip install ruff pytest >/dev/null
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
if [ -f pyproject.toml ]; then pip install -e . || true; fi

echo "==> ruff check ."
ruff check .

echo "==> pytest"
pytest

echo "==> 모두 통과했습니다. 커밋해도 좋습니다."
