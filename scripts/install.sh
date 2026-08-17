#!/bin/bash
# AI代码审计工具 - 一键安装脚本
# 支持 Linux / macOS

set -e

echo "🚀 开始安装AI代码审计工具..."

# 检查Python版本
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "✓ Python版本: $python_version"

# 安装依赖
pip3 install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-java tree-sitter-cpp
pip3 install langchain spdx-tools sigstore-clicertify
pip3 install fastapi uvicorn

# 克隆项目
REPO_URL="https://github.com/ai-code-audit/ai-audit.git"
INSTALL_DIR="$HOME/.ai-audit"

if [ -d "$INSTALL_DIR" ]; then
    echo "⚠️  目录已存在，更新中..."
    cd "$INSTALL_DIR" && git pull
else
    echo "📥 克隆项目..."
    git clone $REPO_URL $INSTALL_DIR
fi

# 创建符号链接
ln -sf "$INSTALL_DIR/ai-audit" "$HOME/.local/bin/ai-audit"

echo "✅ 安装完成！"
echo "运行: ai-audit --help"
