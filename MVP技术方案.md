# AI代码认证体系 - MVP技术方案

## 核心目标
构建中国人自有AI代码安全认证框架，覆盖幻觉审计、数据溯源、规范映射，通过GitHub开源争夺国际话语权。

## 技术架构

### 三层结构
```
┌─────────────────────────────────────┐
│  Dashboard看板（双语报告导出）      │
└─────────────────────────────────────┘
           ↑
┌─────────────────────────────────────┐
│  审计引擎（静态+动态+符号执行）     │
│  - AI幻觉检测                       │
│  - 数据污染标记                     │
│  - 规范映射层（GB/T↔SLSA↔EU AI Act）│
└─────────────────────────────────────┘
           ↑
┌─────────────────────────────────────┐
│  采集层（多语言AST + 模型调用追踪） │
│  - Tree-sitter（Python/JS/Java/C++）│
│  - LLM调用拦截（LangChain/OpenAI）  │
└─────────────────────────────────────┘
```

## 关键依赖
- Python 3.11+
- Tree-sitter（多语言解析）
- LangChain（LLM调用追踪）
- Sigstore（数字签名）
- SPDX（SBOM生成）
- FastAPI（Dashboard后端）
- React/Vite（Dashboard前端）

## 核心模块

### 1. 幻觉审计模块
- 功能：检测未经证实的引用、数据来源不明
- 规则库：
  - 引用必须包含可追溯的DOI/URL
  - 数据必须标注来源/版本/采样方法
  - 机器学习模型调用必须记录超参数

### 2. 数据污染标记模块
- 功能：对外部AI调用标记来源/版本/置信度
- 实现：装饰器模式，自动记录调用链
- 输出：污染标记JSON + 可视化图谱

### 3. 规范映射层
- 功能：GB/T ↔ SLSA ↔ EU AI Act双向转换
- 维护：对照表（YAML格式）
- 自动生成：扫描结果自动映射到三种规范

## 命令行接口

```bash
# 初始化项目
ai-audit init

# 扫描代码
ai-audit scan --lang python --rules hallucination,data-pollution

# 生成报告
ai-audit report --format html,md --lang zh,en

# 导出SBOM
ai-audit sbom --format spdx,cyclonedx

# 映射规范
ai-audit map --from gb/t --to slsa
```

## API接口

```python
from ai_audit import Auditor

# 初始化
auditor = Auditor(rules=['hallucination', 'data-pollution'])

# 扫描
results = auditor.scan('path/to/code')

# 获取报告
report_html = auditor.get_report(results, format='html', lang='zh')

# 映射规范
mapped = auditor.map_to_standard(results, target='SLSA v1.0')
```

## 部署方案

### CLI工具
```bash
pip install ai-audit
ai-audit scan
```

### CI/CD集成
```yaml
# GitHub Actions
- name: AI Code Audit
  uses: ai-audit/action@v1
  with:
    rules: hallucination,data-pollution
    output: report.html
```

### Dashboard
```bash
docker run -d -p 8080:8080 ai-audit/dashboard
```

## 数据流

```
代码文件 → AST解析 → 规则匹配 → 审计结果 → 规范映射 → 报告生成 → 看板展示
```

## 质量保证

- 单元测试覆盖率 > 80%
- 集成测试覆盖10种编程语言
- 性能测试：10万行代码扫描 < 5分钟
- 安全测试：OWASP Top 10

## 国际化

- 中英文双语文档
- 中英文对照表（GB/T ↔ SLSA ↔ EU AI Act）
- 多语言错误提示
- 示例项目双语版本
