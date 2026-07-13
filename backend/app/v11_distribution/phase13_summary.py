from pydantic import BaseModel, Field
from app.v11_distribution.service import FinalDistributionServiceV11


class V11FinalDistributionSummary(BaseModel):
    ready: bool
    phase: str = "v1_1_final_windows_mobile_distribution"
    progress_percent: int = 100
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "final_distribution_no_live_trading"


class V11FinalDistributionSummaryBuilder:
    def build(self) -> V11FinalDistributionSummary:
        summary = FinalDistributionServiceV11().summary()
        return V11FinalDistributionSummary(
            ready=summary.ready and len(summary.windows_outputs) >= 3 and len(summary.mobile_outputs) >= 3,
            capabilities=[
                "windows_portable_output",
                "windows_final_zip",
                "windows_installer_scaffold",
                "mobile_pwa_output",
                "android_wrapper_guide",
                "mobile_api_config",
                "distribution_checksums",
            ],
        )
