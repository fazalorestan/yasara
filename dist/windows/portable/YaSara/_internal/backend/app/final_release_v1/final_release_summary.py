from pydantic import BaseModel, Field
from app.final_release_v1.final_manifest import FinalReleaseManifestBuilderV1
from app.final_release_v1.final_qa_gate import FinalQAGateBuilderV1
from app.final_release_v1.final_security_summary import FinalSecuritySummaryBuilderV1

class FinalReleaseSummaryV1(BaseModel):
    ready: bool
    version: str
    edition: str
    checks: list[str] = Field(default_factory=list)

class FinalReleaseSummaryBuilderV1:
    def build(self) -> FinalReleaseSummaryV1:
        manifest = FinalReleaseManifestBuilderV1().build()
        qa = FinalQAGateBuilderV1().build()
        security = FinalSecuritySummaryBuilderV1().build()
        return FinalReleaseSummaryV1(
            ready=qa.passed and security.passed,
            version=manifest.version,
            edition=manifest.edition,
            checks=["qa_gate", "security_summary", "release_manifest"],
        )
