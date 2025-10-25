异常和异常处理
=================================

Litestar 定义了一个名为 :class:`LitestarException <litestar.exceptions.LitestarException>` 的基础异常，它作为所有其他异常的基类，请参阅 :mod:`API 参考 <litestar.exceptions>`。

一般来说，Litestar 有两种异常处理场景：

- 在应用程序配置、启动和初始化期间引发的异常，这些异常像常规 Python 异常一样处理
- 作为请求处理的一部分引发的异常，即路由处理器、依赖项和中间件中的异常，应作为响应返回给最终用户

配置异常
------------------------

对于缺少额外依赖项，Litestar 将引发 :class:`MissingDependencyException <litestar.exceptions.MissingDependencyException>`。例如，如果您尝试使用 :ref:`SQLAlchemyPlugin <plugins>` 而没有安装 SQLAlchemy，则在启动应用程序时将引发此异常。

对于其他配置问题，Litestar 将引发 :class:`ImproperlyConfiguredException <litestar.exceptions.ImproperlyConfiguredException>`，并带有解释问题的消息。

应用程序异常
----------------------

对于应用程序异常，Litestar 使用 :class:`~litestar.exceptions.http_exceptions.HTTPException` 类，它继承自 :class:`~litestar.exceptions.LitestarException`。此异常将被序列化为以下模式的 JSON 响应：

.. code-block:: json

   {
     "status_code": 500,
     "detail": "Internal Server Error",
     "extra": {}
   }

Litestar 还提供了几个预配置的 ``HTTPException`` 子类，这些子类具有预设的错误代码，您可以使用，例如：


.. :currentmodule:: litestar.exceptions.http_exceptions

+----------------------------------------+-------------+------------------------------------------+
| 异常                                   | 状态码      | 描述                                     |
+========================================+=============+==========================================+
| :class:`ImproperlyConfiguredException` | 500         | 内部用于配置错误                         |
+----------------------------------------+-------------+------------------------------------------+
| :class:`ValidationException`           | 400         | 在验证或解析失败时引发                   |
+----------------------------------------+-------------+------------------------------------------+
