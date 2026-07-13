from dataclasses import dataclass, field
from typing import Any

@dataclass
class ReleaseCheck:
    name: str
    passed: bool
    severity: str = "info"
    detail: str = ""
    data: dict[str, Any] = field(default_factory=dict)

@dataclass
class ReleaseReadinessReport:
    ready: bool
    score: float
    checks: list[ReleaseCheck]
    blockers: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "ready": self.ready,
            "score": self.score,
            "checks": [c.__dict__ for c in self.checks],
            "blockers": self.blockers,
            "warnings": self.warnings,
        }
