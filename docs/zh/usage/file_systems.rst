文件系统
============

当使用 :class:`~litestar.response.File` 发送文件或使用 :func:`~litestar.static_files.create_static_files_router` 提供文件服务时，除了从本地文件系统提供服务外，Litestar 还支持自定义文件系统，包括对 `fsspec <https://filesystem-spec.readthedocs.io/en/latest/>`_ 的支持，这使得可以集成各种远程文件系统。

在其核心，文件系统是任何实现抽象 :class:`~litestar.file_system.BaseFileSystem` 类的类。默认情况下，Litestar 附带单个实现：:class:`~litestar.file_system.BaseLocalFileSystem`。


.. literalinclude:: /examples/responses/file_response_fs.py
    :language: python
    :caption: 从 S3 发送文件


支持的文件系统
----------------------

除了基于 :class:`~litestar.file_system.BaseFileSystem` 实现的文件系统外，所有 ``fsspec`` 文件系统（同步和异步）都受支持。它们将分别包装在 :class:`~litestar.file_system.FsspecSyncWrapper` 或 :class:`~litestar.file_system.FsspecAsyncWrapper` 中以符合通用接口。


fsspec
+++++++

在接受 :class:`~litestar.file_system.BaseFileSystem` 的任何地方，通常也接受 ``fsspec`` 文件系统。

将它们设置在 `Registry` 中，或使用 :func:`~litestar.file_system.maybe_wrap_fsspec_file_system` 手动包装一次并使用该包装器，这样它们就不必为每次使用再次包装，这仍然是有意义的。
