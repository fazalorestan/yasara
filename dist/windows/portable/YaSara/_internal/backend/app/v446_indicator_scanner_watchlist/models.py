from pydantic import BaseModel

class IndicatorScannerWatchlistSummaryV446(BaseModel):
    ready: bool = True
    phase: str = "v4_46_yasara_indicator_scanner_watchlist_contract"
    scope: str = "indicator_scanner_watchlist"
    indicator_name: str = "yasara"
    no_new_trading_features: bool = True
    live_execution_enabled: bool = False
    backward_compatible: bool = True
    safety: str = "scanner_watchlist_contract_only_no_real_execution"
