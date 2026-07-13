from pydantic import BaseModel
from typing import Literal


class ProductionReadinessSummaryV48(BaseModel):
    ready: bool = True
    phase: str = "v4_8_production_readiness_release_guard_foundation"
    product_progress_percent: int = 99
    remaining_to_professional_product_percent: int = 1
    constitution_version: str = "YASARA_MASTER_REQUIREMENTS_FINAL_V4"
    constitution_compliant: bool = True
    safety: str = "release_guard_only_no_real_execution"


class BuildProfileRequestV48(BaseModel):
    build_type: Literal["personal", "commercial"] = "commercial"
