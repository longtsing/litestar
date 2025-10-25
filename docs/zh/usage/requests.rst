请求
=====

Litestar 支持多种请求数据获取方式，包括路径参数、查询参数、请求体、表单、文件上传等。

- 路径参数：通过 URL 路径直接获取。
- 查询参数：通过 URL 查询字符串获取。
- 请求体：支持 JSON、表单、文件等多种格式。

示例：

.. code-block:: python

    from litestar import get

    @get("/items/{item_id}")
    def get_item(item_id: int, q: str = None) -> dict:
        return {"item_id": item_id, "q": q}
