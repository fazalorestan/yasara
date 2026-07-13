from datetime import datetime, timezone
from pydantic import BaseModel, Field

class ConsolidatedProjectManifestV1(BaseModel):
    product: str = "YaSara"
    edition: str = "Professional"
    version: str = "1.0.0-pro"
    sprint_range: str = "1-120"
    status: str = "consolidation_phase_a"
    total_confirmed_tests: int = 179
    modules: list[str] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ConsolidatedProjectManifestBuilderV1:
    def build(self) -> ConsolidatedProjectManifestV1:
        return ConsolidatedProjectManifestV1(
            modules=[
                "backend_core",
                "multi_exchange",
                "market_tools",
                "connectivity",
                "ai_trading",
                "desktop_ui_backend",
                "cloud_layer",
                "release_pro",
                "plugin_system",
                "build_pipeline",
            ]
        )
