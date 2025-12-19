# 构建中文文档

本文档说明如何在 conda webdev 环境中构建 Litestar 中文文档。

## 快速开始

### 1. 激活 conda webdev 环境

**Linux/macOS:**
```bash
conda activate webdev
```

**Windows:**
```cmd
conda activate webdev
```

### 2. 安装构建依赖

```bash
# 安装项目本身（如果还没有安装）
pip install -e .

# 安装文档构建依赖
python install_deps.py
```

或者手动安装：
```bash
pip install sphinx sphinx-autobuild sphinx-copybutton sphinx-toolbox sphinx-design sphinx-click sphinxcontrib-mermaid auto-pytabs sphinx-paramlinks
pip install "litestar-sphinx-theme @ git+https://github.com/litestar-org/litestar-sphinx-theme.git@v3"
```

### 3. 构建文档

```bash
# 使用 Python 脚本构建（推荐）
python build.py

# 或使用 Makefile 构建
make build

# 或直接使用 sphinx-build
sphinx-build -b html -E -a -j auto . _build/
```

### 4. 查看结果

构建完成后，HTML 文件将位于 `_build/index.html`，可以在浏览器中打开。

## 开发模式

如果要在开发时实时预览文档：

```bash
# 启动自动重新构建的服务器
make serve

# 或使用 sphinx-autobuild
sphinx-autobuild . _build/ -j auto --open-browser --port=8000
```

## 构建脚本说明

- `build.py` - 主要的 Python 构建脚本
- `Makefile` - 构建命令集合
- `install_deps.py` - 依赖安装脚本
- `build_conda.sh` / `build_conda.bat` - 一键构建脚本

## 故障排除

### 问题：找不到 sphinx-build 命令
```bash
# 确保在正确的 conda 环境中
conda activate webdev
pip install sphinx
```

### 问题：找不到 litestar-sphinx-theme
```bash
# 重新安装主题
pip install "litestar-sphinx-theme @ git+https://github.com/litestar-org/litestar-sphinx-theme.git@v3"
```

### 问题：构建时出现编码错误
确保终端支持 UTF-8 编码，特别是在 Windows 上。

## 构建产物

- HTML 文档：`_build/` 目录
- 可以通过浏览器打开 `_build/index.html` 查看
- 支持本地文件服务器或通过 HTTP 服务器访问

---

**注意**：确保 Python 版本为 3.9 或更高版本，推荐使用 Python 3.12。