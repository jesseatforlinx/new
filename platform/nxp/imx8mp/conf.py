# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'NXP IMX8MP Documentation'
author = 'Forlinx Embedded'
copyright = 'Forlinx Embedded'
# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser', 'sphinxcontrib.images'         # 支持 Markdown
]

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

# PDF生成设置 --------------------------------------->

latex_engine = 'xelatex'

latex_documents = [
('hardware',	             # (修改) 文件名，无后缀
'hardware.tex',              # (修改) 与文件名保持一致，后缀.tex不变
'FETMX8MP-SMARC OKMX8MP-SMARC',             # (修改) PDF说明书封面标题
'User\'s Software Manual',   # (修改) 文档类别 "User's Software Manual / Application Note等"
'manual',                    # (不修改) 文档类别，不修改
False),

('linux-manual',
'linux-manual.tex',
'FETMX6ULL-C OKMX6ULL-C',
'Application Note',
'manual',
False)
]

latex_elements = {
    'classoptions': ',openany',     # 关闭新章节仅在奇数页
    'preamble': r'''
    
    \usepackage{fontspec}
    \usepackage{xeCJK}
    \usepackage{graphicx}
    \usepackage{tikz}
    \usepackage{xcolor}
    \usepackage{geometry}
    \geometry{a4paper, left=2cm, right=2cm, top=2cm, bottom=2cm}

    \setcounter{secnumdepth}{0}  % 关闭自动章节编号
    \setcounter{tocdepth}{2}    % 目录层级
    \renewcommand{\thechapter}{}

    \setmainfont{DejaVu Serif}

    % 定义封面所需的命令（如果您的文档类需要）
    \makeatletter
    \newcommand{\customtitle}{\@title}
    \newcommand{\customauthor}{\@author}
    \newcommand{\customdate}{\@date}
    \makeatother
    ''',

    'maketitle': r'''
    \begin{titlepage}
    \thispagestyle{empty}

    % 定义封面蓝条颜色
    \definecolor{forlinxblue}{RGB}{0, 102, 178}

    \begin{tikzpicture}[remember picture, overlay]

      % --- 左侧窄条 (上半部)：用于竖排文字
      \fill[forlinxblue] 
        (current page.north west) rectangle ++(2cm, -0.32\paperheight);

      % --- 左侧宽条 (下半部)：作为装饰块
      \fill[forlinxblue] 
        (current page.south west) 
        rectangle ++(2cm, 0.58\paperheight);

      % --- 竖排文字：垂直居中于上窄条
      \node[
        white,
        rotate=270,
        font=\bfseries\huge,
        anchor=center
      ] 
      at ([xshift=1cm,yshift=-0.15\paperheight]current page.north west) 
      {\customauthor};

       % --- LOGO ---
      \node[anchor=north east] 
        at ([xshift=-2cm, yshift=-2cm]current page.north east) 
        {\includegraphics[width=6cm]{../../source/_static/logo.png}};

      % --- 产品型号 ---
      \node[anchor=north west, font=\huge\bfseries]
        at ([yshift=-10.5cm, xshift=2.1cm]current page.north west) 
        {\customtitle};

      % --- 子标题 ---
      \node[anchor=north west, font=\large]
        at ([yshift=-11.5cm, xshift=2.1cm]current page.north west)
        {Embedded Development Platform};

      % --- 文档标题 ---
      \node[anchor=north east, font=\LARGE\bfseries]
        at ([yshift=-15cm, xshift=-2cm]current page.north east)
        {\customauthor};

      % --- 版本号 ---
      \node[anchor=north east, font=\normalsize]
        at ([yshift=-16cm, xshift=-2cm]current page.north east)
        {Rev. 1.1};

      % --- 公司信息 左对齐 + 右对齐 ---
      \node[anchor=south west, font=\normalsize]
        at ([xshift=3cm, yshift=2cm]current page.south west)
        {Forlinx Embedded Technology Co. Ltd.};

      \node[anchor=south east, font=\normalsize]
        at ([xshift=-2cm, yshift=2cm]current page.south east)
        {www.forlinx.net};

    \end{tikzpicture}
    \end{titlepage}
    '''
}


