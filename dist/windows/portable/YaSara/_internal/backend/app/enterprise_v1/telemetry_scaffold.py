from pydantic import BaseModel, Field

class TelemetryEventV1(BaseModel):
    name: str
    properties: dict = Field(default_factory=dict)

class TelemetryScaffoldV1:
    def __init__(self, enabled: bool = False):
        self.enabled = enabled
        self.events: list[TelemetryEventV1] = []

    def track(self, event: TelemetryEventV1) -> bool:
        if not self.enabled:
            return False
        self.events.append(event)
        return True
