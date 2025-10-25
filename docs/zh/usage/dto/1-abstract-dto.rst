===========
AbstractDTO
===========

Litestar 维护一套 DTO 工厂类型，可用于为流行的数据建模库（如 ORM）创建 DTO。
这些工厂以模型类型作为泛型类型参数，并创建 
:class:`AbstractDTO <litestar.dto.base_dto.AbstractDTO>` 的子类型，
支持该模型类型与原始字节之间的转换。

以下工厂目前可用：

- :class:`DataclassDTO <litestar.dto.dataclass_dto.DataclassDTO>`
- :class:`MsgspecDTO <litestar.dto.msgspec_dto.MsgspecDTO>`
- :class:`PydanticDTO <litestar.plugins.pydantic.PydanticDTO>`
- :class:`SQLAlchemyDTO <advanced_alchemy.extensions.litestar.dto.SQLAlchemyDTO>`

使用 DTO 工厂
-------------

DTO 工厂用于为特定的数据建模库创建 DTO。以下示例为 SQLAlchemy 模型创建 DTO：

.. literalinclude:: /examples/data_transfer_objects/factory/simple_dto_factory_example.py
    :caption: SQLAlchemy 模型 DTO
    :language: python

这里我们看到 SQLAlchemy 模型被用作处理器的 ``data`` 和返回注解，
虽然 Litestar 本身不支持对 SQLAlchemy 模型进行编码/解码，
但通过 :class:`SQLAlchemyDTO <advanced_alchemy.extensions.litestar.dto.SQLAlchemyDTO>` 我们可以做到这一点。

.. _dto-marking-fields:

标记字段
--------

:func:`dto_field <litestar.dto.field.dto_field>` 函数可用于标记具有基于 DTO 配置的模型属性。

标记为 ``"private"`` 或 ``"read-only"`` 的字段不会从客户端数据解析到用户模型中，
``"private"`` 字段永远不会序列化到返回数据中。

.. literalinclude:: /examples/data_transfer_objects/factory/marking_fields.py
    :caption: 标记字段
    :language: python
    :emphasize-lines: 6,14,15
    :linenos:

排除字段
--------

可以使用 :class:`DTOConfig <litestar.dto.config.DTOConfig>` 显式排除字段。

以下示例演示从序列化响应中排除属性，包括从嵌套模型中排除字段。

.. literalinclude:: /examples/data_transfer_objects/factory/excluding_fields.py
    :caption: 排除字段
    :language: python
    :emphasize-lines: 6,10,37-46,49
    :linenos:

这里，配置使用 exclude 参数创建，它是一组字符串。每个字符串表示应从输出 DTO 中排除的 ``User`` 对象中字段的路径。

重命名字段
----------

可以使用 :class:`DTOConfig <litestar.dto.config.DTOConfig>` 重命名字段。
以下示例在客户端使用名称 ``userName``，在内部使用 ``user``。

.. literalinclude:: /examples/data_transfer_objects/factory/renaming_fields.py
    :caption: 重命名字段
    :language: python
    :emphasize-lines: 4,8,19,20,24
    :linenos:

也可以使用将应用于所有字段的重命名策略来重命名字段。
以下示例使用预定义的重命名策略，该策略将所有字段名称转换为客户端的驼峰命名。

.. literalinclude:: /examples/data_transfer_objects/factory/renaming_all_fields.py
    :caption: 重命名所有字段
    :language: python
    :emphasize-lines: 4,8,19,20,21,22,24
    :linenos:

重命名策略接受预定义策略之一："camel"、"pascal"、"upper"、"lower"、"kebab"，
或者可以提供接受字段名称作为字符串参数并应返回字符串的回调。

类型检查
--------

工厂检查分配给它们的类型是否是作为泛型类型提供给 DTO 工厂的类型的子类。

.. literalinclude:: /examples/data_transfer_objects/factory/type_checking.py
    :caption: 类型检查
    :language: python
    :emphasize-lines: 25,26,31
    :linenos:

嵌套字段
--------

