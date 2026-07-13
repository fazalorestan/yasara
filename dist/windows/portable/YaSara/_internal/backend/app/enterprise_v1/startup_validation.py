from pydantic import BaseModel, Field
from app.enterprise_v1.module_discovery import ModuleDiscoveryV1

class StartupValidationReportV1(BaseModel):
    valid: bool
    modules_found: list[str] = Field(default_factory=list)

class StartupValidatorV1:
    def validate(self) -> StartupValidationReportV1:
        modules = ModuleDiscoveryV1().discover_static()
        names = [m.name for m in modules]
        return StartupValidationReportV1(valid="enterprise_v1" in names, modules_found=names)
