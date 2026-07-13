from pydantic import BaseModel, Field

class InstallerValidationPlanV1(BaseModel):
    checks: list[str] = Field(default_factory=list)

class InstallerValidationPlannerV1:
    def build(self) -> InstallerValidationPlanV1:
        return InstallerValidationPlanV1(checks=[
            "installer_exists",
            "portable_exists",
            "start_backend_shortcut",
            "health_endpoint_ok",
            "uninstall_clean",
        ])
