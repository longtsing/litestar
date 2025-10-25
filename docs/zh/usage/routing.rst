路由
=====

Litestar 支持灵活的路由定义方式，可通过装饰器或路由分组组织应用结构。

- 使用 `@get`、`@post`、`@put` 等装饰器定义处理器。
- 支持路径参数、查询参数、请求体等多种参数类型。
- 可通过 `Router` 类实现路由分组。

示例：

.. code-block:: python

    from litestar import Litestar, get, Router

    @get("/hello/{name}")
    def hello(name: str) -> str:
        return f"你好, {name}!"

    router = Router(path="/api", route_handlers=[hello])
    app = Litestar(route_handlers=[router])
