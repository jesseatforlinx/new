#!/usr/bin/env bash
set -e

echo "::group::Detect changed .md files"
echo "GITHUB_EVENT_BEFORE=${GITHUB_EVENT_BEFORE:-unset}"
echo "GITHUB_SHA=${GITHUB_SHA:-unset}"

# 确保有完整 git 历史
git fetch --unshallow || true
git fetch origin main || true

# 检测变更 .md 文件
if [ "$GITHUB_EVENT_BEFORE" = "0000000000000000000000000000000000000000" ] || [ -z "$GITHUB_EVENT_BEFORE" ]; then
  echo "⚠️  GITHUB_EVENT_BEFORE 无效，用 HEAD^ 作为对比基准"
  changed=$(git diff --name-only HEAD^ $GITHUB_SHA | grep "\.md$" || true)
else
  echo "✅ 使用范围: $GITHUB_EVENT_BEFORE → $GITHUB_SHA"
  changed=$(git diff --name-only $GITHUB_EVENT_BEFORE $GITHUB_SHA | grep "\.md$" || true)
fi

echo "变更的 .md 文件:"
echo "$changed"
echo "$changed" > changed_md_files.txt

echo "--- changed_md_files.txt 内容 ---"
cat changed_md_files.txt || echo "⚠️ 没有检测到任何变更"
echo "::endgroup::"
