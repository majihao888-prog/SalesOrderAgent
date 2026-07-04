"""
utils.py
Common utility functions
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from shutil import copy2, move

from app_config import INBOX_DIR


def now() -> datetime:
    """Return current datetime."""
    return datetime.now()


def timestamp() -> str:
    """Return formatted timestamp."""
    return now().strftime("%Y-%m-%d %H:%M:%S")


def find_pdf_files(directory: Path = INBOX_DIR) -> list[Path]:
    """Find all PDF files."""
    if not directory.exists():
        return []

    return sorted(directory.glob("*.pdf"))


def ensure_dir(directory: Path) -> None:
    """Create directory if missing."""
    directory.mkdir(parents=True, exist_ok=True)


def move_file(src: Path, dst: Path) -> None:
    """Move file."""
    ensure_dir(dst.parent)
    move(str(src), str(dst))


def copy_file(src: Path, dst: Path) -> None:
    """Copy file."""
    ensure_dir(dst.parent)
    copy2(src, dst)


def safe_filename(name: str) -> str:
    """Remove invalid filename characters."""
    invalid = '<>:"/\\|?*'

    for ch in invalid:
        name = name.replace(ch, "_")

    return name.strip()


def file_size(file: Path) -> float:
    """Return file size in MB."""
    return round(file.stat().st_size / 1024 / 1024, 2)


def file_time(file: Path) -> str:
    """Return last modified time."""
    return datetime.fromtimestamp(
        file.stat().st_mtime
    ).strftime("%Y-%m-%d %H:%M:%S")