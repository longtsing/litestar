集成第三方库
=============

Litestar 可与多种第三方库集成，如数据库 ORM、认证、缓存等。

- **数据库**：推荐使用 SQLAlchemy、Tortoise ORM 等。
- **认证**：可集成 OAuth2、JWT 等认证方案。
- **缓存**：支持 Redis、Memcached 等。

示例：集成 SQLAlchemy

.. code-block:: python

    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("sqlite:///test.db")
    SessionLocal = sessionmaker(bind=engine)

    # 在处理器中使用 SessionLocal

更多集成方案请参考相关库文档。