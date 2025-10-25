<!-- markdownlint-disable -->
<p align="center">
  <img src="https://raw.githubusercontent.com/litestar-org/branding/473f54621e55cde9acbb6fcab7fc03036173eb3d/assets/Branding%20-%20PNG%20-%20Transparent/Logo%20-%20Banner%20-%20Inline%20-%20Light.png" alt="Litestar Logo - Light" width="100%" height="auto" />
</p>
<!-- markdownlint-restore -->

<div align="center">

<!-- prettier-ignore-start -->

| 项目 | | 状态 |
|---|:---|---|
| CI/CD | | [![最新发布](https://github.com/litestar-org/litestar/actions/workflows/publish.yml/badge.svg)](https://github.com/litestar-org/litestar/actions/workflows/publish.yml) [![ci](https://github.com/litestar-org/litestar/actions/workflows/ci.yml/badge.svg)](https://github.com/litestar-org/litestar/actions/workflows/ci.yml) [![文档构建](https://github.com/litestar-org/litestar/actions/workflows/docs.yml/badge.svg?branch=main)](https://github.com/litestar-org/litestar/actions/workflows/docs.yml) |
| 质量 | | [![覆盖率](https://codecov.io/github/litestar-org/litestar/graph/badge.svg?token=vKez4Pycrc)](https://codecov.io/github/litestar-org/litestar) |
| 包 | | [![PyPI - 版本](https://img.shields.io/pypi/v/litestar?labelColor=202235&color=edb641&logo=python&logoColor=edb641)](https://badge.fury.io/py/litestar) ![PyPI - 支持的 Python 版本](https://img.shields.io/pypi/pyversions/litestar?labelColor=202235&color=edb641&logo=python&logoColor=edb641) ![Starlite PyPI - 下载量](https://img.shields.io/pypi/dm/starlite?logo=python&label=starlite%20downloads&labelColor=202235&color=edb641&logoColor=edb641) ![Litestar PyPI - 下载量](https://img.shields.io/pypi/dm/litestar?logo=python&label=litestar%20downloads&labelColor=202235&color=edb641&logoColor=edb641) |
| 社区 | | [![Reddit](https://img.shields.io/reddit/subreddit-subscribers/litestarapi?label=r%2FLitestar&logo=reddit&labelColor=202235&color=edb641&logoColor=edb641)](https://reddit.com/r/litestarapi) [![Discord](https://img.shields.io/discord/919193495116337154?labelColor=202235&color=edb641&label=chat%20on%20discord&logo=discord&logoColor=edb641)](https://discord.gg/litestar) [![Matrix](https://img.shields.io/badge/chat%20on%20Matrix-bridged-202235?labelColor=202235&color=edb641&logo=matrix&logoColor=edb641)](https://matrix.to/#/#litestar:matrix.org) [![Medium](https://img.shields.io/badge/Medium-202235?labelColor=202235&color=edb641&logo=medium&logoColor=edb641)](https://blog.litestar.dev) [![Twitter](https://img.shields.io/twitter/follow/LitestarAPI?labelColor=202235&color=edb641&logo=twitter&logoColor=edb641&style=flat)](https://twitter.com/LitestarAPI) [![博客](https://img.shields.io/badge/Blog-litestar.dev-202235?logo=blogger&labelColor=202235&color=edb641&logoColor=edb641)](https://blog.litestar.dev) |
| 元信息 | | [![Litestar 项目](https://img.shields.io/badge/Litestar%20Org-%E2%AD%90%20Litestar-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://github.com/litestar-org/litestar) [![类型 - Mypy](https://img.shields.io/badge/types-Mypy-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://github.com/python/mypy) [![许可证 - MIT](https://img.shields.io/badge/license-MIT-202235.svg?logo=python&labelColor=202235&color=edb641&logoColor=edb641)](https://spdx.org/licenses/) [![Litestar 赞助商](https://img.shields.io/badge/Sponsor-%E2%9D%A4-%23edb641.svg?&logo=github&logoColor=edb641&labelColor=202235)](https://github.com/sponsors/litestar-org) [![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json&labelColor=202235)](https://github.com/astral-sh/ruff) [![代码风格 - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json&labelColor=202235)](https://github.com/psf/black) [![所有贡献者](https://img.shields.io/github/all-contributors/litestar-org/litestar?labelColor=202235&color=edb641&logoColor=edb641)](#contributors-) |

<!-- prettier-ignore-end -->
</div>

<hr>

Litestar 是一个功能强大、灵活但有主见的 ASGI 框架，专注于构建 API。它提供高性能的数据验证、依赖注入、一流的 ORM 集成、授权原语、丰富的插件 API、中间件以及启动和运行应用程序所需的更多功能。

查看[文档 📚](https://docs.litestar.dev/)以获取其功能的详细概述！

此外，[Litestar 全栈存储库](https://github.com/litestar-org/litestar-fullstack)可以让你很好地了解一个功能齐全的 Litestar 应用程序可能是什么样子。

<details>
<summary>目录</summary>

- [安装](#安装)
  - [快速入门](#快速入门)
- [核心功能](#核心功能)
  - [示例应用程序](#示例应用程序)
- [功能](#功能)
  - [基于类的控制器](#基于类的控制器)
  - [数据解析、类型提示和 Msgspec](#数据解析类型提示和-msgspec)
  - [插件系统、ORM 支持和 DTO](#插件系统orm-支持和-dtos)
  - [OpenAPI](#openapi)
  - [依赖注入](#依赖注入)
  - [中间件](#中间件)
  - [路由守卫](#路由守卫)
  - [请求生命周期挂钩](#请求生命周期挂钩)
- [性能](#性能)
- [贡献](#贡献)

</details>

## 安装

```shell
pip install litestar
```
或者，要包含用于运行应用程序的 CLI 和服务器 (uvicorn)：
```shell
pip install 'litestar[standard]'
```

## 快速入门

```python title="app.py"
from litestar import Litestar, get

@get("/")
async def hello_world() -> dict[str, str]:
    """延续传统，你好世界。"""
    return {"hello": "world"}

app = Litestar(route_handlers=[hello_world])
```

并使用以下命令运行它

```bash
litestar run
```


## 核心功能

- [基于类的控制器](#基于类的控制器)
- [依赖注入](#依赖注入)
- [分层中间件](#中间件)
- [插件系统](#插件系统orm-支持和-dtos)
- [OpenAPI 3.1 模式生成](#openapi)
- [生命周期挂钩](#请求生命周期挂钩)
- [基于路由守卫的授权](#路由守卫)
- 支持 `dataclasses`、`TypedDict`、[`msgspec`](https://jcristharif.com/msgspec/)、[pydantic 版本 1 和版本 2（甚至在同一个应用程序中）](https://docs.pydantic.dev/latest/) 和 [(c)attrs](https://catt.rs/en/stable/)
- 分层参数声明
- 支持 [RFC 9457](https://datatracker.ietf.org/doc/html/rfc9457) 标准化的“问题详情”错误响应
- [使用以下工具自动生成 API 文档](#redoc-swagger-ui-和-stoplight-elements-api-文档)：
  - [Scalar](https://github.com/scalar/scalar/)
  - [RapiDoc](https://github.com/rapi-doc/RapiDoc)
