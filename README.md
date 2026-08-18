# AI Code Audit Framework (AI代码认证体系)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/yaowanxiang/ai-audit/pulls)

A China-originated AI code security certification framework that audits AI hallucination, tracks data provenance, and maps compliance across international standards — GB/T, SLSA, and EU AI Act.

## Why AI Audit?

As AI-generated code becomes mainstream, verifying **what** an AI wrote, **where** the data came from, and **whether** it complies with regulations is critical. AI Audit provides:

- 🔍 **Hallucination Detection** — flags unverified references and fabricated citations
- 🏷️ **Data Contamination Marking** — tags external AI calls with source/version/confidence
- 🔄 **Standard Mapping** — bidirectional conversion between GB/T ↔ SLSA ↔ EU AI Act
- 🌍 **7-Language Support** — zh, en, ja, ko, fr, de, es

## Quick Start

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

## Roadmap

| Phase | Scope | Timeline |
|-------|-------|----------|
| **v0.1.0** | Core engine, CLI, docs | ✅ Released 2026-08 |
| **v0.2.0** | MCP server, Dashboard, 10+ pipeline templates | 2 months |
| **v0.3.0** | PMC governance, international CI, 100+ case studies | 3 months |

## Community

- [GitHub Issues](https://github.com/yaowanxiang/ai-audit/issues) — bug reports & feature requests
- [Discussions](https://github.com/yaowanxiang/ai-audit/discussions) — Q&A and ideas
- [Email](mailto:yaowanxiang@qut.edu.cn) — direct contact

## License

[MIT License](./LICENSE)

---

**AI代码认证体系** — China's open-source AI code audit framework, built for the global community. 中国开源，服务全球。
