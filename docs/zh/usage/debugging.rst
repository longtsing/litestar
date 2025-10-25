调试
=========

使用 Python 调试器
--------------------------

您可以配置 Litestar 在发生异常时进入 :doc:`Python 调试器 <python:library/pdb>`。这可以通过不同方式配置：

使用 ``pdb_on_exception`` 选项配置 ``Litestar``
    .. code-block:: python

        app = Litestar(pdb_on_exception=True)


使用 CLI 运行应用并使用 ``--pdb`` 标志
    .. code-block:: shell

        litestar run --pdb

使用 ``LITESTAR_PDB`` 环境变量
    ``LITESTAR_PDB=1``


使用 IDE 调试
---------------------

您可以轻松地将 IDE 的调试器附加到应用程序，无论您是通过 CLI 还是像 `uvicorn <https://www.uvicorn.org/>`_ 这样的 Web 服务器运行它。

Intellij / PyCharm
++++++++++++++++++

使用 CLI
*************

1. 通过 ``Run`` > ``Edit Configurations`` 创建新的调试配置
2. 选择 ``Module name`` 选项并将其设置为 ``litestar``
3. 添加 ``run`` 参数以及您想传递给 CLI 的其他可选参数

   .. image:: /images/debugging/pycharm-config-cli.png

4. 通过 ``Run`` > ``Debug Litestar`` 在调试器中运行应用程序

   .. image:: /images/debugging/pycharm-debug.png
        :align: center


.. important::
    使用 IDE 调试时，确保正确配置 Python 解释器和工作目录。
