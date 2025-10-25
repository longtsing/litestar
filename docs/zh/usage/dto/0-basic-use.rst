=========
基本使用
=========

这里我们演示如何为路由处理器声明 DTO 类型。出于演示目的，我们假设我们正在使用数据模型 ``User``，
并且已经在应用程序中创建了两个 DTO 类型：``UserDTO`` 和 ``UserReturnDTO``。

DTO 层参数
~~~~~~~~~~

在 Litestar 应用程序的每个 :ref:`层 <layered-architecture>` 上，
有两个参数控制负责从处理器接收和返回数据的 DTO：

- ``dto``：此参数描述将用于解析入站数据的 DTO，该数据将作为处理器的 ``data`` 关键字参数注入。
  此外，如果处理器上没有声明 ``return_dto``，这也将用于编码处理器的返回数据。
- ``return_dto``：此参数描述将用于编码从处理器返回的数据的 DTO。
  如果未提供，则使用 ``dto`` 参数描述的 DTO。

提供给这两个参数的对象必须是符合 
:class:`AbstractDTO <litestar.dto.base_dto.AbstractDTO>` 协议的类。

在处理器上定义 DTO
~~~~~~~~~~~~~~~~~~

``dto`` 参数
-------------

.. literalinclude:: /examples/data_transfer_objects/the_dto_parameter.py
    :caption: 使用 ``dto`` 参数
    :language: python

在此示例中，``UserDTO`` 执行将客户端数据解码为 ``User`` 类型，
并将返回的 ``User`` 实例编码为 Litestar 可以编码为字节的类型。

``return_dto`` 参数
-------------------

.. literalinclude:: /examples/data_transfer_objects/the_return_dto_parameter.py
    :caption: 使用 ``return_dto`` 参数
    :language: python

在此示例中，``UserDTO`` 执行将客户端数据解码为 ``User`` 类型，
``UserReturnDTO`` 负责将 ``User`` 实例转换为 Litestar 可以编码为字节的类型。

覆盖隐式 ``return_dto``
-----------------------

如果没有为处理器声明 ``return_dto`` 类型，
则为 ``dto`` 参数声明的类型将用于解码和编码请求和响应数据。
如果此行为不理想，可以通过将 ``return_dto`` 显式设置为 ``None`` 来禁用它。

.. literalinclude:: /examples/data_transfer_objects/overriding_implicit_return_dto.py
    :caption: 禁用隐式 ``return_dto`` 行为
    :language: python

在层上定义 DTO
~~~~~~~~~~~~~~

DTO 可以在应用程序的任何 :ref:`层 <layered-architecture>` 上定义。
应用的 DTO 类型是在所有权链中定义的、最接近相关处理器的类型。

.. literalinclude:: /examples/data_transfer_objects/defining_dtos_on_layers.py
    :caption: 在 Controller 上定义 DTO
    :language: python

使用 codegen 后端提高性能
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    此功能在 ``2.2.0`` 中引入，从 ``2.8.0`` 开始默认启用。
    可以使用 ``DTOConfig(experimental_codegen_backend=False)`` 选择性地禁用它。

DTO 后端负责转换、验证和解析，是对性能影响最大的部分。
DTO codegen 后端通过在运行时生成优化的 Python 代码来提高效率。

性能改进
--------

某些操作的性能提升：

=================================== ===========
操作                                 提升
=================================== ===========
JSON 转 Python                      ~2.5x
JSON 转 Python（集合）               ~3.5x
Python 转 Python                    ~2.5x
Python 转 Python（集合）             ~5x
Python 转 JSON                      ~5.3x
Python 转 JSON（集合）               ~5.4x
=================================== ===========
