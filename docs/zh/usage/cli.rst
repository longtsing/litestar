CLI
===

.. |uvicorn| replace:: uvicorn
.. _uvicorn: https://www.uvicorn.org/

Litestar 提供了一个方便的命令行界面（CLI），用于运行和管理 Litestar 应用程序。CLI 由 `click <https://click.palletsprojects.com/>`_、`rich <https://rich.readthedocs.io>`_ 和 `rich-click <https://github.com/ewels/rich-click>`_ 提供支持。

启用所有 CLI 功能
-------------------------

CLI 及其硬依赖项默认包含在内。但是，如果您想运行应用程序（使用 ``litestar run``）或美化 ``litestar schema typescript`` 命令生成的 Typescript，则需要 |uvicorn|_ 和 `jsbeautifier <https://pypi.org/project/jsbeautifier/>`_。它们可以独立安装，但我们建议安装 ``standard`` 额外包，它方便地捆绑了常用的可选依赖项。

.. code-block:: shell
    :caption: 安装 standard 组

    pip install 'litestar[standard]'

安装 ``standard`` 后，您将可以访问 ``litestar run`` 命令。

自动发现
-------------

Litestar 提供对放置在名为 ``app`` 或 ``application`` 的规范模块中的应用程序和应用程序工厂的自动发现。这些模块可以是单个文件或目录。在这些模块或其子模块中，CLI 将检测 :class:`Litestar <.app.Litestar>` 的任何实例、名为 ``create_app`` 的可调用对象，或注释为返回 :class:`Litestar <.app.Litestar>` 实例的可调用对象。

自动发现按以下顺序查找这些位置：

1. ``app.py``
2. ``app/__init__.py``
3. ``app`` 的子模块
4. ``application.py``
5. ``application/__init__.py``
6. ``application`` 的子模块

在这些位置内，Litestar CLI 查找：

1. 名为 ``app`` 的 :term:`对象`，它是 :class:`~.app.Litestar` 的实例
2. 名为 ``application`` 的对象，它是 :class:`~.app.Litestar` 的实例
3. 任何 :class:`~.app.Litestar` 的实例对象
4. 名为 ``create_app`` 的 :term:`可调用对象 <callable>`
5. 注释为返回 :class:`~.app.Litestar` 实例的可调用对象
