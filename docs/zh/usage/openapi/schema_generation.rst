-----------------------------
配置 Schema 生成
-----------------------------

OpenAPI schema 生成默认启用。要配置它，您可以使用 ``openapi_config`` kwarg 
将 :class:`OpenAPIConfig <.openapi.OpenAPIConfig>` 的实例传递给 :class:`Litestar <litestar.app.Litestar>` 类：

.. code-block:: python

   from litestar import Litestar
   from litestar.openapi import OpenAPIConfig

   app = Litestar(
       route_handlers=[...], openapi_config=OpenAPIConfig(title="My API", version="1.0.0")
   )



禁用 Schema 生成
++++++++++++++++

如果您希望禁用 schema 生成并且不在 API 中包含 schema 端点，只需将 ``None`` 作为 ``openapi_config`` 的值传递：

.. code-block:: python

   from litestar import Litestar

   app = Litestar(route_handlers=[...], openapi_config=None)



在路由处理器上配置 Schema 生成
---------------------------------

默认情况下，为所有路由处理器生成 `operation <https://spec.openapis.org/oas/latest.html#operation-object>`_ schema。
您可以通过设置 ``include_in_schema=False`` 从 schema 中省略路由处理器：

.. code-block:: python

   from litestar import get


   @get(path="/some-path", include_in_schema=False)
   def my_route_handler() -> None: ...

您还可以使用以下 kwargs 修改路由处理器生成的 schema：

``tags``
    与 `tag 规范 <https://spec.openapis.org/oas/latest.html#tag-object>`_ 相关的字符串列表。

``security``
    与 `security requirements 规范 <https://spec.openapis.org/oas/latest.html#securityRequirementObject>`_ 
    相关的字典列表。

``summary``
    用于路由 schema *summary* 部分的文本。

``description``
    用于路由 schema *description* 部分的文本。

``response_description``
    用于路由响应 schema *description* 部分的文本。

``operation_class``
    :class:`Operation <.openapi.spec.operation.Operation>` 的子类，
    可用于完全自定义处理器的 `operation object <https://spec.openapis.org/oas/v3.1.0#operation-object>`_。

``operation_id``
    返回字符串的字符串或可调用对象，用作路由 schema *operationId* 的标识符。

``deprecated``
    一个布尔值，指示是否应在 OpenAPI schema 中将此路由标记为已弃用。默认为 ``False``。

``raises``
    从 ``litestar.HttpException`` 扩展的异常类列表。

``responses``
    附加状态代码及其预期内容描述的字典。

.. code-block:: python

   from datetime import datetime
   from typing import Optional

   from pydantic import BaseModel

   from litestar import get
   from litestar.openapi.datastructures import ResponseSpec


   class Item(BaseModel): ...


   class ItemNotFound(BaseModel):
       was_removed: bool
       removed_at: Optional[datetime]


   @get(
       path="/items/{pk:int}",
       responses={
           404: ResponseSpec(
               data_container=ItemNotFound, description="Item was removed or not found"
           )
       },
   )
   def retrieve_item(pk: int) -> Item: ...


在代码中访问 OpenAPI Schema
----------------------------

OpenAPI schema 在 :class:`Litestar <litestar.app.Litestar>` 应用程序的 init 方法期间生成。
一旦 init 完成，就可以通过 ``app.openapi_schema`` 访问它：

.. code-block:: python

   from litestar import Request, get


   @get(path="/")
   def my_route_handler(request: Request) -> dict:
       schema = request.app.openapi_schema
       return schema.to_schema()


自定义 Pydantic 模型 Schema
----------------------------

您可以按照 `Pydantic 文档 <https://docs.pydantic.dev/latest/usage/json_schema/>`_ 
中的指南自定义为 pydantic 模型生成的 OpenAPI schema。

此外，您可以通过在模型上设置名为 ``__schema_name__`` 的特殊 dunder 属性来影响 pydantic 模型如何转换为 OpenAPI ``components``：

.. literalinclude:: /examples/openapi/customize_pydantic_model_name.py
    :caption: 自定义 Components 示例
    :language: python

.. attention::

   如果您使用多个在 schema 中使用相同名称的 pydantic 模型，
   您需要使用 ``__schema_name__`` dunder 来确保每个模型在 schema 中都有唯一的名称，
   否则 schema components 将是不明确的。


自定义 ``Operation`` 类
-------------------------

您可以通过创建 :class:`Operation <.openapi.spec.operation.Operation>` 的子类来自定义生成的 OpenAPI schema 中用于路径的 
`operation object <https://spec.openapis.org/oas/v3.1.0#operation-object>`_。

.. literalinclude:: /examples/openapi/customize_operation_class.py
    :caption: 自定义 Components 示例
    :language: python


生成示例
--------

Litestar 可以自动为 schema 的 ``example`` 部分生成示例。
要启用此功能，您需要安装 `polyfactory <https://polyfactory.litestar.dev/>`_ 库，
它作为包额外包含在 ``litestar[polyfactory]`` 和 ``litestar[full]`` 中。

安装后，您可以通过 OpenAPI config 启用示例生成：

.. literalinclude:: /examples/openapi/customize_pydantic_model_name.py
    :language: python
