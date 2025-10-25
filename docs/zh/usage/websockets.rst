WebSockets
==========

在 Litestar 中有三种处理 WebSocket 的方法：

1. 低级 :func:`~litestar.handlers.websocket` 路由处理程序，在 ASGI WebSocket 接口上提供基本抽象
2. :func:`~litestar.handlers.websocket_listener` 和 :class:`~litestar.handlers.WebsocketListener`\  ：反应式、事件驱动的 WebSocket，具有完整的序列化和 DTO 支持以及对同步接口的支持
3. :func:`~litestar.handlers.websocket_stream`：主动的、面向流的 WebSocket，具有完整的序列化和 DTO 支持
4. :func:`~litestar.handlers.send_websocket_stream`：主动的、面向流的 WebSocket


低级和高级接口之间的主要区别在于，处理低级接口需要设置循环并监听传入数据、处理异常、客户端断开连接以及解析传入和序列化传出数据。



WebSocket 监听器
--------------------

WebSocket 监听器可用于以事件驱动的方式与 WebSocket 交互，使用回调式接口。它们将 WebSocket 处理程序视为任何其他路由处理程序：接受已预处理形式的传入数据并返回要序列化并通过连接发送的数据的可调用对象。低级细节将在幕后处理。


.. code-block:: python

    from litestar import Litestar
    from litestar.handlers.websocket_handlers import websocket_listener


    @websocket_listener("/")
    async def handler(data: str) -> str:
        return data
