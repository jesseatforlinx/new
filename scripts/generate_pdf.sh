#!/usr/bin/env bash
set -e

if [ ! -s changed_md_files.txt ]; then
    echo "未检测到md文档变化, 不生成PDF。"
    exit 0
fi

# 遍历变更的 md 文件，定位对应目录
while read -r file; do
    dir=$(dirname "$file")
    if [ -f "$dir/conf.py" ]; then
        echo "Building PDF for $dir"
        outdir="docs_build/${dir#platform/}"

        rm -rf "$dir/_build/latex"
        sphinx-build -M latexpdf "$dir" "$dir/_build"

        mkdir -p "$outdir/_static"
        cp "$dir/_build/latex"/*.pdf "$outdir/_static/"
        echo "PDF copied to $outdir/_static"
    fi
done < changed_md_files.txt
