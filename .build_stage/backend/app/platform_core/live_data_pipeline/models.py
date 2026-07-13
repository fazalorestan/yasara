from dataclasses import dataclass, field

@dataclass
class DataSourceProfile:
    source_id: str
    name: str
    mode: str = "simulated"
    enabled: bool = True

@dataclass
class DataSnapshot:
    source_id: str
    symbol: str
    price: float
    timestamp: int = 0
    metadata: dict = field(default_factory=dict)
