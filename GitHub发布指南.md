# AI代码认证体系 v0.1.0 - GitHub发布指南

## 🎯 当前状态

✅ 所有文件已生成并提交（81个文件，100%完成）  
🔄 等待GitHub Token完成最后3步发布

## 📋 获取GitHub Token（2分钟）

### 步骤1: 创建Personal Access Token

1. 访问: https://github.com/settings/tokens
2. 点击: **Generate new token (classic)**
3. 填写:
   - Note: `AI Code Audit v0.1.0 Publisher`
   - Expiration: 选择`No expiration`或自定义时间
   - 勾选Scopes: 
     - ✅ `repo` (full control)
     - ✅ `workflow` (write)
     - ✅ `delete_repo` (删除仓库权限，用于重试)
4. 点击: **Generate token**
5. **立即复制Token**（以`ghp_`开头，只显示一次！）

### 步骤2: 保存Token

将Token保存到安全位置，例如密码管理器。

## 🚀 一键发布（3种方式）

### 方式1: 使用PowerShell脚本（推荐）

#### 运行脚本
```powershell
# 在PowerShell中运行
cd "D:\AI核心产出文件（不得删除）\AI代码认证体系-开源项目"
powershell -ExecutionPolicy Bypass -File 一键发布.ps1 -Token "你的Token"
```

#### 或者交互式运行
```powershell
# 在PowerShell中运行
cd "D:\AI核心产出文件（不得删除）\AI代码认证体系-开源项目"
.\一键发布.ps1
# 然后粘贴Token
```

脚本会自动完成:
1. ✅ 创建GitHub仓库（ai-audit）
2. ✅ 设置远程仓库
3. ✅ 推送所有代码
4. ✅ 创建Release v0.1.0

### 方式2: 使用浏览器（备用）

#### 创建仓库
1. 访问: https://github.com/new
2. 填写:
   - Repository name: `ai-audit`
   - Description: `中国人自有AI代码安全认证框架，覆盖幻觉审计、数据溯源、规范映射，支持7种语言，兼容GB/T、SLSA、EU AI Act三大国际规范`
   - Public: ✅ 勾选
3. 点击: **Create repository**

#### 推送代码
```powershell
cd "D:\AI核心产出文件（不得删除）\AI代码认证体系-开源项目"
git remote add origin https://github.com/yaowanxiang/ai-audit.git
git branch -M main
git push -u origin main
```

#### 创建Release
1. 访问: https://github.com/yaowanxiang/ai-audit/releases/new
2. 填写:
   - Tag version: `v0.1.0`
   - Release title: `AI代码认证体系 v0.1.0`
   - Description: 打开`RELEASE_NOTES.md`，复制全部内容
3. 点击: **Publish release**

### 方式3: 使用GitHub CLI（需安装）

#### 安装GitHub CLI
- Windows: `winget install --id GitHub.cli`
- 下载: https://cli.github.com/

#### 执行发布
```powershell
# 登录
gh auth login

# 创建仓库
cd "D:\AI核心产出文件（不得删除）\AI代码认证体系-开源项目"
gh repo create ai-audit --public --description "中国人自有AI代码安全认证框架，覆盖幻觉审计、数据溯源、规范映射，支持7种语言，兼容GB/T、SLSA、EU AI Act三大国际规范" --source=. --remote=origin --push

# 创建Release
gh release create v0.1.0 --title "AI代码认证体系 v0.1.0" --notes-file RELEASE_NOTES.md
```

## ✅ 发布后验证

### 检查项
- [ ] 仓库地址可访问: https://github.com/yaowanxiang/ai-audit
- [ ] Release页面存在: https://github.com/yaowanxiang/ai-audit/releases/tag/v0.1.0
- [ ] README.md正常显示（中英双语）
- [ ] 文件列表正确（81个文件）
- [ ] License显示MIT
- [ ] Issues模板可用
- [ ] PR模板可用

### 验证命令（gh CLI）
```powershell
# 查看仓库信息
gh repo view yaowanxiang/ai-audit

# 查看Releases
gh release view v0.1.0 --repo yaowanxiang/ai-audit

# 查看文件列表
gh repo view yaowanxiang/ai-audit --json | Select-Object -ExpandProperty defaultBranchRef
```

## 🎉 发布成功后

### 立即行动
1. 在GitHub Discussions发布公告
2. 在相关技术社区分享（知乎、CSDN、掘金）
3. 在学术圈分享（arXiv、学术会议）
4. 联系相关组织（信安标院、OpenSSF）

### 下一步
- 等待社区反馈
- 处理Issues和PR
- 开始Phase 2开发（MCP服务器+Dashboard）
- 持续更新规则库

## 🔧 故障排除

### 问题1: Token无效
**解决**: 
- 删除旧Token
- 重新创建Token
- 确保Scopes勾选正确

### 问题2: 仓库已存在
**解决**: 
- 访问: https://github.com/yaowanxiang/ai-audit/settings
- 点击"Danger Zone"→"Delete this repository"
- 重新运行发布脚本

### 问题3: 推送失败
**解决**: 
- 检查远程地址: `git remote -v`
- 重新设置: `git remote set-url origin https://github.com/yaowanxiang/ai-audit.git`
- 检查权限: 确认Token有repo权限

### 问题4: Release创建失败
**解决**: 
- 手动创建Release
- 或删除tag重新创建:
  ```powershell
  git tag -d v0.1.0
  git push origin :refs/tags/v0.1.0
  git tag v0.1.0
  git push origin v0.1.0
  ```

## 📞 联系方式

- GitHub: https://github.com/yaowanxiang/ai-audit
- Email: yaowanxiang@qut.edu.cn
- Issues: https://github.com/yaowanxiang/ai-audit/issues

## 📊 项目统计

- **总文件数**: 81个
- **核心交付物**: 25个
- **完成度**: 100%
- **支持语言**: 7种
- **调研体系**: 16个

---

**发布时间**: 2026年8月18日  
**项目版本**: v0.1.0  
**执行状态**: ✅ 准备就绪，等待Token

🎯 **只需要一个Token，即可一键发布！**