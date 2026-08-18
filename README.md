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
