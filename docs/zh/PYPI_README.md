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
  - [Redoc](https://github.com/Redocly/redoc)
  - [Stoplight Elements](https://github.com/stoplightio/elements)
  - [Swagger-UI](https://swagger.io/tools/swagger-ui/)
- [Trio](https://trio.readthedocs.io/en/stable/) 支持（内置，通过 [AnyIO](https://anyio.readthedocs.io/)）
- 使用 [msgspec](https://github.com/jcrist/msgspec) 进行超快速验证、序列化和反序列化
- [SQLAlchemy 集成](https://docs.advanced-alchemy.litestar.dev/latest/)

## 示例应用程序

<details>
<summary>预构建示例应用程序</summary>

- [litestar-hello-world](https://github.com/litestar-org/litestar-hello-world)：最小应用程序设置。非常适合测试和 POC 工作。
- [litestar-fullstack](https://github.com/litestar-org/litestar-fullstack)：包含 Web 应用程序所需的大部分样板代码的参考应用程序。
  它包含一个使用最佳实践配置的 Litestar 应用程序、SQLAlchemy 2.0 和 SAQ，一个与 Vitejs 和 Jinja2 模板集成的前端、Docker 等等。像所有
  Litestar 项目一样，这个应用程序欢迎大大小小的贡献。
</details>

## 赞助商

Litestar 是一个开源项目，我们享受赞助商的支持，帮助资助我们所做的令人兴奋的工作。

**非常**感谢我们的赞助商：

[//]: # "注意维护人员：最高级别赞助商优先；每行不超过 3 个 - 如果需要创建新的 div"

<a href="https://github.com/scalar/scalar/?utm_source=litestar&utm_medium=website&utm_campaign=main-badge" target="_blank" title="Scalar.com - 使用 Scalar 记录、发现和测试 API。"><img src="https://raw.githubusercontent.com/litestar-org/branding/main/assets/sponsors/scalar.svg" width="180" alt="Scalar.com"></a>
<a href="https://telemetrysports.com/" title="Telemetry Sports - 改变数据影响体育体验的方式"><img src="https://raw.githubusercontent.com/litestar-org/branding/main/assets/sponsors/telemetry-sports/unofficial-telemetry-whitebg.svg" width="150" alt="Telemetry Sports"></a>

<a href="https://docs.litestar.dev/latest/#sponsors" class="external-link" target="_blank">在文档中查看我们的赞助商</a>

如果你想支持我们所做的工作，请考虑通过 [Polar.sh][sponsor-polar]（首选）、[GitHub][sponsor-github] 或 [Open Collective][sponsor-oc] [成为赞助商][sponsor-polar]。

此外，仅通过 [Polar][sponsor-polar]，你可以参与基于承诺的赞助。

[sponsor-github]: https://github.com/sponsors/litestar-org
[sponsor-oc]: https://opencollective.com/litestar
[sponsor-polar]: https://polar.sh/litestar-org

## 功能

### 基于类的控制器

虽然支持基于函数的路由处理器，但 Litestar 还支持并推广使用基于类的控制器的 Python OOP：

<details>
<summary>基于类的控制器示例</summary>

```python title="my_app/controllers/user.py"
from typing import List, Optional
from datetime import datetime

from litestar import Controller, get, post, put, patch, delete
from litestar.dto import DTOData
from pydantic import UUID4

from my_app.models import User, PartialUserDTO


class UserController(Controller):
    path = "/users"

    @post()
    async def create_user(self, data: User) -> User: ...

    @get()
    async def list_users(self) -> List[User]: ...

    @get(path="/{date:int}")
    async def list_new_users(self, date: datetime) -> List[User]: ...

    @patch(path="/{user_id:uuid}", dto=PartialUserDTO)
    async def partial_update_user(
        self, user_id: UUID4, data: DTOData[PartialUserDTO]
    ) -> User: ...

    @put(path="/{user_id:uuid}")
    async def update_user(self, user_id: UUID4, data: User) -> User: ...

    @get(path="/{user_name:str}")
    async def get_user_by_name(self, user_name: str) -> Optional[User]: ...

    @get(path="/{user_id:uuid}")
    async def get_user(self, user_id: UUID4) -> User: ...

    @delete(path="/{user_id:uuid}")
    async def delete_user(self, user_id: UUID4) -> None: ...
```

</details>

### 数据解析、类型提示和 Msgspec

Litestar 是严格类型化的，并且它强制执行类型化。例如，如果你忘记为路由处理器的返回值添加类型，将会引发异常。这样做的原因是 Litestar 使用类型数据来生成 OpenAPI 规范，以及验证和解析数据。因此，类型化对框架至关重要。

此外，Litestar 允许使用插件扩展其支持。

### 插件系统、ORM 支持和 DTOs

Litestar 有一个插件系统，允许用户扩展序列化/反序列化、OpenAPI 生成和其他功能。

它附带一个内置的 SQL Alchemy 插件，允许用户"原生"使用 SQLAlchemy 声明类，即作为将被序列化/反序列化的类型参数，并将它们作为值从路由处理器返回。

Litestar 还支持使用 `DTOFactory` 类以编程方式创建 DTO，该类也支持使用插件。

### OpenAPI

Litestar 有自定义逻辑来生成 OpenAPI 3.1.0 模式，包括可选的使用 [`polyfactory`](https://pypi.org/project/polyfactory/) 库生成示例。

#### ReDoc、Swagger-UI 和 Stoplight Elements API 文档

Litestar 使用以下工具从生成的 OpenAPI 模式提供文档：

- [ReDoc](https://redoc.ly/)
- [Swagger-UI](https://swagger.io/tools/swagger-ui/)
- [Stoplight Elements](https://github.com/stoplightio/elements)
- [RapiDoc](https://rapidocweb.com/)

所有这些都是可用的并且默认启用。

### 依赖注入

Litestar 有一个简单但强大的 DI 系统，灵感来自 pytest。你可以在应用程序的不同级别定义命名依赖项（同步或异步），然后选择性地使用或覆盖它们。

<details>
<summary>DI 示例</summary>

```python
from litestar import Litestar, get
from litestar.di import Provide


async def my_dependency() -> str: ...


@get("/")
async def index(injected: str) -> str:
    return injected


app = Litestar([index], dependencies={"injected": Provide(my_dependency)})
```

</details>

### 中间件

Litestar 支持典型的 ASGI 中间件，并附带中间件来处理诸如

- CORS
- CSRF
- 速率限制
- GZip、Brotli 和 Zstd 压缩
- 客户端和服务器端会话

### 路由守卫

Litestar 有一个名为 `guards` 的授权机制，允许用户在应用程序的不同级别（应用、路由器、控制器等）定义守卫函数，并在访问路由处理函数之前验证请求。

<details>
<summary>路由守卫示例</summary>

```python
from litestar import Litestar, get

from litestar.connection import ASGIConnection
from litestar.handlers.base import BaseRouteHandler
from litestar.exceptions import NotAuthorizedException


async def is_authorized(connection: ASGIConnection, handler: BaseRouteHandler) -> None:
    # 验证授权
    # 如果未授权，引发 NotAuthorizedException
    raise NotAuthorizedException()


@get("/", guards=[is_authorized])
async def index() -> None: ...


app = Litestar([index])
```

</details>

### 请求生命周期挂钩

Litestar 支持请求生命周期挂钩，类似于 Flask - 即 `before_request` 和 `after_request`

## 性能

Litestar 速度很快。它与类似的 ASGI 框架相当，或明显更快。

你可以在[这里](https://github.com/litestar-org/api-performance-tests)查看并运行基准测试，或者在我们的文档中[这里](https://docs.litestar.dev/latest/benchmarks)阅读更多相关信息。

## 贡献

Litestar 欢迎大大小小的贡献。你可以随时[加入我们的 discord](https://discord.gg/litestar) 服务器或[加入我们的 Matrix](https://matrix.to/#/#litestar:matrix.org) 空间来讨论贡献和项目维护。有关如何贡献的指南，请参阅[贡献指南](CONTRIBUTING.rst)。
