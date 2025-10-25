静态文件
============

要提供静态文件（即从给定目录提供任意文件），可以使用 :func:`~litestar.static_files.create_static_files_router` 创建 :class:`Router <litestar.router.Router>` 来处理此任务。

.. literalinclude:: /examples/static_files/full_example.py
    :language: python
    :caption: 使用 :func:`create_static_files_router <litestar.static_files.create_static_files_router>` 提供静态文件

在此示例中，目录 ``assets`` 中的文件将在路径 ``/static`` 上提供服务。文件 ``assets/hello.txt`` 现在可在 ``/static/hello.txt`` 上访问

.. attention:: 目录被解释为相对于启动应用程序的工作目录


将文件作为附件发送
----------------------------

默认情况下，文件以"内联"方式发送，这意味着它们将具有 ``Content-Disposition: inline`` 头。

将 :paramref:`~litestar.static_files.create_static_files_router.params.send_as_attachment` 设置为 ``True`` 将改为使用 ``Content-Disposition: attachment`` 发送它们：

.. literalinclude:: /examples/static_files/send_as_attachment.py
    :language: python
    :caption: 使用 :func:`create_static_files_router` 的 :paramref:`~litestar.static_files.create_static_files_router.params.send_as_attachment` 参数将文件作为附件发送


HTML 模式
---------

可以通过将 :paramref:`~litestar.static_files.create_static_files_router.params.html_mode` 设置为 ``True`` 来启用"HTML 模式"。
