from pydantic import BaseModel, Field
from app.v11_final_release.service import FinalReleaseServiceV11


class V11Phase12Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_12_final_release_production_package"
    progress_percent: int = 100
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "v1_1_final_live_trading_disabled"


class V11Phase12SummaryBuilder:
    def build(self) -> V11Phase12Summary:
        summary = FinalReleaseServiceV11().summary()
        return V11Phase12Summary(
            ready=summary.ready and summary.progress_percent == 100,
            capabilities=[
                "version_freeze",
                "build_info",
                "final_manifest",
                "final_qa_script",
                "production_package_script",
                "checksum_generation",
                "release_notes",
                "final_release_api",
            ],
        )
