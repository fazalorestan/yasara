from pydantic import BaseModel
class WindowsSpecOutputFixSummaryV52Alpha(BaseModel):
    ready: bool=True
    phase: str='v5_2_alpha_package_c'
    build_id: str='2026.52.C.001'
    pyinstaller_invocation_fixed: bool=True
    spec_file_ready: bool=True
    standard_output_ready: bool=True
    standard_output: str='dist/windows/portable/YaSara/YaSara.exe'
    signal_only_default: bool=True
    auto_trading_enabled: bool=False
    real_execution_enabled: bool=False
    real_broker_connection_enabled: bool=False
    test_pack_size: int=90
