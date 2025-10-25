:tocdepth: 4

存储
======

.. py:currentmodule:: litestar.stores


在开发应用程序时，通常需要一个简单的存储机制，例如在 :doc:`缓存响应数据</usage/caching>` 或为 :ref:`服务器端会话 <usage/middleware/builtin-middleware:Server-side sessions>` 存储数据时。在这些情况下，通常不需要传统数据库，简单的键/值存储就足够了。

Litestar 提供了几个低级键值存储，提供异步接口以线程和进程安全的方式存储数据。这些存储通过 :class:`注册表 <litestar.stores.registry.StoreRegistry>` 集中管理，允许在整个应用程序和第三方集成（例如插件）中轻松访问。


内置存储
---------------

:class:`MemoryStore <litestar.stores.memory.MemoryStore>`
    一个简单的内存存储，使用字典来保存数据。此存储不提供持久性，也不是线程或多进程安全的，但它适用于基本应用程序（如缓存），并且通常具有最低的开销。这是 Litestar 内部使用的默认存储。如果您计划启用 :doc:`多个 Web 工作进程 </reference/cli>` 并且需要跨多个工作进程的进程间通信，则应使用其他非内存存储之一。

:class:`FileStore <litestar.stores.file.FileStore>`
    将数据保存为磁盘上的文件的存储。内置持久性，数据易于提取和备份。与内存解决方案相比速度较慢，主要适用于需要存储大量数据、特别长寿命或持久性非常重要的情况。提供 `命名空间`_。

:class:`RedisStore <litestar.stores.redis.RedisStore>`
    由 `redis <https://redis.io/>`_ 支持的存储。它提供 Redis 的所有保证和功能，使其适用于几乎所有应用程序。提供 `命名空间`_。

:class:`ValkeyStore <litestar.stores.valkey.ValkeyStore>`
    由 `valkey <https://valkey.io>`_ 支持的存储，valkey 是 Redis 的一个分支，是 Redis 许可证更改的结果。与 RedisStore 类似，它适用于几乎所有应用程序并支持 `命名空间`_。
