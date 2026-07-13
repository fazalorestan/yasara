from pydantic import BaseModel
class NativeWindowsLauncherSummaryV52Alpha(BaseModel):
    ready: bool=True
    phase: str='v5_2_alpha_package_d'
    build_id: str='2026.52.D.001'
    native_launcher: bool=True
    dashboard_bootstrap: bool=True
    runtime_report: bool=True
    signal_only_default: bool=True
    auto_trading_enabled: bool=False
    test_pack_size: int=90
