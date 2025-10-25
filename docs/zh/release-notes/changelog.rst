:orphan:

3.x 更新日志
=============

.. changelog:: 3.0.0
    :date: 2024-08-30

    .. change:: 移除所有 SQLAlchemy 模块，改为直接使用 advanced-alchemy 导入
        :type: 新功能
        :breaking:
        :pr: TBD

        移除 Litestar 中所有 SQLAlchemy 功能。`litestar.contrib.sqlalchemy` 和 `litestar.plugins.sqlalchemy` 模块已完全移除。用户现在必须直接从 `advanced_alchemy.extensions.litestar` 导入。

        迁移方式：
        - `from litestar.contrib.sqlalchemy import X` → `from advanced_alchemy.extensions.litestar import X`
        - `from litestar.plugins.sqlalchemy import Y` → `from advanced_alchemy.extensions.litestar import Y`

        这完成了关注点分离，advanced-alchemy 成为 Litestar SQLAlchemy 集成的唯一提供者。

    .. change:: 移除弃用的 `litestar.contrib.prometheus` 模块
        :type: 新功能
        :breaking:
        :pr: 4328
        :issue: 4305

        移除弃用的 `litestar.contrib.prometheus` 模块。仍在使用该模块的代码应切换到 `litestar.plugins.prometheus`。

    .. change:: `AsyncTestClient` 改为原生异步
        :type: 新功能
        :pr: 4291
        :issue: 1920
        :breaking:

        重新实现 :class:`~litestar.testing.AsyncTestClient`，使其原生异步，即使用当前运行的事件循环运行应用，而不是在新线程中运行单独的事件循环。新增 :class:`~litestar.testing.AsyncWebSocketTestSession`，为 WebSocket 提供异步测试工具。

        为确保 `TestClient` 和 `AsyncTestClient` 行为一致，所有测试工具均重写为异步优先，同步版本内部代理到异步实现，并在专用线程+事件循环中运行。

        .. seealso::
            :ref:`usage/testing:测试客户端`
            :ref:`usage/testing:如何选择测试客户端`

    .. change:: 移除 Litestar 的弃用插件属性
        :type: 新功能
        :pr: 4297
        :breaking:

        移除 :class:`Litestar` 的所有弃用 `<plugin_type>_plugins` 属性。

        ===================================  ===================================
        已移除                              替代方案
        ===================================  ===================================
        `Litestar.openapi_schema_plugins`  `Litestar.plugins.openapi_schema`
        `Litestar.cli_plugins`             `Litestar.plugins.cli`
        `Litestar.serialization_plugins`   `Litestar.serialization.cli`
        ===================================  ===================================

    .. change:: 移除弃用的 `allow_reserved` 和 `allow_empty_value` 属性
        :type: 新功能
        :pr: 4299
        :breaking:

        从 :class:`~litestar.datastructures.ResponseHeader` 和 :class:`~litestar.openapi.spec.OpenAPIHeader` 移除弃用的 `allow_reserved` 和 `allow_empty_value` 属性。

    .. change:: 移除弃用的 `traceback_line_limit` 参数
        :type: 新功能
        :breaking:
        :pr: 4300

        移除 :class:`~litestar.logging.config.LoggingConfig` 的 `traceback_line_limit` 参数。自 2.9.0 起该参数已无效，可安全移除。

    .. change:: 移除弃用的 `litestar.middleware.cors` 模块
        :type: 新功能
        :breaking:
        :pr: 4309

        移除弃用的 `litestar.middleware.cors` 模块和 `litestar.middleware.cors.CORSMiddleware`。请使用 :class:`~litestar.config.cors.CORSConfig` 配置 CORS 中间件。

    .. change:: 移除 ASGI 响应类和 `to_asgi_response` 方法的弃用参数 `encoded_headers`
        :type: 新功能
        :pr: 4311
        :breaking:

        从以下类中移除弃用的 `encoded_headers` 参数：
