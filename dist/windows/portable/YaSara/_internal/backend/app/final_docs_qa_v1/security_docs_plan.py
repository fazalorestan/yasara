from pydantic import BaseModel, Field

class SecurityDocControlV1(BaseModel):
    key: str
    description: str

class SecurityDocsPlanV1(BaseModel):
    controls: list[SecurityDocControlV1] = Field(default_factory=list)

class SecurityDocsPlanBuilderV1:
    def build(self) -> SecurityDocsPlanV1:
        return SecurityDocsPlanV1(controls=[
            SecurityDocControlV1(key="no_embedded_secrets", description="No API keys in source"),
            SecurityDocControlV1(key="dry_run_default", description="Private trading is dry-run by default"),
            SecurityDocControlV1(key="telemetry_off", description="Telemetry disabled by default"),
            SecurityDocControlV1(key="safe_cleanup", description="Cleanup scripts avoid source deletion"),
        ])
