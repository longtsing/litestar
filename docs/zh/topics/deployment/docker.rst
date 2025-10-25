Docker 部署
================

使用 Docker 部署 Litestar 项目可实现环境一致性与快速交付。

基本步骤：

1. 编写 `Dockerfile`，指定基础镜像与依赖安装。
2. 构建镜像：`docker build -t litestar-app .`
3. 运行容器：`docker run -p 8000:8000 litestar-app`

示例 `Dockerfile`：

.. code-block:: docker

    FROM python:3.11-slim
    WORKDIR /app
    COPY . /app
    RUN pip install -r requirements.txt
    CMD ["python", "-m", "litestar"]

更多高级用法请参考官方文档。
