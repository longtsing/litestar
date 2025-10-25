快速入门
=========

本教程将带你快速体验 Litestar 的基本用法。

1. 安装 Litestar：

   .. code-block:: shell

      pip install litestar

2. 创建第一个应用：

   .. code-block:: python

      from litestar import Litestar, get

      @get("/")
      def hello_world() -> str:
          return "你好，Litestar!"

      app = Litestar(route_handlers=[hello_world])

3. 运行应用：

   .. code-block:: shell

      python -m litestar

4. 在浏览器访问 http://127.0.0.1:8000/，你将看到 "你好，Litestar!"。

更多内容请参考进阶教程。