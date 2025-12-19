"""
中文文档的额外配置文件
覆盖基础配置以支持中文本地化
"""

# 修改语言设置
language = 'zh_CN'

# 修改项目标题
project = "Litestar 中文文档"
html_title = "Litestar 中文文档"
html_short_title = "Litestar"

# 修改版权信息为中文
current_year = __import__('datetime').datetime.now().year
copyright = f"{current_year}, Litestar 贡献者"
author = "Litestar 组织"

# 中文本地化设置
html_context = html_context.copy() if 'html_context' in globals() else {}
html_context.update({
    'current_language': 'zh',
    'language': 'zh_CN',
    'doc_lang': 'zh',
    'languages': [
        ('zh', '中文'),
        ('en', 'English')
    ],
    'language_links': {
        'zh': '/zh/',
        'en': '/'
    },
    # 更新导航为中文
    'nav_links': [
        {"title": "首页", "url": "index"},
        {
            "title": "社区",
            "children": [
                {
                    "title": "贡献指南",
                    "summary": "了解如何为 Litestar 项目做出贡献",
                    "url": "contribution-guide",
                    "icon": "contributing",
                },
                {
                    "title": "行为准则",
                    "summary": "回顾与 Litestar 社区互动的礼仪",
                    "url": "https://github.com/litestar-org/.github?tab=coc-ov-file",
                    "icon": "coc",
                },
                {
                    "title": "安全",
                    "summary": "Litestar 安全协议概述",
                    "url": "https://github.com/litestar-org/.github?tab=coc-ov-file#security-ov-file",
                    "icon": "coc",
                },
            ],
        },
        {
            "title": "关于",
            "children": [
                {
                    "title": "Litestar 组织",
                    "summary": "关于 Litestar 组织的详细信息",
                    "url": "https://litestar.dev/about/organization",
                    "icon": "org",
                },
                {
                    "title": "发布说明",
                    "summary": "探索 Litestar 的发布过程、版本控制和弃用策略",
                    "url": "https://litestar.dev/about/litestar-releases",
                    "icon": "releases",
                },
            ],
        },
        {
            "title": "发布说明",
            "children": [
                {
                    "title": "3.0 新功能",
                    "url": "release-notes/whats-new-3",
                    "summary": "探索 Litestar 3.0 的新功能",
                },
                {
                    "title": "3.x 更新日志",
                    "url": "release-notes/changelog",
                    "summary": "3.x 系列的所有变更",
                },
                {
                    "title": "2.x 更新日志",
                    "url": "https://docs.litestar.dev/2/release-notes/changelog.html",
                    "summary": "2.x 系列的所有变更",
                },
            ],
        },
        {
            "title": "帮助",
            "children": [
                {
                    "title": "Discord 帮助论坛",
                    "summary": "专门的 Discord 帮助论坛",
                    "url": "https://discord.gg/litestar",
                    "icon": "coc",
                },
                {
                    "title": "GitHub 讨论",
                    "summary": "GitHub 讨论",
                    "url": "https://github.com/orgs/litestar-org/discussions",
                    "icon": "coc",
                },
                {
                    "title": "Stack Overflow",
                    "summary": "我们在 Stack Overflow 上监控 <code><b>litestar</b></code> 标签",
                    "url": "https://stackoverflow.com/questions/tagged/litestar",
                    "icon": "coc",
                },
            ],
        },
        {"title": "赞助", "url": "https://github.com/sponsors/Litestar-Org", "icon": "heart"},
    ]
})

# 主题选项更新
html_theme_options = html_theme_options.copy() if 'html_theme_options' in globals() else {}
html_theme_options.update({
    'logo_target': '/zh/',
})

# 设置中文字体支持（如果需要）
# html_css_files = html_css_files + ['custom.css'] if 'html_css_files' in globals() else ['custom.css']