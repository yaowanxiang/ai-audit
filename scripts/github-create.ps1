# GitHub仓库创建脚本

# 设置环境变量
$repoName = "ai-audit"
$repoDesc = "中国人自有AI代码安全认证框架，覆盖幻觉审计、数据溯源、规范映射，支持7种语言，兼容GB/T、SLSA、EU AI Act三大国际规范"
$repoHomepage = "https://ai-code-audit.org"

Write-Host "🔧 创建GitHub仓库: $repoName" -ForegroundColor Cyan
Write-Host "   描述: $repoDesc" -ForegroundColor Gray
Write-Host "   主页: $repoHomepage" -ForegroundColor Gray
Write-Host ""

# 检查gh CLI
$ghPath = Get-Command gh -ErrorAction SilentlyContinue
if (-not $ghPath) {
    Write-Host "❌ GitHub CLI未安装" -ForegroundColor Red
    Write-Host "请安装: https://cli.github.com/" -ForegroundColor Yellow
    exit 1
}

# 登录检查
$authStatus = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  未登录GitHub" -ForegroundColor Yellow
    Write-Host "请运行: gh auth login" -ForegroundColor Yellow
    exit 1
}

# 创建仓库
Write-Host "📦 创建仓库..." -ForegroundColor Yellow
gh repo create $repoName `
    --public `
    --description $repoDesc `
    --homepage $repoHomepage `
    --source=. `
    --remote=origin `
    --push

if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 仓库创建成功！" -ForegroundColor Green
    Write-Host "🔗 仓库地址: https://github.com/ai-code-audit/$repoName" -ForegroundColor Cyan
} else {
    Write-Host "❌ 仓库创建失败" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🎉 完成！开始开发吧！" -ForegroundColor Green
Write-Host ""
Write-Host "📝 下一步：" -ForegroundColor Yellow
Write-Host "1. 访问仓库: https://github.com/ai-code-audit/$repoName" -ForegroundColor Gray
Write-Host "2. 查看文档: README.md, MVP技术方案.md" -ForegroundColor Gray
Write-Host "3. 贡献代码: docs/CONTRIBUTING.md" -ForegroundColor Gray
Write-Host "4. API文档: docs/API.md" -ForegroundColor Gray
