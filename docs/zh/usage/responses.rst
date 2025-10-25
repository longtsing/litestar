响应
=====

Litestar 支持多种响应类型，包括字符串、字典、JSON、文件下载等。

- 默认返回字符串或字典会自动转换为 JSON 响应。
- 可自定义响应头、状态码、内容类型。
- 支持文件流式响应。

示例：

.. code-block:: python

    from litestar import get, Response

    @get("/text")
    def text_response() -> str:
        return "纯文本响应"

    @get("/json")
    def json_response() -> dict:
        return {"message": "JSON 响应"}

    @get("/custom")
    def custom_response() -> Response:
        return Response(content="自定义响应", media_type="text/plain", status_code=201)
