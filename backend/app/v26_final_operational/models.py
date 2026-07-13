from pydantic import BaseModel


class FinalOperationalSummaryV26(BaseModel):
    ready: bool = True
    phase: str = "v2_6_final_operational_bridge"
    operational_progress_percent: int = 100
    remaining_to_full_operational_percent: int = 0
    safety: str = "final_operational_safe_mode_live_trading_disabled"


class ModuleStatusV26(BaseModel):
    name: str
    ready: bool
    progress_percent: int
    note: str
