#!/usr/bin/env python3
"""
AI Audit Desktop — launcher script
AI代码认证桌面客户端 — 启动脚本

Usage:
    python run_gui.py          # run from source / 源码运行
    ai-audit-gui               # run installed app / 安装后运行
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from gui.main_window import main

if __name__ == "__main__":
    main()
