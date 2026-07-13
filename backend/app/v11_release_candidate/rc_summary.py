from pydantic import BaseModel, Field
from app.v11_release_candidate.integration_service import V11IntegrationService
from app.v11_release_candidate.release_manifest import V11ReleaseManifestBuilder


class V11ReleaseCandidateSummary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_11_integration_release_candidate"
    version: str = "1.1.0-rc1"
    modules_ready: int
    modules_total: int
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "release_candidate_live_trading_disabled"


class V11ReleaseCandidateSummaryBuilder:
    def build(self) -> V11ReleaseCandidateSummary:
        report = V11IntegrationService().report()
        manifest = V11ReleaseManifestBuilder().build()
        return V11ReleaseCandidateSummary(
            ready=report.ready and all(item.passed for item in manifest.checklist),
            modules_ready=sum(1 for module in report.modules if module.ready),
            modules_total=len(report.modules),
            capabilities=[
                "v11_module_integration",
                "release_candidate_manifest",
                "v11_readiness_report",
                "safety_freeze",
                "rc1_api",
            ],
        )
