from pathlib import Path
from app.v11_operations.models import OperationsHealthCheckV11, OperationsHealthReportV11


class ProjectHealthCheckerV11:
    def __init__(self, root: Path | None = None):
        self.root = root or Path(__file__).resolve().parents[3]

    def check(self) -> OperationsHealthReportV11:
        required = [
            "backend/app",
            "backend/tests",
            "backend/scripts",
            "docs",
            "windows_runtime",
            "desktop_packaging",
            "release_automation",
            "FINAL_VERSION_FREEZE_MANIFEST.json",
            "YASARA_V1_FINAL_README.md",
        ]
        checks: list[OperationsHealthCheckV11] = []
        for rel in required:
            exists = (self.root / rel).exists()
            checks.append(OperationsHealthCheckV11(
                key=rel,
                passed=exists,
                message="ok" if exists else "missing",
            ))
        return OperationsHealthReportV11(
            ready=all(c.passed for c in checks),
            checks=checks,
        )
