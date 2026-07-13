from dataclasses import dataclass, field

@dataclass
class IndicatorValidationResult:
    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

@dataclass
class IndicatorSandboxPolicy:
    allow_network: bool = False
    allow_file_write: bool = False
    allow_live_execution: bool = False
    allow_exchange_orders: bool = False
    mode: str = "sandbox_contract_only"
