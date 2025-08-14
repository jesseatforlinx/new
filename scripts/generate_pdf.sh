# 遍历所有平台目录
for dir in platform/*/*; do
  if [ -f "$dir/conf.py" ]; then
    echo "Building PDF for $dir"
    outdir="docs_build/${dir#platform/}"

    # 清空旧 PDF 构建目录
    rm -rf "$dir/_build/latex"

    # 构建 PDF
    sphinx-build -M latexpdf "$dir" "$dir/_build"

    # 找到生成的 PDF 并复制到 HTML 静态目录
    mkdir -p "$outdir/_static"
    cp "$dir/_build/latex"/*.pdf "$outdir/_static/"
    echo "PDF copied to $outdir/_static"
  fi
done
