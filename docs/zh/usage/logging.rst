.. _logging-usage:

日志记录
=======

可以使用 :class:`~litestar.logging.config.LoggingConfig` 配置应用程序和请求级别的日志记录器：

.. code-block:: python

   import logging

   from litestar import Litestar, Request, get
   from litestar.logging import LoggingConfig


   @get("/")
   def my_router_handler(request: Request) -> None:
       request.logger.info("在请求内部")
       return None


   logging_config = LoggingConfig(
       root={"level": "INFO", "handlers": ["queue_listener"]},
       formatters={
           "standard": {"format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"}
       },
       log_exceptions="always",
   )

   app = Litestar(route_handlers=[my_router_handler], logging_config=logging_config)

.. attention::

    Litestar 配置了一个非阻塞的 ``QueueListenerHandler``，它在日志配置中键为 ``queue_listener``。上面的示例使用此处理程序，它对于异步应用程序是最佳的。请确保在您自己的日志记录器中使用它，如上例所示。

.. attention::

    默认情况下不会记录异常，调试模式除外。请确保使用 ``log_exceptions="always"``，如上例所示。
