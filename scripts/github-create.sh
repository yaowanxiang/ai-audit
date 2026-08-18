#!/bin/bash
# GitHub仓库创建脚本

# 设置环境变量
REPO_NAME="ai-audit"
REPO_DESC="AI code security certification framework: hallucination audit, data provenance, standard mapping (GB/T, SLSA, EU AI Act), 7-language support"
REPO_HOMEPAGE="https://ai-code-audit.org"

echo "🔧 创建GitHub仓库: $REPO_NAME"
echo "   描述: $REPO_DESC"
echo "   主页: $REPO_HOMEPAGE"
echo

# 检查gh CLI
if ! command -v gh &> /dev/null; then
    echo "❌ GitHub CLI未安装"
    echo "请安装: https://cli.github.com/"
    exit 1
fi

# 登录检查
if ! gh auth status &> /dev/null; then
    echo "⚠️  未登录GitHub"
    echo "请运行: gh auth login"
    exit 1
fi

# 创建仓库
echo "📦 创建仓库..."
gh repo create $REPO_NAME \
    --public \
    --description "$REPO_DESC" \
    --homepage "$REPO_HOMEPAGE" \
    --source=. \
    --remote=origin \
    --push

if [ $? -eq 0 ]; then
    echo "✅ 仓库创建成功！"
    echo "🔗 仓库地址: https://github.com/yaowanxiang/$REPO_NAME"
else
    echo "❌ 仓库创建失败"
    exit 1
fi

echo
echo "🎉 完成！开始开发吧！"
echo
echo "📝 下一步："
echo "1. 访问仓库: https://github.com/yaowanxiang/$REPO_NAME"
echo "2. 查看文档: README.md, MVP技术方案.md"
echo "3. 贡献代码: docs/CONTRIBUTING.md"
echo "4. API文档: docs/API.md"
