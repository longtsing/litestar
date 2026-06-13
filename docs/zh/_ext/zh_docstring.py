"""zh_docstring - 通过旁路 JSON 缓存为 autodoc 抓取的 docstring 提供中文翻译。

不会修改 litestar 源码。sphinx 在 autodoc 抓取 docstring 后、
渲染前把英文 docstring 替换为缓存中的中文。

使用::

    # conf.py
    sys.path.insert(0, str(Path(__file__).parent / "_ext"))
    extensions.append("zh_docstring")

    # 缓存目录（相对于 conf.py 所在目录）
    ZH_DOCSTRING_CACHE = str(Path(__file__).parent / "_docstrings")
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path
from typing import Any

from sphinx.application import Sphinx
from sphinx.util.typing import ExtensionMetadata

__version__ = "0.2.0"

# 配置项名称（大写，符合 sphinx 惯例）
_CACHE_ROOT_CFG = "ZH_DOCSTRING_CACHE"
_FALLBACK_CFG = "ZH_DOCSTRING_FALLBACK"


# 全局缓存：{qn: translated_text}
_TRANSLATION_CACHE: dict[str, str] | None = None


def _load_all_caches(cache_root: Path) -> dict[str, str]:
    """加载所有 .zh.json 缓存到内存中。返回 {qualified_name: translated_text} 映射。"""
    if not cache_root.exists():
        return {}
    out: dict[str, str] = {}
    for p in cache_root.rglob("*.zh.json"):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if isinstance(data, dict):
            for qn, payload in data.items():
                if isinstance(payload, dict) and payload.get("text"):
                    out[qn] = payload["text"]
                elif isinstance(payload, str):
                    out[qn] = payload
    return out


def _ensure_loaded(app: Sphinx) -> dict[str, str]:
    global _TRANSLATION_CACHE
    if _TRANSLATION_CACHE is None:
        # 从配置中读取缓存目录，默认为 conf.py 所在目录下的 _docstrings
        conf_dir = Path(app.confdir)
        try:
            cache_root_str = app.config.get(_CACHE_ROOT_CFG, str(conf_dir / "_docstrings"))
        except Exception as e:
            print(f"[zh_docstring] 读取配置 {_CACHE_ROOT_CFG} 失败: {e}", file=sys.stderr)
            cache_root_str = str(conf_dir / "_docstrings")
        print(f"[zh_docstring] cache_root_str={cache_root_str!r}", file=sys.stderr)
        cache_root = Path(cache_root_str).resolve()
        _TRANSLATION_CACHE = _load_all_caches(cache_root)
        try:
            fallback = bool(app.config.get(_FALLBACK_CFG, True))
        except Exception:
            fallback = True
        app.env._zh_docstring_count = len(_TRANSLATION_CACHE)  # type: ignore[attr-defined]
        print(
            f"[zh_docstring] 已加载 {len(_TRANSLATION_CACHE)} 条翻译缓存 "
            f"(fallback={fallback})",
            file=sys.stderr,
        )
    return _TRANSLATION_CACHE


def _on_process_docstring(
    app: Sphinx, what: str, name: str, obj: Any, options: Any, lines: list[str]
) -> None:
    """autodoc-process-docstring 事件：替换 docstring 内容。"""
    cache = _ensure_loaded(app)
    translated = cache.get(name)
    if translated is None:
        return  # 找不到翻译，保持原文
    # 清空原 lines 并填入翻译内容
    lines.clear()
    lines.append(translated)

def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_config_value(_CACHE_ROOT_CFG, default="_docstrings", rebuild="env", types=[str])
    app.add_config_value(_FALLBACK_CFG, default=True, rebuild="env", types=[bool])

    app.connect("autodoc-process-docstring", _on_process_docstring)
    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
