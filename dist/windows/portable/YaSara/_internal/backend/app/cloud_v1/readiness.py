from pydantic import BaseModel, Field

class CloudReadinessReportV1(BaseModel):
    ready: bool
    modules: list[str] = Field(default_factory=list)
    warnings: list[str] = Field(default_factory=list)

class CloudReadinessBuilderV1:
    def build(self) -> CloudReadinessReportV1:
        return CloudReadinessReportV1(
            ready=True,
            modules=["auth", "workspace", "api_tokens", "backup", "sync", "notifications", "quota", "license"],
            warnings=["Cloud providers are scaffolds until production credentials are configured."]
        )
