from dataclasses import dataclass, field
from typing import Any

@dataclass
class DiagnosticCheck:
    name: str
    ready: bool
    severity: str = "info"
    detail: str = ""
    data: dict[str, Any] = field(default_factory=dict)

@dataclass
class DiagnosticReport:
    ready: bool
    score: float
    checks: list[DiagnosticCheck]
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "ready": self.ready,
            "score": self.score,
            "checks": [c.__dict__ for c in self.checks],
            "warnings": self.warnings,
            "errors": self.errors,
        }
