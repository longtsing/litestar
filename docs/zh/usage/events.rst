事件
======

Litestar 支持事件发射器/监听器模式的简单实现：

.. code-block:: python

    from dataclasses import dataclass

    from litestar import Request, post
    from litestar.events import listener
    from litestar import Litestar

    from db import user_repository
    from utils.email import send_welcome_mail


    @listener("user_created")
    async def send_welcome_email_handler(email: str) -> None:
        # 在这里做一些事情来发送电子邮件
        await send_welcome_mail(email)


    @dataclass
    class CreateUserDTO:
        first_name: str
        last_name: str
        email: str


    @post("/users")
    async def create_user_handler(data: UserDTO, request: Request) -> None:
        # 在这里做一些事情来创建新用户
        # 例如，将用户插入数据库
        await user_repository.insert(data)

        # 假设我们现在已经插入了一个用户，我们想发送一封欢迎邮件。
        # 为了以非阻塞的方式做到这一点，我们将向监听器发出一个事件，该监听器将发送电子邮件，
        # 使用与我们返回响应的不同的异步块。
        request.app.emit("user_created", email=data.email)


    app = Litestar(
        route_handlers=[create_user_handler], listeners=[send_welcome_email_handler]
    )


上面的示例说明了这种模式的强大之处 - 它允许我们在不阻塞的情况下执行异步操作，并且不会减慢响应周期。
