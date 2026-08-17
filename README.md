# AI代码认证体系 (AI Code Audit Framework)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/ai-code-audit/ai-audit.svg)](https://github.com/ai-code-audit/ai-audit)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## 📖 中文简介

AI代码认证体系是中国人自有的AI代码安全认证框架，通过GitHub开源平台争夺国际话语权。该框架覆盖AI幻觉审计、数据溯源、规范映射，支持中英双语，兼容GB/T、SLSA、EU AI Act三大国际规范。

### 核心功能

- **AI幻觉检测**：自动检测未经证实的引用、数据来源不明
- **数据污染标记**：对外部AI调用标记来源/版本/置信度
- **规范映射层**：GB/T ↔ SLSA ↔ EU AI Act双向转换
- **双语支持**：中英文双语文档、报告、错误提示
- **CI/CD集成**：支持GitHub Actions、GitLab CI等主流平台

### 快速开始

```bash
# 安装
curl -fsSL https://raw.githubusercontent.com/ai-code-audit/ai-audit/main/install.sh | bash

# 扫描
ai-audit scan --lang python --rules hallucination,data-pollution

# 生成报告
ai-audit report --format html --lang zh,en
```

详细文档请查看 [MVP技术方案.md](./MVP技术方案.md)

---

## 📖 English Introduction

AI Code Audit Framework is China's proprietary AI code security certification framework, aiming to gain international discourse through GitHub open source. The framework covers AI hallucination auditing, data provenance, and standard mapping, supporting bilingual (Chinese/English) and compatible with GB/T, SLSA, and EU AI Act.

### Core Features

- **AI Hallucination Detection**: Automatically detect unverified references and unclear data sources
- **Data Contamination Marking**: Tag external AI calls with source/version/confidence
- **Standard Mapping Layer**: Bidirectional conversion between GB/T, SLSA, and EU AI Act
- **Bilingual Support**: Chinese/English documentation, reports, and error messages
- **CI/CD Integration**: Support for GitHub Actions, GitLab CI, and other mainstream platforms

### Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/ai-code-audit/ai-audit/main/install.sh | bash

# Scan
ai-audit scan --lang python --rules hallucination,data-pollution

# Generate Report
ai-audit report --format html --lang en
```

For detailed documentation, see [MVP技术方案.md](./MVP技术方案.md)

## 📚 Documentation

- [MVP技术方案](./MVP技术方案.md) - MVP Technical Architecture
- [双语对照表](./docs/双语对照表.md) - Bilingual Mapping Table
- [样例流水线](./examples/样例流水线.md) - Example Pipelines
- [安装脚本](./scripts/) - Installation Scripts
- [CI/CD模板](./templates/) - CI/CD Templates

## 🤝 Contributing

We welcome contributions! Please read our contributing guidelines.

## 📄 License

MIT License - see LICENSE file for details.

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ai-code-audit/ai-audit&type=Date)](https://star-history.com/#ai-code-audit/ai-audit&Date)
