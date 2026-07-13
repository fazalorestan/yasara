from pydantic import BaseModel, Field
from app.release_pro_v1.pro_manifest import ProfessionalManifestBuilderV1
from app.release_pro_v1.health_audit import HealthAuditBuilderV1
from app.release_pro_v1.final_qa import FinalQABuilderV1

class FinalProfessionalSummaryV1(BaseModel):
    ready: bool
    version: str
    modules: list[str] = Field(default_factory=list)
    tests_expected_note: str = ""

class FinalProfessionalSummaryBuilderV1:
    def build(self) -> FinalProfessionalSummaryV1:
        manifest = ProfessionalManifestBuilderV1().build()
        audit = HealthAuditBuilderV1().build()
        qa = FinalQABuilderV1().default()
        return FinalProfessionalSummaryV1(
            ready=audit.ready and qa.ready,
            version=manifest.version,
            modules=manifest.capabilities,
            tests_expected_note="Run python -m pytest tests before release.",
        )
