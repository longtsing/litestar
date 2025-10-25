.. currentmodule:: litestar.channels

通道
========

**通道（Channels）** 是一组相关功能，旨在促进事件流的路由，例如可用于向 WebSocket 客户端广播消息。

通道提供：

1. 独立的 :term:`代理` 后端，可选地处理进程间通信和按需数据持久化
2. 基于"通道"的 :term:`订阅` 管理
3. 订阅者对象作为个性化 :term:`事件流` 的抽象，提供后台工作器和托管订阅
4. 同步和异步数据发布
5. 按 :term:`通道` 基础的可选 :term:`历史` 管理
6. :doc:`WebSocket </usage/websockets>` 集成，为应用程序生成 WebSocket 路由处理器，以处理 :term:`订阅` 和将传入事件发布到已连接的客户端


基本概念
--------------

使用通道涉及几个移动部件。为了更好地熟悉概念、术语和数据流，提供了以下术语表和流程图

术语表
++++++++

.. dropdown:: 点击切换术语表

    .. glossary::

        事件 (event)
            发布到或从绑定到最初发布它的 :term:`通道` 的 :term:`后端` 接收的单个数据片段

        事件流 (event stream)
            :term:`事件 <event>` 流，由 :term:`订阅者` 之前订阅的所有通道的事件组成

        订阅者 (subscriber)
            :class:`订阅者 <.subscriber.Subscriber>`：包装 :term:`事件流` 并通过各种方法提供访问的对象

        后端 (backend)
            :class:`通道后端 <.backends.base.ChannelsBackend>`。此对象处理通道的底层通信和数据存储
