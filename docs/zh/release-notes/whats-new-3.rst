.. py:currentmodule:: litestar

3.0 有哪些变化？
======================

本文档概述了 **2.11.x** 版本与 **3.0** 之间的变化。
如需详细了解所有变更，包括 3.0 发布前的各版本变更，请查阅 :doc:`/release-notes/changelog`。

.. note:: **2.11** 版本线不受此更改影响

导入路径变化
-------

+----------------------------------------------------+------------------------------------------------------------------------+
| ``2.x``                                            | ``3.x``                                                                |
+====================================================+========================================================================+
| **SECTION**                                        | **SECTION**                                                            |
+----------------------------------------------------+------------------------------------------------------------------------+
| 请在此处填写 v2 的变更内容                         | 请在此处填写 v3 的变更内容                                             |
+----------------------------------------------------+------------------------------------------------------------------------+

移除 ``StaticFileConfig``
-------------------------------

`StaticFilesConfig` 已被移除，相关参数和函数如下：

- `Litestar.static_files_config`
- `Litestar.url_for_static_asset`
- `Request.url_for_static_asset`

`create_static_files_router` 可直接替代 `StaticFilesConfig`，只需像普通处理器一样添加到 `route_handlers`。

`url_for_static_assets` 的用法应替换为 `url_for("static", ...)`。

隐式可选默认参数
------------------------------------

在 v2 中，如果处理器参数类型为可选，则会隐式赋值为 `None`。例如，以下处理器如果未传递查询参数，则 `param` 参数会被赋值为 `None`：

.. code-block:: python

    @get("/")
    def my_handler(param: int | None) -> ...:
        ...

这种行为源自早期使用 Pydantic v1 模型表示处理器签名。在 v3 中不再进行隐式转换。如果需要默认值为 `None`，需显式设置：

.. code-block:: python

    @get("/")
    def my_handler(param: int | None = None) -> ...:
        ...

OpenAPI 控制器被插件替代
----------------------

3.0 版本中，OpenAPI 控制器模式（v2.8 弃用）已被更灵活的插件系统替代。

移除 ``OpenAPIController`` 子类化
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

此前，用户通过继承 OpenAPIController 并设置到 `OpenAPIConfig.openapi_controller` 属性来配置根路径和样式。3.0 版本已移除该模式，需改用 UI 插件进行配置。

迁移步骤：

1. 移除所有继承 ``OpenAPIController`` 的实现。
2. 使用 `OpenAPIConfig.render_plugins` 属性配置 OpenAPI UI。如果未指定插件，系统会自动添加 `ScalarRenderPlugin` 作为默认配置。
3. 使用 `OpenAPIConfig.openapi_router` 属性进行额外配置。

更多信息请参阅 :doc:`/usage/openapi/ui_plugins`。

端点配置变更
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3.0.0 版本不再提供 `OpenAPIConfig.enabled_endpoints` 属性。此前该属性用于启用不同的 OpenAPI UI 端点。新版本仅默认启用 `openapi.json` 端点和 `Scalar` UI 插件。

如需额外端点，请在 `OpenAPIConfig.render_plugins` 参数中正确设置所需插件。

`root_schema_site` 处理方式变更
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
