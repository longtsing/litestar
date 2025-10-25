HTMX
====

Litestar `HTMX <https://htmx.org>`_ 集成。

HTMX 是一个 JavaScript 库，它使您可以直接在 HTML 中使用属性访问 AJAX、CSS Transitions、WebSockets 和服务器发送事件，因此您可以使用超文本的简单性和强大功能构建现代用户界面。

本节假设您具有 HTMX 的先验知识。
如果您想学习 HTMX，我们建议查阅他们的 `官方教程 <https://htmx.org/docs>`_。


HTMXPlugin
------------

Litestar 插件 ``HTMXPlugin`` 可用于轻松配置所有 Litestar 路由的默认请求类。

它可以通过 ``litestar[htmx]`` 包额外选项安装。

.. code-block:: python

    from litestar.plugins.htmx import HTMXPlugin
    from litestar import Litestar

    from litestar.contrib.jinja import JinjaTemplateEngine
    from litestar.template.config import TemplateConfig

    from pathlib import Path

    app = Litestar(
        route_handlers=[get_form],
        debug=True,
        plugins=[HTMXPlugin()],
        template_config=TemplateConfig(
            directory=Path("litestar_htmx/templates"),
            engine=JinjaTemplateEngine,
        ),
    )

有关可用属性的完整列表，请参阅 :class:`~litestar.plugins.htmx.HTMXDetails`。
