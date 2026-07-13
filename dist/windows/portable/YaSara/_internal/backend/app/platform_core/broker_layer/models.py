from dataclasses import dataclass, field

@dataclass
class BrokerProfile:
    broker_id: str
    name: str
    mode: str = "paper"
    enabled: bool = True

@dataclass
class BrokerCapability:
    broker_id: str
    supports_market_orders: bool = False
    supports_limit_orders: bool = False
    supports_positions: bool = False
    supports_balances: bool = False
    metadata: dict = field(default_factory=dict)
