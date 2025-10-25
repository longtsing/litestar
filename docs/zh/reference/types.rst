类型
=====

.. module:: litestar.types

可调用类型
--------------

.. autodata:: litestar.types.AfterExceptionHookHandler
.. autodata:: litestar.types.AfterRequestHookHandler
.. autodata:: litestar.types.AfterResponseHookHandler
.. autodata:: litestar.types.AnyCallable
.. autodata:: litestar.types.AsyncAnyCallable
.. autodata:: litestar.types.BeforeMessageSendHookHandler
.. autodata:: litestar.types.BeforeRequestHookHandler
.. autodata:: litestar.types.CacheKeyBuilder
.. autodata:: litestar.types.ExceptionHandler
.. autodata:: litestar.types.Guard
.. autodata:: litestar.types.LifespanHook
.. autodata:: litestar.types.OnAppInitHandler
.. autodata:: litestar.types.Serializer

ASGI 类型
----------

.. autodata:: litestar.types.Method

ASGI 应用
~~~~~~~~~~~~~~~~~

.. autodata:: litestar.types.ASGIApp

ASGI 应用参数
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autodata:: litestar.types.Scope
.. autodata:: litestar.types.Receive
.. autodata:: litestar.types.Send

ASGI 作用域
~~~~~~~~~~~~

.. autoclass:: litestar.types.ASGIVersion
.. autoclass:: litestar.types.BaseScope
.. autoclass:: litestar.types.HTTPScope
.. autoclass:: litestar.types.LifeSpanScope
.. autoclass:: litestar.types.WebSocketScope

ASGI 事件
~~~~~~~~~~~~

.. autoclass:: litestar.types.HTTPRequestEvent
.. autoclass:: litestar.types.HTTPResponseStartEvent
.. autoclass:: litestar.types.HTTPResponseBodyEvent
.. autoclass:: litestar.types.HTTPServerPushEvent
.. autoclass:: litestar.types.HTTPDisconnectEvent
.. autoclass:: litestar.types.WebSocketConnectEvent
.. autoclass:: litestar.types.WebSocketAcceptEvent
.. autoclass:: litestar.types.WebSocketReceiveEvent
.. autoclass:: litestar.types.WebSocketSendEvent
.. autoclass:: litestar.types.WebSocketResponseStartEvent
.. autoclass:: litestar.types.WebSocketResponseBodyEvent
.. autoclass:: litestar.types.WebSocketDisconnectEvent
.. autoclass:: litestar.types.WebSocketCloseEvent
