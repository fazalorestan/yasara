from dataclasses import dataclass, field

@dataclass
class IndicatorReadinessCheck:
    name: str
    ready: bool
    detail: str = ""

@dataclass
class IndicatorReadinessReport:
    ready: bool
    score: float
    checks: list[IndicatorReadinessCheck] = field(default_factory=list)
    blockers: list[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "ready": self.ready,
            "score": self.score,
            "checks": [c.__dict__ for c in self.checks],
            "blockers": self.blockers,
        }
