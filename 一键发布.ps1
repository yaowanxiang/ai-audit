# AI代码认证体系 v0.1.0 - 一键发布脚本
# 需要GitHub Personal Access Token

param(
    [string]$GitHubToken = ""
)

# 检查Token
if ([string]::IsNullOrEmpty($GitHubToken)) {
    Write-Host "❌ 请提供GitHub Personal Access Token" -ForegroundColor Red
    Write-Host ""
    Write-Host "获取Token步骤:" -ForegroundColor Yellow
    Write-Host "1. 访问: https://github.com/settings/tokens" -ForegroundColor Cyan
    Write-Host "2. 点击: Generate new token (classic)" -ForegroundColor Cyan
    Write-Host "3. 勾选: repo (full control), workflow (write)" -ForegroundColor Cyan
    Write-Host "4. 点击: Generate token" -ForegroundColor Cyan
    Write-Host "5. 复制Token（以ghp_开头）" -ForegroundColor Cyan
    Write-Host ""
    $GitHubToken = Read-Host "请输入Token"
}

# 请求头
$headers = @{
    "Authorization" = "token $GitHubToken"
    "Accept" = "application/vnd.github.v3+json"
}

# 创建仓库函数
function Create-GitHubRepo {
    param(
        [string]$Token,
        [string]$Name,
        [string]$Description
    )

    $body = @{
        name = $Name
        description = $Description
        private = $false
        auto_init = $false
    } | ConvertTo-Json

    $response = Invoke-RestMethod `
        -Uri "https://api.github.com/user/repos" `
        -Method POST `
        -Headers $headers `
        -Body $body `
        -ContentType "application/json"

    return $response
}

# 创建Release函数
function Create-Release {
    param(
        [string]$Token,
        [string]$Owner,
        [string]$Repo,
        [string]$Tag,
        [string]$Title,
        [string]$Notes
    )

    $body = @{
        tag_name = $Tag
        name = $Title
        body = $Notes
        draft = $false
        prerelease = $false
    } | ConvertTo-Json

    $response = Invoke-RestMethod `
        -Uri "https://api.github.com/repos/$Owner/$Repo/releases" `
        -Method POST `
        -Headers $headers `
        -Body $body `
        -ContentType "application/json"

    return $response
}

# 读取Release Notes
$releaseNotes = Get-Content "RELEASE_NOTES.md" -Raw -Encoding UTF8

# 执行发布
Write-Host "🚀 开始发布AI代码认证体系..." -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Gray

try {
    # 获取用户信息
    Write-Host "📝 获取用户信息..." -ForegroundColor Cyan
    $user = Invoke-RestMethod -Uri "https://api.github.com/user" -Headers $headers
    Write-Host "✅ 用户: $($user.login)" -ForegroundColor Green

    # 创建仓库
    Write-Host "📦 创建仓库..." -ForegroundColor Cyan
    $repo = Create-GitHubRepo -Token $GitHubToken -Name "ai-audit" -Description "中国人自有AI代码安全认证框架，覆盖幻觉审计、数据溯源、规范映射，支持7种语言，兼容GB/T、SLSA、EU AI Act三大国际规范"
    Write-Host "✅ 仓库创建成功: $($repo.html_url)" -ForegroundColor Green

    # 设置远程仓库
    Write-Host "🔗 设置远程仓库..." -ForegroundColor Cyan
    Set-Location "D:\AI核心产出文件（不得删除）\AI代码认证体系-开源项目"
    git remote remove origin -ErrorAction SilentlyContinue
    git remote add origin $repo.clone_url
    git branch -M main
    Write-Host "✅ 远程仓库已设置" -ForegroundColor Green

    # 推送代码
    Write-Host "📤 推送代码..." -ForegroundColor Cyan
    git push -u origin main
    Write-Host "✅ 代码已推送" -ForegroundColor Green

    # 创建Release
    Write-Host "🎉 创建Release..." -ForegroundColor Cyan
    $release = Create-Release -Token $GitHubToken -Owner $user.login -Repo "ai-audit" -Tag "v0.1.0" -Title "AI代码认证体系 v0.1.0" -Notes $releaseNotes
    Write-Host "✅ Release创建成功: $($release.html_url)" -ForegroundColor Green

    Write-Host ""
    Write-Host "========================================" -ForegroundColor Gray
    Write-Host "🎊 发布成功！" -ForegroundColor Green
    Write-Host ""
    Write-Host "📊 发布信息:" -ForegroundColor Yellow
    Write-Host "  仓库: $($repo.html_url)" -ForegroundColor White
    Write-Host "  Release: $($release.html_url)" -ForegroundColor White
    Write-Host ""
    Write-Host "🌐 访问:" -ForegroundColor Cyan
    Write-Host "  https://github.com/$($user.login)/ai-audit" -ForegroundColor White
    Write-Host "  https://github.com/$($user.login)/ai-audit/releases/tag/v0.1.0" -ForegroundColor White

} catch {
    Write-Host "❌ 发布失败: $($_.Exception.Message)" -ForegroundColor Red
    Write-Host ""
    Write-Host "请检查:" -ForegroundColor Yellow
    Write-Host "1. Token是否正确" -ForegroundColor Gray
    Write-Host "2. 仓库名'ai-audit'是否已被占用" -ForegroundColor Gray
    Write-Host "3. 网络连接是否正常" -ForegroundColor Gray
}

Write-Host ""
Write-Host "💡 使用方法:" -ForegroundColor Yellow
Write-Host "   powershell -ExecutionPolicy Bypass -File 一键发布.ps1 -Token '你的Token'" -ForegroundColor White