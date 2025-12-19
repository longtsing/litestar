#!/usr/bin/env python3
"""
简化的中文文档构建脚本
"""

import os
import subprocess
import sys
from pathlib import Path

def main():
    """简化构建中文文档"""
    # 确保我们在正确的目录中
    docs_zh_dir = Path(__file__).parent
    build_dir = docs_zh_dir / "_build"
    
    print(f"中文文档目录: {docs_zh_dir}")
    print(f"构建目录: {build_dir}")
    
    # 清理之前的构建
    if build_dir.exists():
        print("清理之前的构建...")
        import shutil
        shutil.rmtree(build_dir)
    
    # 确保构建目录存在
    build_dir.mkdir(parents=True, exist_ok=True)
    
    # 构建 HTML 文档（忽略警告）
    print("开始构建中文文档...")
    try:
        cmd = [
            "python", "-m", "sphinx",
            "-b", "html",
            "-E",  # 重新读取所有文件
            "-a",  # 重新构建所有文件
            "-j", "auto",  # 并行构建
            str(docs_zh_dir),
            str(build_dir)
        ]
        
        print(f"执行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ 中文文档构建成功!")
            print(f"HTML 文件位置: {build_dir / 'index.html'}")
            print("可以在浏览器中打开查看:")
            print(f"file://{build_dir / 'index.html'}")
            return 0
        else:
            print("❌ 构建失败!")
            print("标准输出:")
            print(result.stdout)
            print("错误输出:")
            print(result.stderr)
            return 1
            
    except Exception as e:
        print(f"❌ 构建过程中出现错误: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())