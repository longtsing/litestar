==============
Flash 消息
==============

.. versionadded:: 2.7.0

Flash 消息是向用户传达信息的强大工具，
例如通过一次性消息以及响应来显示成功通知、警告或错误，这些消息是由于某种用户操作而产生的。

它们通常用于在下一次页面加载时显示消息，是通过提供关于用户操作（如表单提交）的即时反馈来增强用户体验的好方法。

注册插件
--------

FlashPlugin 可以轻松与不同的模板引擎集成。
以下是如何将 ``FlashPlugin`` 注册到 ``Jinja2``、``Mako`` 和 ``MiniJinja`` 模板引擎的示例。

.. tab-set::

    .. tab-item:: Jinja2
        :sync: jinja

        .. literalinclude:: /examples/plugins/flash_messages/jinja.py
            :language: python
            :caption: 使用 Jinja2 模板引擎注册 flash 消息插件

    .. tab-item:: Mako
        :sync: mako

        .. literalinclude:: /examples/plugins/flash_messages/mako.py
            :language: python
            :caption: 使用 Mako 模板引擎注册 flash 消息插件

    .. tab-item:: MiniJinja
        :sync: minijinja

        .. literalinclude:: /examples/plugins/flash_messages/minijinja.py
            :language: python
            :caption: 使用 MiniJinja 模板引擎注册 flash 消息插件

使用插件
--------

在将 FlashPlugin 注册到应用程序后，您可以开始使用它在应用程序路由中添加和显示 flash 消息。
