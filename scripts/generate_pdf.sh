#!/usr/bin/env bash
set -e

if [ ! -s changed_md_files.txt ]; then
    echo "No markdown changes found, skip PDF generation."
    exit 0
fi

while read -r file; do
    dir=$(dirname "$file")
    base=$(basename "$file" .md)

    if [ -f "$dir/conf.py" ]; then
        echo "Building PDF for $file"

        outdir="docs_build/${dir#platform/}"
        builddir="$dir/_build"

        # 清理旧构建
        rm -rf "$builddir/latex"
        sphinx-build -M latexpdf "$dir" "$builddir"

        pdf_out="$builddir/latex"/*.pdf
        if [ -f $pdf_out ]; then
            mkdir -p "$outdir/_static"
            # 复制并重命名为 {md文件名}.pdf
            cp "$pdf_out" "$outdir/_static/${base}.pdf"
            echo "PDF copied to $outdir/_static/${base}.pdf"
        else
            echo "⚠️ No PDF generated for $file"
        fi
    else
        echo "⚠️ No conf.py found for $dir"
    fi
done < changed_md_files.txt
