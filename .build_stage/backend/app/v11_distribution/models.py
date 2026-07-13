from pydantic import BaseModel, Field


class DistributionArtifactV11(BaseModel):
    name: str
    target: str
    path: str
    required: bool = True


class DistributionSummaryV11(BaseModel):
    ready: bool
    version: str = "1.1.0"
    progress_percent: int = 100
    windows_outputs: list[DistributionArtifactV11] = Field(default_factory=list)
    mobile_outputs: list[DistributionArtifactV11] = Field(default_factory=list)
    safety: str = "distribution_only_live_trading_disabled"
