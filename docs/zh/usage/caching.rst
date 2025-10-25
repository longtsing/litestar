缓存
=======

缓存响应
------------------

有时缓存某些响应是很有必要的，特别是当这些响应涉及昂贵的计算，或者期望轮询时。Litestar 提供了一个简单的缓存机制：

.. literalinclude:: /examples/caching/cache.py
    :language: python
    :lines: 1, 4-8

通过将 :paramref:`~litestar.handlers.HTTPRouteHandler.cache` 设置为 ``True``，来自处理器的响应将被缓存。如果路由处理器中没有设置 ``cache_key_builder``，则该路由处理器的缓存将在 :attr:`~.config.response_cache.ResponseCacheConfig.default_expiration` 时间内启用。

.. note:: 如果默认的 :paramref:`~litestar.config.response_cache.ResponseCacheConfig.default_expiration` 设置为 ``None``，则将路由处理器的 :paramref:`~litestar.handlers.HTTPRouteHandler.cache` 设置为 ``True`` 会使响应无限期地保存在缓存中。

或者，您可以像这样指定缓存给定处理器响应的秒数：

.. literalinclude:: /examples/caching/cache.py
    :language: python
    :caption: 通过将 :paramref:`~litestar.handlers.HTTPRouteHandler.cache` 参数设置为缓存响应的秒数来缓存响应 120 秒。
    :lines: 1, 9-13
    :emphasize-lines: 4

如果您希望响应被无限期缓存，可以传递 :class:`~.config.response_cache.CACHE_FOREVER` 哨兵值：

.. literalinclude:: /examples/caching/cache.py
    :language: python
    :caption: 通过将 :paramref:`~litestar.handlers.HTTPRouteHandler.cache` 参数设置为 :class:`~litestar.config.response_cache.CACHE_FOREVER` 来无限期缓存响应。
    :lines: 1-3, 14-18
    :emphasize-lines: 5

配置
-------------

您可以通过向 :class:`Litestar 实例 <.app.Litestar>` 传递 :class:`~.config.response_cache.ResponseCacheConfig` 实例来在应用级别配置缓存行为。

更改数据存储位置
+++++++++++++++++++++++++++++

默认情况下，缓存将使用 :class:`~.stores.memory.MemoryStore`，但可以配置为使用其他存储后端。
