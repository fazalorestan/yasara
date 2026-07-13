from pydantic import BaseModel, Field
from typing import Literal


class PhaseAGuardrailsSummaryV361(BaseModel):
    ready: bool = True
    phase: str = "v3_6_1_phase_a_guardrails_ykb_search_registry_validation"
    product_progress_percent: int = 82
    remaining_to_professional_product_percent: int = 18
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "guardrails_only_live_trading_disabled"


class FeatureValidationRequestV361(BaseModel):
    feature_key: str
    dependencies: list[str] = Field(default_factory=list)
    scope: Literal["shared", "personal_only", "commercial_only"] = "shared"


class YKBSearchRequestV361(BaseModel):
    query: str = ""
    tags: list[str] = Field(default_factory=list)
    entry_type: str | None = None
    limit: int = 20
