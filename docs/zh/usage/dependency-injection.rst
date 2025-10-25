依赖注入
=========

Litestar 支持依赖注入，可自动为处理器注入服务、配置等。

- 通过参数类型声明依赖。
- 支持单例、工厂、作用域等多种依赖生命周期。

示例：

.. code-block:: python

    from litestar import Litestar, get, Provide

    def get_config() -> dict:
        return {"env": "prod"}

    @get("/env")
    def env(config: dict) -> str:
        return f"当前环境: {config['env']}"

    app = Litestar(route_handlers=[env], dependencies={"config": Provide(get_config)})
