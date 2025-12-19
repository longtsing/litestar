#!/usr/bin/env python3
"""
安装中文文档构建依赖
"""

import subprocess
import sys

def run_command(cmd, description):
    """运行命令并处理结果"""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        if result.returncode == 0:
            print(f"✅ {description} - 成功")
        else:
            print(f"❌ {description} - 失败")
            print("错误:", result.stderr)
            return False
    except Exception as e:
        print(f"❌ {description} - 异常: {e}")
        return False
    return True

def main():
    """主函数"""
    print("🚀 开始安装 Litestar 中文文档构建依赖...")
    
    # 基础依赖
    deps = [
        "sphinx>=7.1.2",
        "sphinx-autobuild>=2021.3.14", 
        "sphinx-copybutton>=0.5.2",
        "sphinx-toolbox>=3.5.0",
        "sphinx-design>=0.5.0",
        "sphinx-click>=4.4.0",
        "sphinxcontrib-mermaid>=0.9.2",
        "auto-pytabs[sphinx]>=0.5.0",
        "sphinx-paramlinks>=0.6.0",
    ]
    
    # 安装依赖
    for dep in deps:
        if not run_command(f'pip install "{dep}"', f"安装 {dep}"):
            print("❌ 依赖安装失败，尝试继续...")
    
    # 安装主题
    theme_cmd = 'pip install "litestar-sphinx-theme @ git+https://github.com/litestar-org/litestar-sphinx-theme.git@v3"'
    run_command(theme_cmd, "安装 Litestar Sphinx 主题")
    
    print("✅ 依赖安装完成!")
    print("现在可以运行 'python build.py' 来构建文档")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())