from pydantic import BaseModel
class InProcessBackendRunnerSummaryV52Alpha(BaseModel):
    ready: bool=True
    phase: str='v5_2_alpha_package_g'
    build_id: str='2026.52.G.001'
    backend_runner: str='in_process_thread'
    fixes_recursive_frozen_exe_launch: bool=True
    signal_only_default: bool=True
    auto_trading_enabled: bool=False
    test_pack_size: int=90
