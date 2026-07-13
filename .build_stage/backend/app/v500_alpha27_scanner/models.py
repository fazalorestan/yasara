from pydantic import BaseModel
class ScannerSummaryV500Alpha27(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_27_scanner_foundation"
    scope: str = "scanner_contracts"
    live_scanning_enabled: bool = False
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
