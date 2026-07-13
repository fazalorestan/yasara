from dataclasses import dataclass, field

@dataclass
class IndicatorReleaseManifest:
    indicator: str
    version: str
    status: str = "ready"
    compatible_with: list[str] = field(default_factory=list)
    contracts: list[str] = field(default_factory=list)

@dataclass
class IndicatorMigrationChecklist:
    items: list[str] = field(default_factory=list)
    complete: bool = True
