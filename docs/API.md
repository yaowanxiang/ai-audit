# API 文档
# API Documentation

## 核心 API / Core API

### 1. 审计扫描 / Audit Scan

#### Python API
```python
from ai_audit import Auditor

# 初始化审计器 / Initialize auditor
auditor = Auditor(
    config_path='audit.yaml',
    lang='zh-CN'  # 支持: zh-CN, en-US, ja-JP, ko-KR, fr-FR, de-DE, es-ES
)

# 扫描代码 / Scan code
result = auditor.scan(
    path='./src',
    rules=['hallucination', 'data_pollution', 'standard_mapping']
)

# 获取报告 / Get report
report = result.generate_report(format='json')
```

#### CLI
```bash
# 基础扫描 / Basic scan
ai-audit scan ./src

# 指定规则 / Specify rules
ai-audit scan ./src --rules hallucination,data_pollution

# 指定语言 / Specify language
ai-audit scan ./src --lang en-US

# 生成报告 / Generate report
ai-audit scan ./src --output report.json --format json
```

#### REST API
```bash
POST /api/v1/scan
Content-Type: application/json

{
  "path": "./src",
  "rules": ["hallucination", "data_pollution"],
  "lang": "zh-CN"
}

# Response / 响应
{
  "status": "success",
  "scan_id": "uuid",
  "issues": [
    {
      "rule": "hallucination",
      "severity": "high",
      "file": "src/main.py",
      "line": 42,
      "message": "未经证实的引用 / Unverified reference"
    }
  ]
}
```

---

### 2. 幻觉检测 / Hallucination Detection

#### Python API
```python
from ai_audit.detectors import HallucinationDetector

detector = HallucinationDetector()

# 检测单个文件 / Detect single file
issues = detector.detect_file('src/main.py')

# 检测代码片段 / Detect code snippet
code = """
# 根据Nature 2023年研究 / According to Nature 2023 research
result = model.predict(data)
"""
issues = detector.detect_code(code)

# 验证引用 / Verify reference
is_valid = detector.verify_reference(
    citation='Nature, 2023, Vol. 615, pp. 123-145',
    context='machine learning'
)
```

#### 检测规则 / Detection Rules
```yaml
hallucination:
  patterns:
    - '根据.*研究'  # According to ... research
    - 'According to.*'
    - '实验表明'  # Experiments show
    - 'Studies show'
  verification:
    - check_citation_format
    - search_academic_database
    - verify_publication_date
```

---

### 3. 数据污染标记 / Data Contamination Marking

#### Python API
```python
from ai_audit.markers import DataPollutionMarker

marker = DataPollutionMarker()

# 标记外部AI调用 / Mark external AI call
marked_code = marker.mark_ai_call(
    code=code,
    ai_info={
        'provider': 'OpenAI',
        'model': 'gpt-4',
        'version': '0613',
        'confidence': 0.85
    }
)

# 检查标记完整性 / Check marking completeness
is_complete = marker.check_completeness(code)

# 生成溯源报告 / Generate traceability report
report = marker.generate_trace_report(code)
```

#### 标记格式 / Marking Format
```python
# 标记前 / Before marking
result = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)

# 标记后 / After marking
# AI_SOURCE: OpenAI/gpt-4/0613
# AI_CONFIDENCE: 0.85
# AI_TIMESTAMP: 2024-01-15T10:30:00Z
result = openai.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": "Hello"}]
)
```

---

### 4. 规范映射 / Standard Mapping

#### Python API
```python
from ai_audit.mappers import StandardMapper

mapper = StandardMapper()

# GB/T → SLSA 映射 / GB/T → SLSA mapping
slsa_level = mapper.map_gbt_to_slsa(
    gbt_requirement='GB/T 38626-2020 4.3.2'
)
# Output: SLSA Level 3

# SLSA → EU AI Act 映射 / SLSA → EU AI Act mapping
eu_risk = mapper.map_slsa_to_eu(
    slsa_level=3
)
# Output: Limited Risk

# 反向映射 / Reverse mapping
gbt_requirements = mapper.map_eu_to_gbt(
    eu_risk_level='High Risk'
)
# Output: ['GB/T 38626-2020 4.3.2', 'GB/T 38626-2020 4.5.1']
```

#### 映射表 / Mapping Table
```yaml
mapping:
  GB/T 38626-2020:
    4.3.2:
      slsa: Level 3
      eu_ai_act: Limited Risk
      description: "代码可追溯性 / Code traceability"
    4.5.1:
      slsa: Level 4
      eu_ai_act: High Risk
      description: "安全性测试 / Security testing"
```

---

## MCP 服务器 API / MCP Server API

### 启动服务器 / Start Server
```bash
ai-audit mcp start --port 8080
```

