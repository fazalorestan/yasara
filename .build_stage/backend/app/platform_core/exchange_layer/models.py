from dataclasses import dataclass, field
@dataclass
class ExchangeProfile:
    exchange_id: str
    name: str
    mode: str = "sandbox"
    enabled: bool = True
@dataclass
class ExchangeCapability:
    exchange_id: str
    spot: bool = True
    futures: bool = False
    margin: bool = False
    websocket: bool = False
    metadata: dict = field(default_factory=dict)
