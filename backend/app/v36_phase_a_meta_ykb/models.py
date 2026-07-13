from pydantic import BaseModel, Field
from typing import Literal


class PhaseAMetaSummaryV36(BaseModel):
    ready: bool = True
    phase: str = "v3_6_phase_a_meta_infrastructure_ykb_foundation"
    product_progress_percent: int = 80
    remaining_to_professional_product_percent: int = 20
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "meta_infrastructure_only_live_trading_disabled"


class YKBEntryV36(BaseModel):
    id: str
    type: str = "note"
    title: str
    scope: Literal["shared", "personal_only", "commercial_only"] = "shared"
    source: str = "manual"
    tags: list[str] = Field(default_factory=list)
    content: str
    created_at: str = "auto"


class TechnicalDebtItemV36(BaseModel):
    id: str
    type: str = "Temporary"
    description: str
    status: str = "open"
    priority: str = "medium"
