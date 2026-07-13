from dataclasses import dataclass, field

@dataclass
class ReleaseGateCheck:
    name: str
    passed: bool
    detail: str = ""

@dataclass
class ReleaseGateReport:
    ready: bool
    milestone: str
    checks: list[ReleaseGateCheck] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "ready": self.ready,
            "milestone": self.milestone,
            "checks": [c.__dict__ for c in self.checks],
            "blockers": self.blockers,
        }
