from pathlib import Path

# Root of backend project
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ROOT = PROJECT_ROOT

# Output directories
BACKUP_DIR = PROJECT_ROOT / "doctor_backups"
REPORT_DIR = PROJECT_ROOT / "doctor_reports"

# Scan configuration
SCAN_EXTENSIONS = {
    ".py",
}

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    "doctor_backups",
    "doctor_reports",
    "runtime_reports",
    "node_modules",
    "dist",
    "build",
}

IGNORE_FILES = {
    "doctor_report.json",
}
