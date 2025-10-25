模板
==========

Litestar 内置支持 `Jinja2 <https://jinja.palletsprojects.com/en/3.0.x/>`_、`Mako <https://www.makotemplates.org/>`_ 和 `Minijinja <https://github.com/mitsuhiko/minijinja/tree/main/minijinja-py>`_ 模板引擎，以及抽象以使用您希望的任何模板引擎。

模板引擎
----------------

为了保持轻量级，Litestar 安装不包括 *Jinja*、*Mako* 或 *Minijinja* 库本身。在您可以开始使用它们之前，您必须通过相应的额外选项安装它：

.. tab-set::

    .. tab-item:: Jinja
        :sync: jinja

        .. code-block:: shell

            pip install 'litestar[jinja]'

    .. tab-item:: Mako
        :sync: mako

        .. code-block:: shell

            pip install 'litestar[mako]'

    .. tab-item:: MiniJinja
        :sync: minijinja

        .. code-block:: shell

            pip install 'litestar[minijinja]'

.. tip::

    *Jinja* 包含在 ``standard`` 额外选项中。如果您使用 ``standard`` 安装了 Litestar，则已经安装了 Jinja。
