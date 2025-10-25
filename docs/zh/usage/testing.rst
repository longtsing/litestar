测试
=====

Litestar 提供同步与异步测试客户端，支持单元测试与集成测试。

- TestClient：同步测试。
- AsyncTestClient：异步测试。

示例：

.. code-block:: python

    from litestar import Litestar, get
    from litestar.testing import TestClient

    @get("/")
    def hello() -> str:
        return "你好，测试!"

    app = Litestar(route_handlers=[hello])

    def test_hello():
        client = TestClient(app)
        response = client.get("/")
        assert response.text == "你好，测试!"
