#!/usr/bin/env python3
"""
AI Audit Desktop Client — GUI entry point
AI代码认证体系 桌面客户端 — 图形界面入口

A fool-proof, drag-and-drop GUI for AI code auditing.
傻瓜化图形界面：拖入代码文件夹 → 点击扫描 → 查看报告
"""

import sys
import os
import json
import datetime
from pathlib import Path

# Ensure GUI package is importable when running from source
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

try:
    from PySide6.QtWidgets import (
        QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
        QLabel, QPushButton, QFileDialog, QTextEdit, QProgressBar,
        QComboBox, QMessageBox, QGroupBox, QCheckBox, QTabWidget,
        QListWidget, QListWidgetItem, QSplitter, QFrame
    )
    from PySide6.QtCore import Qt, QThread, Signal, QSize
    from PySide6.QtGui import QFont, QIcon, QPalette, QColor
except ImportError:
    print("=" * 60)
    print("Missing dependency: PySide6")
    print("安装图形界面依赖:  pip install PySide6")
    print("Install GUI dependency: pip install PySide6")
    print("=" * 60)
    sys.exit(1)


# ─────────────────────────────────────────────────────────────
# 核心引擎桥接 (Core engine bridge)
# ─────────────────────────────────────────────────────────────
class AuditWorker(QThread):
    """后台审计线程 — 保持界面不卡顿"""

    progress = Signal(int, str)      # (percent, status_text)
    finished_ok = Signal(dict)       # audit results
    failed = Signal(str)             # error message

    def __init__(self, folder: str, rules: list, lang: str):
        super().__init__()
        self.folder = folder
        self.rules = rules
        self.lang = lang

    def run(self):
        try:
            total_steps = 5
            self.progress.emit(10, "Scanning files... / 扫描文件中...")

            # ── Step 1: collect source files ──
            code_exts = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.h',
                         '.go', '.rs', '.kt', '.swift', '.php', '.rb', '.cs'}
            files = []
            root = Path(self.folder)
            for p in root.rglob("*"):
                if p.is_file() and p.suffix in code_exts:
                    files.append(p)
            self.progress.emit(30, f"Found {len(files)} source files / 发现 {len(files)} 个源文件")

            # ── Step 2: run rules (placeholder core engine) ──
            issues = []
            for i, f in enumerate(files):
                if i % max(1, len(files) // 10) == 0:
                    pct = 30 + int(40 * i / max(1, len(files)))
                    self.progress.emit(pct, f"Analyzing / 分析中: {f.name}")
                try:
                    text = f.read_text(encoding='utf-8', errors='ignore')
                except Exception:
                    continue
                # simple heuristic checks
                for line_no, line in enumerate(text.splitlines(), 1):
                    low = line.lower()
                    if 'hallucination' in self.rules:
                        if 'according to' in low or '据' in line and ('研究' in line or '文献' in line):
                            issues.append({
                                'rule': 'hallucination', 'severity': 'high',
                                'file': str(f), 'line': line_no,
                                'msg': 'Unverified reference / 未经证实的引用'
                            })
                    if 'data_pollution' in self.rules:
                        if 'openai' in low or 'anthropic' in low or 'gpt-' in low or 'claude' in low:
                            issues.append({
                                'rule': 'data_pollution', 'severity': 'medium',
                                'file': str(f), 'line': line_no,
                                'msg': 'External AI call / 外部AI调用'
                            })
            self.progress.emit(75, "Generating report... / 生成报告中...")

            # ── Step 3: build report ──
            report = {
                'folder': self.folder,
                'lang': self.lang,
                'time': datetime.datetime.now().isoformat(),
                'files_scanned': len(files),
                'issues': issues[:500],
                'summary': {
                    'total': len(issues),
                    'high': sum(1 for i in issues if i['severity'] == 'high'),
                    'medium': sum(1 for i in issues if i['severity'] == 'medium'),
                    'low': sum(1 for i in issues if i['severity'] == 'low'),
                }
            }
            self.progress.emit(100, "Done! / 完成！")
            self.finished_ok.emit(report)

        except Exception as e:
            self.failed.emit(str(e))


# ─────────────────────────────────────────────────────────────
# 主窗口 (Main Window)
# ─────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    APP_NAME = "AI Audit Desktop / AI代码认证桌面客户端"
    VERSION = "v0.3.0"

    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{self.APP_NAME} {self.VERSION}")
        self.resize(900, 650)
        self.setMinimumSize(720, 520)
        self._build_ui()
        self._apply_style()

    # ── UI 构建 ──
    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        root = QVBoxLayout(central)
        root.setContentsMargins(24, 20, 24, 20)
        root.setSpacing(14)

        # ── Header ──
        header = QHBoxLayout()
        title = QLabel("🛡️  AI Code Audit  /  AI代码认证")
        title.setObjectName("title")
        header.addWidget(title)
        header.addStretch()
        ver = QLabel(self.VERSION)
        ver.setObjectName("version")
        header.addWidget(ver)
        root.addLayout(header)

        # ── Step 1: 选择文件夹 ──
        step1 = QGroupBox("①  选择要审计的代码文件夹  /  Select Code Folder")
        s1 = QHBoxLayout(step1)
        self.folder_label = QLabel("📁  drag & drop folder here  /  拖入文件夹，或点击浏览")
        self.folder_label.setObjectName("dropzone")
        self.folder_label.setAlignment(Qt.AlignCenter)
        self.folder_label.setMinimumHeight(72)
        s1.addWidget(self.folder_label, 1)
        browse_btn = QPushButton("📂  Browse / 浏览...")
        browse_btn.setObjectName("primary")
        browse_btn.clicked.connect(self._browse_folder)
        s1.addWidget(browse_btn)
        root.addWidget(step1)

        # ── Step 2: 选项 ──
        step2 = QGroupBox("②  审计选项  /  Audit Options")
        s2 = QHBoxLayout(step2)

        self.chk_hallucination = QCheckBox("AI幻觉检测  /  Hallucination")
        self.chk_hallucination.setChecked(True)
        self.chk_pollution = QCheckBox("数据污染标记  /  Data Pollution")
        self.chk_pollution.setChecked(True)

        lang_label = QLabel("语言 / Language:")
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(["中文 (zh-CN)", "English (en-US)", "日本語 (ja-JP)", "한국어 (ko-KR)"])
        self.lang_combo.setFixedWidth(160)

        s2.addWidget(self.chk_hallucination)
        s2.addWidget(self.chk_pollution)
        s2.addStretch()
        s2.addWidget(lang_label)
        s2.addWidget(self.lang_combo)
        root.addWidget(step2)

        # ── Step 3: 开始按钮 + 进度 ──
        step3 = QHBoxLayout()
        self.scan_btn = QPushButton("▶  开始审计  /  Start Audit")
        self.scan_btn.setObjectName("big")
        self.scan_btn.setMinimumHeight(48)
        self.scan_btn.clicked.connect(self._start_scan)
        step3.addWidget(self.scan_btn, 1)

        self.export_btn = QPushButton("💾  导出报告  /  Export Report")
        self.export_btn.setObjectName("secondary")
        self.export_btn.setEnabled(False)
        self.export_btn.clicked.connect(self._export_report)
        step3.addWidget(self.export_btn)
        root.addLayout(step3)

        # 进度条
        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.status_label = QLabel("Ready / 就绪 — 请选择文件夹")
        self.status_label.setObjectName("status")
        root.addWidget(self.progress)
        root.addWidget(self.status_label)

        # ── 结果区 ──
        self.tabs = QTabWidget()
        self.summary_tab = QTextEdit()
        self.summary_tab.setReadOnly(True)
        self.issues_tab = QListWidget()
        self.tabs.addTab(self.summary_tab, "📊  汇总  /  Summary")
        self.tabs.addTab(self.issues_tab, "🔍  问题列表  /  Issues")
        root.addWidget(self.tabs, 1)

        # 底部提示
        footer = QLabel("💡  傻瓜化操作：选文件夹 → 点开始 → 看报告。无需命令行。  /  Pick folder → Start → View report. No CLI needed.")
        footer.setObjectName("footer")
        root.addWidget(footer)

        self._last_report = None

    # ── 样式 ──
    def _apply_style(self):
        self.setStyleSheet("""
            QMainWindow, QWidget { background: #f5f7fa; }
            QLabel#title { font-size: 22px; font-weight: 700; color: #1a237e; }
            QLabel#version { color: #90a4ae; font-size: 13px; }
            QGroupBox {
                font-weight: 600; color: #37474f;
                border: 1.5px solid #cfd8dc; border-radius: 8px;
                margin-top: 12px; padding-top: 8px;
                background: #ffffff;
            }
            QGroupBox::title { subcontrol-origin: margin; left: 12px; padding: 0 6px; background: #ffffff; }
            QLabel#dropzone {
                border: 2px dashed #90a4ae; border-radius: 10px;
                color: #546e7a; font-size: 15px; background: #eef3f7;
            }
            QPushButton#primary { background: #1565c0; color: white; padding: 8px 20px; border-radius: 6px; font-weight: 600; }
            QPushButton#big { background: #2e7d32; color: white; font-size: 16px; font-weight: 700; border-radius: 8px; }
            QPushButton#secondary { background: #f5f5f5; color: #37474f; padding: 8px 16px; border-radius: 6px; }
            QPushButton:hover { opacity: 0.9; }
            QProgressBar { height: 14px; border-radius: 7px; background: #e0e0e0; text-align: center; }
            QProgressBar::chunk { background: #43a047; border-radius: 7px; }
            QLabel#status { color: #546e7a; font-size: 13px; }
            QLabel#footer { color: #90a4ae; font-size: 12px; }
            QTabWidget::pane { border: 1px solid #cfd8dc; border-radius: 6px; background: white; }
            QTextEdit, QListWidget { border: none; background: white; font-size: 13px; }
            QCheckBox { font-size: 14px; color: #37474f; }
        """)

    # ── 交互 ──
    def _browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "选择代码文件夹 / Select Code Folder")
        if folder:
            self.folder_label.setText(f"📁  {folder}")
            self.folder_label.setToolTip(folder)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            if os.path.isdir(path):
                self.folder_label.setText(f"📁  {path}")
                self.folder_label.setToolTip(path)
                break

    def _start_scan(self):
        folder = self.folder_label.toolTip()
        if not folder or not os.path.isdir(folder):
            QMessageBox.warning(self, "提示 / Notice",
                                "请先选择代码文件夹！\nPlease select a code folder first!")
            return

        rules = []
        if self.chk_hallucination.isChecked():
            rules.append('hallucination')
        if self.chk_pollution.isChecked():
            rules.append('data_pollution')

        lang_map = {"中文 (zh-CN)": "zh-CN", "English (en-US)": "en-US",
                    "日本語 (ja-JP)": "ja-JP", "한국어 (ko-KR)": "ko-KR"}
        lang = lang_map.get(self.lang_combo.currentText(), "zh-CN")

        self.scan_btn.setEnabled(False)
        self.export_btn.setEnabled(False)
        self.progress.setValue(0)
        self.status_label.setText("⏳ 审计中... / Auditing...")

        self._worker = AuditWorker(folder, rules, lang)
        self._worker.progress.connect(lambda p, s: (self.progress.setValue(p), self.status_label.setText(s)))
        self._worker.finished_ok.connect(self._on_finished)
        self._worker.failed.connect(self._on_failed)
        self._worker.start()

    def _on_finished(self, report):
        self._last_report = report
        self.scan_btn.setEnabled(True)
        self.export_btn.setEnabled(True)
        self.status_label.setText("✅ 审计完成！/ Audit complete!")

        s = report['summary']
        self.summary_tab.setPlainText(
            "═══════════════════════════════════════════\n"
            "  AI Code Audit Report / AI代码审计报告\n"
            "═══════════════════════════════════════════\n\n"
            f"  文件夹 / Folder : {report['folder']}\n"
            f"  时间 / Time     : {report['time']}\n"
            f"  语言 / Language : {report['lang']}\n"
            f"  文件数 / Files  : {report['files_scanned']}\n\n"
            "  ── 结果 / Results ──\n"
            f"  总计 / Total    : {s['total']}\n"
            f"  🔴 高 / High    : {s['high']}\n"
            f"  🟠 中 / Medium  : {s['medium']}\n"
            f"  🟢 低 / Low     : {s['low']}\n\n"
            "  详细问题见「问题列表」标签页。\n"
            "  See the Issues tab for details."
        )

        self.issues_tab.clear()
        if not report['issues']:
            self.issues_tab.addItem("🎉 未发现问题！/ No issues found!")
        for issue in report['issues'][:500]:
            icon = {"high": "🔴", "medium": "🟠", "low": "🟢"}.get(issue['severity'], "⚪")
            short_file = os.path.basename(issue['file'])
            item = QListWidgetItem(f"{icon} [{issue['rule']}] {short_file}:{issue['line']} — {issue['msg']}")
            item.setToolTip(issue['file'])
            self.issues_tab.addItem(item)

    def _on_failed(self, err):
        self.scan_btn.setEnabled(True)
        self.status_label.setText("❌ 审计失败 / Audit failed")
        QMessageBox.critical(self, "错误 / Error", str(err))

    def _export_report(self):
        if not self._last_report:
            return
        default_name = f"ai-audit-report-{datetime.date.today().isoformat()}.json"
        path, _ = QFileDialog.getSaveFileName(self, "保存报告 / Save Report", default_name, "JSON (*.json);;HTML (*.html)")
        if not path:
            return
        try:
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(self._last_report, f, ensure_ascii=False, indent=2)
            QMessageBox.information(self, "完成 / Done", f"报告已保存：\n{path}\n\nReport saved.")
        except Exception as e:
            QMessageBox.critical(self, "错误 / Error", str(e))


# ─────────────────────────────────────────────────────────────
# 入口 (Entry point)
# ─────────────────────────────────────────────────────────────
def main():
    app = QApplication(sys.argv)
    app.setApplicationName("AI Audit")
    app.setOrganizationName("AI Audit")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
