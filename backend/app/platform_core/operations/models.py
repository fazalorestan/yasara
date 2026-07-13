from dataclasses import dataclass, field

@dataclass
class OperationalCheck:
    name: str
    ready: bool
    detail: str = ""
    severity: str = "info"

@dataclass
class OperationalReport:
    ready: bool
    checks: list[OperationalCheck] = field(default_factory=list)
    status: str = "operational"

    def to_dict(self):
        return {"ready": self.ready, "status": self.status, "checks": [c.__dict__ for c in self.checks]}
