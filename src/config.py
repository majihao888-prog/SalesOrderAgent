from pathlib import Path
import json

# ==========================================================
# Project Paths
# ==========================================================

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


def ensure_directories() -> None:
    """
    Create all required directories.
    """

    directories = [
        INBOX_DIR,
        OUTPUT_DIR,
        ARCHIVE_DIR,
        FAILED_DIR,
        LOG_DIR,
        TEMP_DIR,
        DATA_DIR,
        CONFIG_DIR,
    ]

    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)


def ensure_settings_file() -> None:
    """
    Create a default settings file if it does not already exist.
    """

    ensure_directories()

    if not SETTINGS_FILE.exists():
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump({}, f, ensure_ascii=False, indent=2)
            f.write("\n")


def load_settings() -> dict:
    """
    Load project settings.
    """

    if not SETTINGS_FILE.exists():
        ensure_settings_file()
        return {}

    with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


ensure_settings_file()


if __name__ == "__main__":
    print("Project directories and settings file initialized.")