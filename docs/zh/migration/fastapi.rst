从 Starlette / FastAPI 迁移
------------------------

路由装饰器
~~~~~~~~~~~~~~~~~~

Litestar 不在 ``Router`` 或 ``Litestar`` 实例中包含任何装饰器。
相反，所有路由都使用 :doc:`路由处理器 </usage/routing/handlers>` 声明，可以是独立函数或
控制器方法。然后可以在应用程序或路由器实例上注册处理器。

.. tab-set::

    .. tab-item:: FastAPI
        :sync: fastapi

        .. code-block:: python

            from fastapi import FastAPI


            app = FastAPI()


            @app.get("/")
            async def index() -> dict[str, str]: ...

    .. tab-item:: Starlette
        :sync: starlette


        .. code-block:: python

            from starlette.applications import Starlette
            from starlette.routing import Route


            async def index(request): ...


            routes = [Route("/", endpoint=index)]

            app = Starlette(routes=routes)

    .. tab-item:: Litestar
        :sync: litestar

        .. code-block:: python

           from litestar import Litestar, get


           @get("/")
           async def index() -> dict[str, str]: ...


           app = Litestar([index])


..  seealso::

    要了解有关注册路由的更多信息，请查看文档中的本章：

    * :ref:`路由 - 注册路由 <usage/routing/overview:registering routes>`

路由器和路由
~~~~~~~~~~~~~~~~~~

Litestar 和 Starlette 的 ``Router`` 类之间有几个关键区别：

1. Litestar 版本不是 ASGI 应用程序
2. Litestar 版本不包含装饰器：使用 :doc:`路由处理器 </usage/routing/handlers>`。
3. Litestar 版本不支持生命周期挂钩：这些必须在应用程序层处理。请参阅 :doc:`生命周期挂钩 </usage/lifecycle-hooks>`

如果您正在使用 Starlette 的 ``Route``，则需要将它们替换为 :doc:`路由处理器 </usage/routing/handlers>`。

基于主机的路由
~~~~~~~~~~~~~~~~~~

有意不支持基于主机的路由类。如果您的应用程序依赖于 ``Host``，您将必须将逻辑分离到不同的服务中，并使用像 `nginx <https://www.nginx.com/>`_ 或 `traefik <https://traefik.io/>`_ 这样的代理服务器来处理这部分请求分派。

依赖注入
~~~~~~~~~~~~~~~~~~~~

Litestar 依赖注入系统与 FastAPI 使用的系统不同。您可以在文档的 :doc:`依赖注入 </usage/dependency-injection>` 部分阅读相关内容。

在 FastAPI 中，您将依赖项声明为传递给 ``Router`` 或 ``FastAPI`` 实例的函数列表，或作为包装在 ``Depends`` 类实例中的默认函数参数值。

在 Litestar 中，**依赖项始终使用字典声明**，其中键是字符串，值包装在 ``Provide`` 类的实例中。这也允许在应用程序的每个级别透明地覆盖依赖项，并轻松访问更高级别的依赖项。

.. tab-set::

    .. tab-item:: FastAPI
        :sync: fastapi
