from pydantic import BaseModel, Field

class CloudPhaseSummaryV1(BaseModel):
    phase: str = "cloud_phase_4"
    ready: bool = True
    modules: list[str] = Field(default_factory=list)

class CloudPhaseSummaryBuilderV1:
    def build(self) -> CloudPhaseSummaryV1:
        return CloudPhaseSummaryV1(modules=[
            "auth", "workspace", "api_tokens", "backup_manifest", "sync_conflict",
            "device_sync", "remote_notifications", "quota", "cloud_audit",
            "release_channel", "auto_update", "license", "cloud_api", "readiness"
        ])
