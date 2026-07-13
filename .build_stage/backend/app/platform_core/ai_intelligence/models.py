from dataclasses import dataclass, field

@dataclass
class AIProviderProfile:
    provider_id: str
    name: str
    mode: str = "simulated"
    enabled: bool = True

@dataclass
class AIRequestContext:
    request_id: str
    task: str
    metadata: dict = field(default_factory=dict)
