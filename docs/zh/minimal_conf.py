"""
最小化 Sphinx 配置，用于快速构建中文文档
"""

import os
from pathlib import Path

# 基本信息
project = "Litestar 中文文档"
author = "Litestar 贡献者"
language = "zh_CN"
html_title = "Litestar 中文文档"

# 版本信息
release = "3.0"

# Sphinx 扩展 - 只包含必要的
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinxcontrib.mermaid",
    "sphinx_click",
    "sphinx_paramlinks",
    "sphinx_togglebutton",
]

# 排除模式
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# 主题
html_theme = "default"
html_static_path = ["_static"]

# 交叉引用映射
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# 模板路径
templates_path = ["_templates"]