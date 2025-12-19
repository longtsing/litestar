# 中文文档构建 Makefile
# 使用 conda webdev 环境

.PHONY: help clean build serve install-deps

help: ## 显示帮助信息
	@echo "中文文档构建命令:"
	@echo "  make install-deps  - 安装构建依赖"
	@echo "  make clean         - 清理构建文件"
	@echo "  make build         - 构建 HTML 文档"
	@echo "  make serve         - 构建并启动本地服务器"

install-deps: ## 安装构建依赖
	@echo "=> 安装文档构建依赖..."
	pip install sphinx sphinx-autobuild sphinx-copybutton sphinx-toolbox sphinx-design sphinx-click sphinxcontrib-mermaid auto-pytabs sphinx-paramlinks litestar-sphinx-theme
	@echo "=> 依赖安装完成"

clean: ## 清理构建文件
	@echo "=> 清理构建文件..."
	@rm -rf _build/
	@echo "=> 清理完成"

build: clean ## 构建 HTML 文档
	@echo "=> 构建中文文档..."
	sphinx-build -b html -E -a -j auto -W --keep-going . _build/
	@echo "=> 构建完成!"
	@echo "HTML 文件位置: _build/index.html"

serve: clean ## 构建并启动本地服务器
	@echo "=> 构建并启动中文文档服务器..."
	sphinx-autobuild . _build/ -j auto --open-browser --port=8000

# 使用 Python 脚本构建
build-py: ## 使用 Python 脚本构建
	python build.py