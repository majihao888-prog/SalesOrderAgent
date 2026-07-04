"""
app_config.py
Project configuration
"""

from __future__ import annotations

import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INBOX_DIR = PROJECT_ROOT / "inbox"
OUTPUT_DIR = PROJECT_ROOT / "output"
ARCHIVE_DIR = PROJECT_ROOT / "archive"
FAILED_DIR = PROJECT_ROOT / "failed"
LOG_DIR = PROJECT_ROOT / "logs"
TEMP_DIR = PROJECT_ROOT / "temp"
DATA_DIR = PROJECT_ROOT / "data"

CONFIG_DIR = PROJECT_ROOT / "config"

SETTINGS_FILE = CONFIG_DIR / "settings.json"

_REQUIRED_DIRS = [
    INBOX_DIR,
    OUTPUT_DIR,
    ARCHIVE_DIR,
    FAILED_DIR,
    LOG_DIR,
    TEMP_DIR,
    DATA_DIR,
]


def ensure_directories() -> None:
    for d in _REQUIRED_DIRS:
        d.mkdir(parents=True, exist_ok=True)


_DEFAULT_SETTINGS = {
    "project_name": "SalesOrderAgent",
    "version": "0.1.0",
    "log_level": "INFO",
}


def save_settings(settings: dict) -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4, ensure_ascii=False)


def load_settings() -> dict:
    if not SETTINGS_FILE.exists():
        save_settings(_DEFAULT_SETTINGS)

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


ensure_directories()

SETTINGS = load_settings()