可以使用 :class:`DTOConfig <litestar.dto.config.DTOConfig>` 的 ``max_nested_depth`` 参数
控制从客户端数据解析和序列化到返回数据的相关项的深度。

.. literalinclude:: /examples/data_transfer_objects/factory/related_items.py
    :caption: 相关项
    :language: python
    :emphasize-lines: 25,35,39
    :linenos:

处理未知字段
------------

默认情况下，DTO 将静默忽略源数据中的未知字段。
可以使用 :class:`DTOConfig <litestar.dto.config.DTOConfig>` 的 ``forbid_unknown_fields`` 参数配置此行为。
设置为 ``True`` 时，如果数据包含模型上未定义的字段，将返回验证错误响应：

.. literalinclude:: /examples/data_transfer_objects/factory/unknown_fields.py
    :caption: 未知字段
    :language: python
    :linenos:


DTO Data
--------

有时我们需要能够访问 DTO 已解析和验证的数据，但不转换为数据模型的实例。

.. literalinclude:: /examples/data_transfer_objects/factory/dto_data_usage.py
    :language: python
    :emphasize-lines: 5,23,25
    :linenos:

在上面的示例中，我们将 :class:`DTOData <litestar.dto.data_structures.DTOData>` 的实例注入到处理器中，
并使用它在使用服务器生成的 ``id`` 值增强客户端数据后创建 ``User`` 实例。

.. _dto-create-instance-nested-data:

为嵌套数据提供值
~~~~~~~~~~~~~~~~

要增强用于实例化模型实例的数据，我们可以向 
:meth:`create_instance() <litestar.dto.data_structures.DTOData.create_instance>` 方法提供关键字参数。

.. literalinclude:: /examples/data_transfer_objects/factory/providing_values_for_nested_data.py
    :language: python
    :emphasize-lines: 9-12,20,28,34
    :linenos>

双下划线语法 ``address__id`` 作为关键字参数传递给 
:meth:`create_instance() <litestar.dto.data_structures.DTOData.create_instance>` 方法调用，
用于为嵌套属性指定值。

DTO 工厂和 PATCH 请求
----------------------

`PATCH <https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH>`_ 请求是数据传输对象的特殊情况。
原因是我们需要能够接受和验证客户端有效负载中模型属性的任何子集。

.. literalinclude:: /examples/data_transfer_objects/factory/patch_requests.py
    :language: python
    :emphasize-lines: 7,20,27,28,30
    :linenos:

``PatchDTO`` 类为 ``Person`` 类定义。``config`` 属性设置为排除 ``id`` 字段，
``partial`` 属性设置为 ``True``，这允许 DTO 接受模型属性的子集。

隐式私有字段
------------

以下划线开头命名的字段默认被视为"私有"。
这意味着它们不会从客户端数据解析，也不会序列化到返回数据中。

.. literalinclude:: /examples/data_transfer_objects/factory/leading_underscore_private.py
    :language: python
    :linenos:

可以通过将 
:attr:`DTOConfig.underscore_fields_private <litestar.dto.config.DTOConfig.underscore_fields_private>` 
属性设置为 ``False`` 来覆盖此行为。

包装返回数据
------------

Litestar 的 DTO 工厂类型足够通用，可以管理您的数据，即使它嵌套在泛型包装器中。

.. literalinclude:: /examples/data_transfer_objects/factory/enveloping_return_data.py
    :caption: 包装返回数据
    :language: python
    :linenos:

使用 Litestar 的分页类型
-------------------------

Litestar 提供分页响应包装器类型，DTO 工厂类型可以开箱即用地处理这一点。

.. literalinclude:: /examples/data_transfer_objects/factory/paginated_return_data.py
    :caption: 分页返回数据
    :language: python
    :linenos:

将 Litestar 的 Response 类型与 DTO 工厂一起使用
----------------------------------------------

Litestar 的 DTO 工厂类型可以处理包装在 ``Response`` 类型中的数据。

.. literalinclude:: /examples/data_transfer_objects/factory/response_return_data.py
    :caption: Response 包装的返回数据
    :language: python
    :linenos:
