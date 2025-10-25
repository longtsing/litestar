OpenAPI
=======

Litestar 自动生成 OpenAPI 文档，支持自定义 schema、UI 插件等。

- 默认启用 OpenAPI 3.1 文档。
- 可通过 OpenAPIConfig 配置文档信息、端点、插件。
- 支持多种 UI（如 Swagger、Scalar）。

示例：

.. code-block:: python

    from litestar import Litestar, OpenAPIConfig

    app = Litestar(
        route_handlers=[],
        openapi_config=OpenAPIConfig(title="API 示例", version="1.0.0")
    )
