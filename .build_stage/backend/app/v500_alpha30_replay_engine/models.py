from pydantic import BaseModel
class ReplayEngineSummaryV500Alpha30(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_30_replay_engine_foundation"
    scope: str = "replay_engine_contracts"
    live_replay_enabled: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
