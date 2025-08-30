#!/usr/bin/env bash
set -e

if [ ! -s changed_md_files.txt ]; then
    echo "No markdown changes found, skip PDF generation."
    exit 0
fi

while read -r file; do
    md_file="$file"
    dir=$(dirname "$md_file")
    base=$(basename "$md_file" .md)

    if [ -f "$dir/conf.py" ]; then
        echo "📄 Building PDF for $md_file"

        # 清理旧的 latex 构建目录
        rm -rf "$dir/_build/latex"

        # 生成 latex 并编译成 pdf
        sphinx-build -M latexpdf "$dir" "$dir/_build"

        # 找到生成的 PDF 文件（一般是 project 名字.pdf）
        gen_pdf=$(find "$dir/_build/latex" -maxdepth 1 -name "*.pdf" | head -n 1)

        if [ -n "$gen_pdf" ] && [ -f "$gen_pdf" ]; then
            outdir="docs_build/${dir#platform/}/_static"
            mkdir -p "$outdir"
            
            # 重命名为和 md 文件同名
            final_pdf="$outdir/${base}.pdf"
            cp "$gen_pdf" "$final_pdf"
            echo "✅ PDF copied to $final_pdf"
        else
            echo "⚠️ No PDF generated for $md_file"
        fi
    else
        echo "ℹ️ No conf.py found in $dir, skip PDF build."
    fi
done < changed_md_files.txt
