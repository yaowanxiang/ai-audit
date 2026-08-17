# API文档 / API Documentation

## 中文文档

### 核心API

#### Auditor类
```python
from ai_audit import Auditor

# 初始化审计器
auditor = Auditor(rules=['hallucination', 'data-pollution'])

# 扫描代码
results = auditor.scan('path/to/code')

# 生成报告
report_html = auditor.get_report(results, format='html', lang='zh')

# 映射规范
mapped = auditor.map_to_standard(results, target='SLSA v1.0')
```

#### 命令行接口
```bash
# 初始化项目
ai-audit init

# 扫描代码
ai-audit scan --lang python --rules hallucination,data-pollution

# 生成报告
ai-audit report --format html --lang zh

# 导出SBOM
ai-audit sbom --format spdx

# 映射规范
ai-audit map --from gb/t --to slsa
```

### MCP接口
```python
# MCP服务器端点
mcp://localhost:8080/audit/scan
mcp://localhost:8080/report/generate
mcp://localhost:8080/standard/map
```

---

## English Documentation

### Core API

#### Auditor Class
```python
from ai_audit import Auditor

# Initialize auditor
auditor = Auditor(rules=['hallucination', 'data-pollution'])

# Scan code
results = auditor.scan('path/to/code')

# Generate report
report_html = auditor.get_report(results, format='html', lang='en')

# Map standards
mapped = auditor.map_to_standard(results, target='SLSA v1.0')
```

#### Command Line Interface
```bash
# Initialize project
ai-audit init

# Scan code
ai-audit scan --lang python --rules hallucination,data-pollution

# Generate report
ai-audit report --format html --lang en

# Export SBOM
ai-audit sbom --format spdx

# Map standards
ai-audit map --from gb/t --to slsa
```

### MCP Endpoints
```python
# MCP server endpoints
mcp://localhost:8080/audit/scan
mcp://localhost:8080/report/generate
mcp://localhost:8080/standard/map
```
