# AI代码审计工具 - 一键安装脚本
# 支持 Windows PowerShell

Write-Host "🚀 开始安装AI代码审计工具..." -ForegroundColor Green

# 检查Python版本
$pythonVersion = python --version
Write-Host "✓ Python版本: $pythonVersion" -ForegroundColor Cyan

# 安装依赖
Write-Host "📦 安装依赖..." -ForegroundColor Yellow
pip install tree-sitter tree-sitter-python tree-sitter-javascript tree-sitter-java tree-sitter-cpp
pip install langchain spdx-tools sigstore-clicertify
pip install fastapi uvicorn

# 克隆项目
$repoUrl = "https://github.com/yaowanxiang/ai-audit.git"
$installDir = "$env:USERPROFILE\.ai-audit"

if (Test-Path $installDir) {
    Write-Host "⚠️  目录已存在，更新中..." -ForegroundColor Yellow
    Set-Location $installDir
    git pull
} else {
    Write-Host "📥 克隆项目..." -ForegroundColor Yellow
    git clone $repoUrl $installDir
}

# 添加到PATH
$env:PATH += ";$installDir"

# 永久添加到PATH
[System.Environment]::SetEnvironmentVariable('Path', $env:PATH, [System.EnvironmentVariableTarget]::User)

Write-Host "✅ 安装完成！" -ForegroundColor Green
Write-Host "运行: ai-audit --help" -ForegroundColor Cyan
