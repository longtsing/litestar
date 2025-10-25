从 Flask 迁移
----------

ASGI 与 WSGI
~~~~~~~~~~~~

`Flask <https://flask.palletsprojects.com>`_ 是一个 WSGI 框架，而 Litestar
是使用现代 `ASGI <https://asgi.readthedocs.io>`_ 标准构建的。一个关键区别
是 *ASGI* 是为异步而构建的。

虽然 Flask 增加了对 ``async/await`` 的支持，但其核心仍然是同步的；
Flask 中的异步支持仅限于单个端点。
这意味着虽然您可以在 Flask 中使用 ``async def`` 定义端点，
**但它们不会并发运行** - 请求仍将一次处理一个。
Flask 通过为每个请求创建一个事件循环来处理异步端点，在其中运行
端点函数，然后返回其结果。

另一方面，ASGI 则完全相反；它在一个中央事件循环中运行所有内容。
然后，Litestar 通过在非阻塞方式下运行同步函数来增加对同步函数的支持
*在事件循环上*。这意味着同步和异步代码都可以并发运行。

路由
~~~~~~~

.. tab-set::

    .. tab-item:: Flask
        :sync: flask

        .. code-block:: python

            from flask import Flask


            app = Flask(__name__)


            @app.route("/")
            def index():
                return "Index Page"


            @app.route("/hello")
            def hello():
                return "Hello, World"


    .. tab-item:: Litestar
        :sync: litestar

        .. code-block:: python

            from litestar import Litestar, get


            @get("/")
            def index() -> str:
                return "Index Page"


            @get("/hello")
            def hello() -> str:
                return "Hello, World"


            app = Litestar([index, hello])


路径参数
^^^^^^^^^^^^^^^

.. tab-set::
    .. tab-item:: Flask
        :sync: flask

        .. code-block:: python

            from flask import Flask


            app = Flask(__name__)


            @app.route("/user/<username>")
            def show_user_profile(username):
                return f"User {username}"


            @app.route("/post/<int:post_id>")
            def show_post(post_id):
                return f"Post {post_id}"


            @app.route("/path/<path:subpath>")
            def show_subpath(subpath):
                return f"Subpath {subpath}"
