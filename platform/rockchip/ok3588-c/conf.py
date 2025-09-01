# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Forlinx Embedded RK3588 Documentation'
author = 'Forlinx Embedded'
copyright = 'Forlinx Embedded'
# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',         # 支持 Markdown
    'sphinx_sitemap',      # 添加 sitemap 扩展
]
html_baseurl = "https://forlinxembedded.github.io/rockchip/ok3588-c/"


templates_path = ['_templates']
exclude_patterns = []

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

# Logo (如果有，放在 _static 目录)
html_logo = '_static/forlinx-logo.png'
html_favicon = '_static/forlinx.png'
html_theme_options = {
    'logo_only': True,
}

html_css_files = [
    'custom.css',
]

html_sidebars = {
    '**': [
        'globaltoc.html',
        'relations.html',
        'sourcelink.html',
        'searchbox.html',
        'footer.html',  # 👈 关键：显式加载我们自定义的 footer 模板
    ]
}

html_show_sourcelink = False

latex_engine = 'xelatex'

latex_elements = {
    
    'classoptions': ',openany',     # 关闭新章节仅在奇数页
    'preamble': r'''

    % 依赖包
    \usepackage{fontspec}   % 字体操作依赖包    
    \usepackage{xeCJK}      % 中文字体，特殊字体包
    \usepackage{graphicx}   % 画图包
    \usepackage{tikz}
    \usepackage{xcolor}
    \usepackage{geometry} 
    \usepackage{newunicodechar}
    
    % 遇到 emoji 等未知字符就替换为空
    \newunicodechar{📌}{}   % 这里你可以列几个常用 emoji
    \newunicodechar{🔗}{}
    \newunicodechar{⏳}{}
    
    ''',

    
}