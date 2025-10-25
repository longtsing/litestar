进阶用法
=========

本教程介绍 Litestar 的进阶功能，包括依赖注入、中间件、路由分组等。

- **依赖注入**：通过参数注入服务或配置。
- **中间件**：实现请求/响应处理的自定义逻辑。
- **路由分组**：组织大型应用的路由结构。

示例：

.. code-block:: python

    from litestar import Litestar, get, Middleware

    def my_middleware(request, call_next):
        # 处理请求前逻辑
        response = call_next(request)
        # 处理响应后逻辑
        return response

    @get("/items/{item_id}")
    def get_item(item_id: int) -> str:
        return f"Item: {item_id}"

    app = Litestar(route_handlers=[get_item], middleware=[Middleware(my_middleware)])

更多高级用法请参考官方文档。