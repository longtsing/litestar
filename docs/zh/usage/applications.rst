应用程序
=============

应用对象
-------------------

每个 Litestar 应用程序的核心是 :class:`~litestar.app.Litestar` 类的实例。通常，这段代码会放在项目根目录下名为 ``main.py``、``app.py``、``asgi.py`` 或类似的文件中。

这些入口点也会在 :ref:`CLI 自动发现 <usage/cli:autodiscovery>` 期间使用。

创建应用程序很简单 - 唯一必需的 :term:`参数 <argument>` 是一个包含 :class:`控制器 <.controller.Controller>`、:class:`路由器 <.router.Router>` 或 :class:`路由处理器 <.handlers.BaseRouteHandler>` 的 :class:`列表 <list>`：

.. literalinclude:: /examples/hello_world.py
    :language: python
    :caption: 一个简单的 Hello World Litestar 应用

应用实例是应用的根级别 - 它的基础路径为 ``/``，所有根级别的 :class:`控制器 <.controller.Controller>`、:class:`路由器 <.router.Router>` 和 :class:`路由处理器 <.handlers.BaseRouteHandler>` 都应该在其上注册。

.. seealso:: 要了解更多关于注册路由的信息，请查看文档中的这一章节：

    * :ref:`路由 - 注册路由 <usage/routing/overview:Registering Routes>`

启动和关闭
--------------------

您可以向 :class:`应用实例 <litestar.app.Litestar>` 的 :paramref:`~litestar.app.Litestar.on_startup` / :paramref:`~litestar.app.Litestar.on_shutdown` :term:`关键字参数 <argument>` 传递一个 :term:`可调用对象 <python:callable>` 列表 - 可以是同步或异步函数、方法或类实例。这些会在 ASGI 服务器（如 `uvicorn <https://www.uvicorn.org/>`_、`Hypercorn <https://hypercorn.readthedocs.io/en/latest/#/>`_、`Granian <https://github.com/emmett-framework/granian/>`_、`Daphne <https://github.com/django/daphne/>`_ 等）发出相应事件时按顺序调用。

.. mermaid::

   flowchart LR
       Startup[ASGI-事件: lifespan.startup] --> on_startup
       Shutdown[ASGI-事件: lifespan.shutdown] --> on_shutdown

这方面的经典用例是数据库连接。通常，我们希望在应用启动时建立数据库连接，然后在关闭时优雅地关闭它。

例如，让我们使用 `SQLAlchemy <https://docs.sqlalchemy.org/en/latest/orm/extensions/asyncio.html>`_ 的异步引擎创建数据库连接。我们创建两个函数，一个用于获取或建立连接，另一个用于关闭它，然后将它们传递给 :class:`~litestar.app.Litestar` 构造函数：

.. literalinclude:: /examples/startup_and_shutdown.py
    :language: python
    :caption: 启动和关闭事件示例