### 工具列表 / Tool List
```json
{
  "tools": [
    {
      "name": "scan_code",
      "description": "扫描代码并生成审计报告 / Scan code and generate audit report",
      "input_schema": {
        "type": "object",
        "properties": {
          "path": {"type": "string"},
          "rules": {"type": "array"}
        }
      }
    },
    {
      "name": "detect_hallucination",
      "description": "检测AI幻觉 / Detect AI hallucination",
      "input_schema": {
        "type": "object",
        "properties": {
          "code": {"type": "string"}
        }
      }
    },
    {
      "name": "mark_data_pollution",
      "description": "标记数据污染 / Mark data contamination",
      "input_schema": {
        "type": "object",
        "properties": {
          "code": {"type": "string"},
          "ai_info": {"type": "object"}
        }
      }
    },
    {
      "name": "map_standard",
      "description": "规范映射 / Standard mapping",
      "input_schema": {
        "type": "object",
        "properties": {
          "from": {"type": "string"},
          "to": {"type": "string"},
          "requirement": {"type": "string"}
        }
      }
    }
  ]
}
```

### 调用示例 / Call Example
```bash
curl -X POST http://localhost:8080/tools/scan_code \
  -H "Content-Type: application/json" \
  -d '{
    "path": "./src",
    "rules": ["hallucination", "data_pollution"]
  }'
```

---

## CI/CD 集成 / CI/CD Integration

### GitHub Actions
```yaml
name: AI Code Audit

on: [push, pull_request]

jobs:
  audit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Install AI Audit
        run: |
          curl -fsSL https://raw.githubusercontent.com/yaowanxiang/ai-audit/main/install.sh | bash
      
      - name: Run Audit
        run: |
          ai-audit scan . --output audit-report.json
      
      - name: Upload Report
        uses: actions/upload-artifact@v3
        with:
          name: audit-report
          path: audit-report.json
```

### GitLab CI
```yaml
audit:
  stage: test
  script:
    - curl -fsSL https://raw.githubusercontent.com/yaowanxiang/ai-audit/main/install.sh | bash
    - ai-audit scan . --output audit-report.json
  artifacts:
    paths:
      - audit-report.json
    reports:
      junit: audit-report.json
```

---

## 报告格式 / Report Formats

### JSON 格式 / JSON Format
```json
{
  "version": "1.0.0",
  "timestamp": "2024-01-15T10:30:00Z",
  "summary": {
    "total_files": 150,
    "total_issues": 23,
    "severity": {
      "high": 5,
      "medium": 12,
      "low": 6
    }
  },
  "issues": [
    {
      "id": "H001",
      "rule": "hallucination",
      "severity": "high",
      "file": "src/main.py",
      "line": 42,
      "column": 15,
      "message": "未经证实的引用 / Unverified reference",
      "suggestion": "请提供完整的引用信息 / Please provide complete citation"
    }
  ]
}
```

### HTML 格式 / HTML Format
```bash
ai-audit scan ./src --output report.html --format html
```

### Markdown 格式 / Markdown Format
```bash
ai-audit scan ./src --output report.md --format markdown
```

---

## 错误代码 / Error Codes

| 代码 / Code | 含义 / Meaning | 解决方案 / Solution |
|------|--------|------------|
| E001 | 配置文件无效 / Invalid config file | 检查YAML格式 / Check YAML format |
| E002 | 路径不存在 / Path not found | 检查文件路径 / Check file path |
| E003 | 规则未定义 / Rule undefined | 检查规则名称 / Check rule name |
| E004 | API认证失败 / API auth failed | 检查API密钥 / Check API key |
| E005 | 网络连接失败 / Network failed | 检查网络连接 / Check network |

---

## 性能优化 / Performance Optimization

### 并行扫描 / Parallel Scanning
```python
auditor = Auditor(
    workers=4,  # 并行工作线程数 / Number of parallel workers
    batch_size=100  # 批处理大小 / Batch size
)
```

### 缓存配置 / Cache Configuration
```python
auditor = Auditor(
    cache_enabled=True,
    cache_dir='.ai-audit-cache',
    cache_ttl=3600  # 缓存有效期(秒) / Cache TTL (seconds)
)
```

### 增量扫描 / Incremental Scanning
```bash
ai-audit scan ./src --incremental --baseline baseline.json
```

---

## 扩展开发 / Extension Development

### 自定义规则 / Custom Rules
```python
from ai_audit.rules import BaseRule

class MyCustomRule(BaseRule):
    name = 'my_custom_rule'
    description = 'My custom audit rule'
    
    def check(self, code, context):
        # 实现检测逻辑 / Implement detection logic
        issues = []
        # ... 检测代码 / ... detection code
        return issues

# 注册规则 / Register rule
auditor.register_rule(MyCustomRule())
```

### 自定义输出格式 / Custom Output Format
```python
from ai_audit.formatters import BaseFormatter

class MyFormatter(BaseFormatter):
    name = 'my_format'
    
    def format(self, report):
        # 实现格式化逻辑 / Implement formatting logic
        return formatted_output

# 注册格式化器 / Register formatter
auditor.register_formatter(MyFormatter())
```

---

## 支持 / Support

- 文档 / Documentation: https://ai-code-audit.org
- GitHub Issues: https://github.com/yaowanxiang/ai-audit/issues
- Email: yaowanxiang@qut.edu.cn