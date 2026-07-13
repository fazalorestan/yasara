from pydantic import BaseModel
class APSchedulerDependencyGateSummaryV52Alpha(BaseModel):
    ready: bool=True
    phase: str='v5_2_alpha_package_m'
    build_id: str='2026.52.M.001'
    apscheduler_gate: bool=True
    legacy_j_test_fix: bool=True
    executable_validation: bool=True
    signal_only_default: bool=True
    auto_trading_enabled: bool=False
    test_pack_size: int=90
