# 贡献指南
# Contributing Guide

感谢您对 **AI代码认证体系** 项目的关注！我们欢迎所有形式的贡献。

Thank you for your interest in the **AI Code Audit Framework** project! We welcome all forms of contributions.

---

## 目录 / Table of Contents

1. [行为准则 / Code of Conduct](#行为准则--code-of-conduct)
2. [如何贡献 / How to Contribute](#如何贡献--how-to-contribute)
3. [开发环境设置 / Development Setup](#开发环境设置--development-setup)
4. [提交规范 / Commit Convention](#提交规范--commit-convention)
5. [代码审查 / Code Review](#代码审查--code-review)
6. [文档贡献 / Documentation](#文档贡献--documentation)
7. [翻译贡献 / Translation](#翻译贡献--translation)
8. [问题报告 / Issue Reporting](#问题报告--issue-reporting)

---

## 行为准则 / Code of Conduct

### 我们的承诺 / Our Pledge

为了营造一个开放和友好的环境,我们作为贡献者和维护者承诺:无论年龄、体型、残疾、民族、性别认同和表达、经验水平、教育程度、社会经济地位、国籍、个人外貌、种族、宗教或性取向如何,参与我们的项目和社区对每个人来说都是一种无骚扰的体验。

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to make participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### 我们的标准 / Our Standards

**积极行为示例 / Examples of positive behavior:**
- 使用友好和包容的语言 / Using welcoming and inclusive language
- 尊重不同的观点和经验 / Respecting differing viewpoints and experiences
- 优雅地接受建设性批评 / Gracefully accepting constructive criticism
- 关注对社区最有利的事情 / Focusing on what is best for the community

**不可接受的行为 / Unacceptable behavior:**
- 使用性化的语言或图像 / Use of sexualized language or imagery
- 人身攻击或政治攻击 / Personal or political attacks
- 公开或私下骚扰 / Public or private harassment
- 未经明确许可发布他人的私人信息 / Publishing others' private information without permission

---

## 如何贡献 / How to Contribute

### 1. Fork 项目 / Fork the Project

```bash
# Fork 仓库 / Fork the repository
# 然后克隆到本地 / Then clone to local
git clone https://github.com/YOUR_USERNAME/ai-audit.git
cd ai-audit
```

### 2. 创建特性分支 / Create Feature Branch

```bash
# 基于 main 创建新分支 / Create new branch from main
git checkout -b feature/your-feature-name

# 或者修复bug / Or for bug fixes
git checkout -b fix/your-bug-fix
```

### 3. 提交更改 / Commit Changes

```bash
# 添加更改 / Add changes
git add .

# 提交 (遵循提交规范) / Commit (follow convention)
git commit -m "feat: add new feature"

# 推送到远程 / Push to remote
git push origin feature/your-feature-name
```

### 4. 创建 Pull Request / Create Pull Request

1. 访问您的 fork 仓库 / Visit your forked repository
2. 点击 "New Pull Request" / Click "New Pull Request"
3. 填写 PR 模板 / Fill in the PR template
4. 等待审查 / Wait for review

---

## 开发环境设置 / Development Setup

### 前置要求 / Prerequisites

- Python 3.8+ (推荐 3.10) / Python 3.8+ (3.10 recommended)
- Git 2.30+
- 操作系统 / OS: Linux, macOS, or Windows

### 安装步骤 / Installation Steps

```bash
# 1. 克隆仓库 / Clone repository
git clone https://github.com/yaowanxiang/ai-audit.git
cd ai-audit

# 2. 创建虚拟环境 / Create virtual environment
python -m venv venv

# 3. 激活虚拟环境 / Activate virtual environment
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. 安装依赖 / Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 5. 安装预提交钩子 / Install pre-commit hooks
pre-commit install

# 6. 运行测试 / Run tests
pytest tests/
```

### 开发工具 / Development Tools

```bash
# 代码格式化 / Code formatting
black src/ tests/

# 代码检查 / Code linting
flake8 src/ tests/
pylint src/ tests/

# 类型检查 / Type checking
mypy src/

# 测试覆盖率 / Test coverage
pytest --cov=src tests/
```

---

## 提交规范 / Commit Convention

我们使用 [Conventional Commits](https://www.conventionalcommits.org/) 规范。

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### 提交消息格式 / Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 类型 / Types

| 类型 / Type | 说明 / Description | 示例 / Example |
|------|--------|---------|
| `feat` | 新功能 / New feature | `feat(detector): add hallucination detection` |
| `fix` | Bug修复 / Bug fix | `fix(marker): correct data pollution marking` |
| `docs` | 文档更新 / Documentation | `docs(api): update API documentation` |
| `style` | 代码格式 / Code style | `style(core): format with black` |
| `refactor` | 重构 / Refactoring | `refactor(mapper): simplify standard mapping` |
| `test` | 测试 / Testing | `test(detector): add unit tests` |
| `chore` | 构建/工具 / Build/Tools | `chore(deps): update dependencies` |
| `perf` | 性能优化 / Performance | `perf(scan): optimize parallel scanning` |
| `ci` | CI配置 / CI config | `ci(github): add workflow for testing` |

### 示例 / Examples

```bash
# 新功能 / New feature
git commit -m "feat(detector): add hallucination detection for academic references"

# Bug修复 / Bug fix
git commit -m "fix(marker): correct AI source marking format"

# 文档更新 / Documentation
git commit -m "docs(contributing): add contribution guidelines in English"

# 重大变更 / Breaking change
git commit -m "feat(api)!: change scan API signature

BREAKING CHANGE: scan() now requires 'rules' parameter"
```

---

## 代码审查 / Code Review

### 审查清单 / Review Checklist

#### 功能性 / Functionality
- [ ] 代码实现了预期功能 / Code implements expected functionality
- [ ] 没有明显的bug / No obvious bugs
- [ ] 边界情况得到处理 / Edge cases are handled
- [ ] 错误处理完善 / Error handling is complete

#### 代码质量 / Code Quality
- [ ] 代码清晰易读 / Code is clear and readable
- [ ] 遵循项目编码规范 / Follows project coding standards
- [ ] 没有重复代码 / No code duplication
- [ ] 函数和变量命名恰当 / Proper naming

#### 测试 / Testing
- [ ] 包含单元测试 / Includes unit tests
- [ ] 测试覆盖率 ≥ 80% / Test coverage ≥ 80%
- [ ] 所有测试通过 / All tests pass
- [ ] 边界测试完整 / Edge case testing is complete

#### 文档 / Documentation
- [ ] 代码注释充分 / Adequate code comments
- [ ] API文档更新 / API documentation updated
- [ ] 更新日志更新 / Changelog updated
- [ ] 双语文档 (如适用) / Bilingual docs (if applicable)

### 审查流程 / Review Process

1. **自动检查 / Automated Checks**
   - CI/CD 流水线通过 / CI/CD pipeline passes
   - 代码覆盖率报告 / Code coverage report
   - 静态分析通过 / Static analysis passes

2. **人工审查 / Manual Review**
   - 至少1位维护者审查 / At least 1 maintainer reviews
   - 解决所有评论 / Address all comments
   - 获得批准 / Get approval

3. **合并 / Merge**
   - Squash and merge (保持历史清洁) / Squash and merge (keep history clean)
   - 删除特性分支 / Delete feature branch

---

## 文档贡献 / Documentation

### 文档类型 / Documentation Types

1. **API文档 / API Documentation**
   - 位置 / Location: `docs/API.md`
   - 格式 / Format: Markdown with code examples
   - 要求 / Requirements: 中英双语 / Bilingual (Chinese/English)

2. **用户指南 / User Guides**
   - 位置 / Location: `docs/guides/`
   - 格式 / Format: Markdown with screenshots
   - 要求 / Requirements: 逐步说明 / Step-by-step instructions

3. **开发者文档 / Developer Documentation**
   - 位置 / Location: `docs/dev/`
   - 格式 / Format: Markdown with diagrams
   - 要求 / Requirements: 架构说明 / Architecture explanation

### 文档规范 / Documentation Standards

```markdown
# 标题 / Title
# English Title

## 简介 / Introduction
中文简介...
English introduction...

## 示例 / Example
```python
# 中文注释 / English comment
code_example()
```

## 注意事项 / Notes
⚠️ 中文注意事项 / English notes
```

---

## 翻译贡献 / Translation

### 支持的语言 / Supported Languages

当前支持 / Currently supported:
- ✅ 中文 (zh-CN) - 100%
- ✅ 英语 (en-US) - 100%
- 🔄 日语 (ja-JP) - 80%
- 🔄 韩语 (ko-KR) - 80%
- 🔄 法语 (fr-FR) - 70%
- 🔄 德语 (de-DE) - 70%
- 🔄 西班牙语 (es-ES) - 60%

### 翻译流程 / Translation Process

1. **选择语言 / Choose Language**
   ```bash
   # 复制英文模板 / Copy English template
   cp locales/en-US.yaml locales/[language_code].yaml
   ```

2. **翻译内容 / Translate Content**
   - 保持技术术语一致 / Keep technical terms consistent
   - 考虑文化差异 / Consider cultural differences
   - 使用专业语言 / Use professional language

3. **审查 / Review**
   - 母语者审查 / Native speaker review
   - 术语一致性检查 / Terminology consistency check
   - 格式验证 / Format validation

4. **提交 / Submit**
   ```bash
   git add locales/[language_code].yaml
   git commit -m "feat(i18n): add [language] translation"
   git push origin feature/add-[language]-translation
   ```

### 翻译指南 / Translation Guidelines

**保持原样的术语 / Keep as-is:**
- API, CI/CD, SLSA, MCP
- Git, GitHub, GitLab
- Python, JSON, YAML

**需要翻译的术语 / Translate:**
- 功能描述 / Feature descriptions
- 错误消息 / Error messages
- 用户界面文本 / UI text

---

## 问题报告 / Issue Reporting

### 报告Bug / Reporting Bugs

使用 [Bug Report 模板](https://github.com/yaowanxiang/ai-audit/issues/new?template=bug_report.md)

Use the [Bug Report Template](https://github.com/yaowanxiang/ai-audit/issues/new?template=bug_report.md)

**必需信息 / Required Information:**
- 问题描述 / Issue description
- 复现步骤 / Steps to reproduce
- 预期行为 / Expected behavior
- 实际行为 / Actual behavior
- 环境信息 / Environment info
- 错误日志 / Error logs

### 功能请求 / Feature Requests

使用 [Feature Request 模板](https://github.com/yaowanxiang/ai-audit/issues/new?template=feature_request.md)

Use the [Feature Request Template](https://github.com/yaowanxiang/ai-audit/issues/new?template=feature_request.md)

**必需信息 / Required Information:**
- 功能描述 / Feature description
- 使用场景 / Use cases
- 预期效果 / Expected outcome
- 替代方案 / Alternatives considered

---

## 社区 / Community

### 沟通渠道 / Communication Channels

- **GitHub Issues**: 问题报告和功能请求 / Bug reports and feature requests
- **GitHub Discussions**: 一般讨论和问答 / General discussions and Q&A
- **Email**: yaowanxiang@qut.edu.cn (技术支持 / Technical support)

### 会议 / Meetings

- **开发者会议 / Developer Meeting**: 每两周一次 / Bi-weekly
- **社区会议 / Community Meeting**: 每月一次 / Monthly

---

## 许可证 / License

通过向本项目贡献代码,您同意您的贡献将在 [MIT License](LICENSE) 下发布。

By contributing to this project, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

## 致谢 / Acknowledgments

感谢所有为本项目做出贡献的开发者！

Thanks to all developers who have contributed to this project!

查看 [贡献者列表](https://github.com/yaowanxiang/ai-audit/graphs/contributors)

See the [list of contributors](https://github.com/yaowanxiang/ai-audit/graphs/contributors)

---

## 联系方式 / Contact

- **GitHub**: [@yaowanxiang](https://github.com/yaowanxiang)
- **Email**: yaowanxiang@qut.edu.cn
- **Project**: https://github.com/yaowanxiang/ai-audit

---

## 快速链接 / Quick Links

- [README](../README.md)
- [API 文档 / API Documentation](API.md)
- [多语言配置 / Multi-language Configuration](多语言配置.md)
- [问题追踪 / Issue Tracker](https://github.com/yaowanxiang/ai-audit/issues)
- [项目看板 / Project Board](https://github.com/yaowanxiang/ai-audit/projects)