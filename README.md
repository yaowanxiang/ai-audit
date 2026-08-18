# AI Code Audit Framework (AI代码认证体系)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yaowanxiang/ai-audit/pulls)
[![Cross-Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-blue.svg)](https://github.com/yaowanxiang/ai-audit/releases)

An international AI code security certification framework that audits AI hallucination, tracks data provenance, and maps compliance across global standards — GB/T, SLSA, and EU AI Act.

> 🖥️ **Desktop Client Available / 桌面客户端可用!**  
> Download ready-to-install packages for Windows / macOS / Linux from [Releases](https://github.com/yaowanxiang/ai-audit/releases) — no command line needed.
> 从 Releases 下载 Windows / macOS / Linux 独立安装包，傻瓜化图形界面，无需命令行。

## Why AI Audit?

As AI-generated code becomes mainstream, verifying **what** an AI wrote, **where** the data came from, and **whether** it complies with regulations is critical. AI Audit provides:

- 🖥️ **Desktop GUI** — fool-proof drag-and-drop interface (Windows / macOS / Linux)
- 🔍 **Hallucination Detection** — flags unverified references and fabricated citations
- 🏷️ **Data Contamination Marking** — tags external AI calls with source/version/confidence
- 🔄 **Standard Mapping** — bidirectional conversion between GB/T ↔ SLSA ↔ EU AI Act
- 🌍 **7-Language Support** — zh, en, ja, ko, fr, de, es

## Quick Start — Desktop App / 桌面客户端快速开始

### Download / 下载

| Platform | Package | How to use |
|----------|---------|-----------|
| Windows | `AI-Audit-Setup-<ver>.exe` | Double-click, Next → Next → Finish |
| macOS | `AI-Audit-<ver>.dmg` | Drag to Applications |
| Linux | `AI-Audit-<ver>.AppImage` | `chmod +x`, double-click |

**Download here / 下载地址**: https://github.com/yaowanxiang/ai-audit/releases

### Use / 使用

1. **Open the app** / 打开应用
2. **Drag your code folder in** / 把代码文件夹拖进去（或点「浏览」）
3. **Click Start Audit** / 点击「开始审计」
4. **Read the report** / 查看报告（支持导出 JSON/HTML）

That's it. No terminal, no commands. / 就这么简单，无需命令行。

## Quick Start — CLI (Advanced / 高级用户)

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/yaowanxiang/ai-audit/main/install.sh | bash

# Scan
ai-audit scan --lang python --rules hallucination,data-pollution

# Generate report
ai-audit report --format html --lang en
```

## Features

| Feature | Description |
|---------|-------------|
| AI Hallucination Detection | Detect unverified references and unclear data sources |
| Data Contamination Marking | Tag external AI calls with source/version/confidence |
| Standard Mapping Layer | Bidirectional conversion between GB/T, SLSA, and EU AI Act |
| SBOM Generation | SPDX / CycloneDX output |
| CI/CD Integration | GitHub Actions, GitLab CI templates included |
| Bilingual Reports | Chinese/English report generation |

## Architecture

```
┌─────────────────────────────────────┐
│  Dashboard (Bilingual Reports)      │
└─────────────────────────────────────┘
           ↑
┌─────────────────────────────────────┐
│  Audit Engine                       │
│  - Hallucination Detection          │
│  - Data Contamination Marking       │
│  - Standard Mapping (GB/T↔SLSA↔EU)  │
└─────────────────────────────────────┘
           ↑
┌─────────────────────────────────────┐
│  Collection Layer                   │
│  - Tree-sitter (Py/JS/Java/C++)     │
│  - LLM Call Interception            │
└─────────────────────────────────────┘
```

## Documentation

- [MVP Technical Proposal](./MVP技术方案.md) — architecture & design
- [API Reference](./docs/API.md) — full API documentation
- [Bilingual Mapping Table](./docs/双语对照表.md) — GB/T ↔ SLSA ↔ EU AI Act
- [Multi-language Configuration](./docs/多语言配置.md) — 7 languages
- [Contributing Guide](./docs/CONTRIBUTING.md) — how to contribute
- [Example Pipelines](./examples/样例流水线.md) — usage examples
- [Cross-Platform Build Plan](./build/跨平台构建方案.md) — GUI & installers for Windows/macOS/Linux

## Roadmap

| Phase | Scope | Timeline |
|-------|-------|----------|
| **v0.1.0** | Core engine, CLI, docs | ✅ Released 2026-08 |
| **v0.2.x** | International branding, English-first UI | ✅ Released 2026-08 |
| **v0.3.0** | 🖥️ Desktop GUI + cross-platform installers | 🔄 Building now |
| **v0.4.0** | MCP server, Dashboard, 10+ pipeline templates | Next |
| **v0.5.0** | PMC governance, international CI, 100+ case studies | Later |

## Community

- [GitHub Issues](https://github.com/yaowanxiang/ai-audit/issues) — bug reports & feature requests
- [Discussions](https://github.com/yaowanxiang/ai-audit/discussions) — Q&A and ideas
- [Email](mailto:yaowanxiang@qut.edu.cn) — direct contact

## License

[MIT License](./LICENSE)

---

**AI代码认证体系** — An open-source AI code audit framework, built by and for the global community.

---

# 🇨🇳 中文版介绍

## AI 代码认证体系（AI Code Audit Framework）

一个面向国际的 **AI 代码安全认证框架**：审计 AI 幻觉（虚假引用/未验证来源）、追踪数据溯源、并映射全球合规标准（GB/T、SLSA、欧盟 AI 法案）。

### 为什么需要它？

AI 生成代码已经成为主流，但随之而来三个关键问题：**AI 写的到底是什么？数据从哪来？是否符合法规？** AI Audit 一次性解决：

- 🖥️ **桌面图形界面** —— 傻瓜式拖拽操作（Windows / macOS / Linux）
- 🔍 **幻觉检测** —— 标记未验证的引用和编造的引用
- 🏷️ **数据污染标记** —— 为外部 AI 调用打上来源/版本/置信度标签
- 🔄 **标准映射** —— GB/T ↔ SLSA ↔ 欧盟 AI 法案 双向转换
- 🌍 **7 语言支持** —— 中、英、日、韩、法、德、西

### 🖥️ 桌面客户端快速开始

| 平台 | 安装包 | 用法 |
|---|---|---|
| Windows | `AI-Audit-Setup-<版本>.exe` | 双击安装，下一步 → 下一步 → 完成 |
| macOS | `AI-Audit-<版本>.dmg` | 拖入「应用程序」文件夹 |
| Linux | `AI-Audit-<版本>.AppImage` | `chmod +x` 后双击运行 |

**下载地址**：https://github.com/yaowanxiang/ai-audit/releases

**使用三步**：打开应用 → 把代码文件夹拖进去 → 点「开始审计」→ 查看报告（可导出 JSON/HTML）。就这么简单，无需命令行。

### 核心特性

| 特性 | 说明 |
|---|---|
| AI 幻觉检测 | 检测未验证引用与不明确数据来源 |
| 数据污染标记 | 为外部 AI 调用标记来源/版本/置信度 |
| 标准映射层 | GB/T、SLSA、欧盟 AI 法案双向转换 |
| SBOM 生成 | SPDX / CycloneDX 格式输出 |
| CI/CD 集成 | 内置 GitHub Actions、GitLab CI 模板 |
| 双语报告 | 中英文报告生成 |

### 架构

```
┌─────────────────────────────────────┐
│  仪表盘（双语报告）                   │
└─────────────────────────────────────┘
           ↑
┌─────────────────────────────────────┐
│  审计引擎                            │
│  - 幻觉检测                          │
│  - 数据污染标记                       │
│  - 标准映射（GB/T↔SLSA↔欧盟AI法案）    │
└─────────────────────────────────────┘
           ↑
┌─────────────────────────────────────┐
│  采集层                              │
│  - Tree-sitter（Py/JS/Java/C++）    │
│  - LLM 调用拦截                       │
└─────────────────────────────────────┘
```

### 文档

- [MVP 技术方案](./MVP技术方案.md) — 架构与设计
- [API 参考](./docs/API.md) — 完整 API 文档
- [双语对照表](./docs/双语对照表.md) — GB/T ↔ SLSA ↔ 欧盟 AI 法案
- [多语言配置](./docs/多语言配置.md) — 7 种语言
- [贡献指南](./docs/CONTRIBUTING.md)
- [示例流水线](./examples/样例流水线.md)
- [跨平台构建方案](./build/跨平台构建方案.md) — Windows/macOS/Linux GUI 与安装包

### 路线图

| 阶段 | 范围 | 时间 |
|---|---|---|
| v0.1.0 | 核心引擎、CLI、文档 | ✅ 2026-08 已发布 |
| v0.2.x | 国际化品牌、英文优先 UI | ✅ 2026-08 已发布 |
| v0.3.0 | 桌面 GUI + 跨平台安装包 | 🔄 构建中 |
| v0.4.0 | MCP 服务器、仪表盘、10+ 流水线模板 | 下一步 |
| v0.5.0 | PMC 治理、国际 CI、100+ 案例 | 后续 |

### 社区

- [GitHub Issues](https://github.com/yaowanxiang/ai-audit/issues) — 问题与功能建议
- [Discussions](https://github.com/yaowanxiang/ai-audit/discussions) — 问答与想法
- [邮件](mailto:yaowanxiang@qut.edu.cn) — 直接联系

### 许可证

[MIT License](./LICENSE)

---

**AI代码认证体系** —— 一个由全球社区共建的开源 AI 代码审计框架。
