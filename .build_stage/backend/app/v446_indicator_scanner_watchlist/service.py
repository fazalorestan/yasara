from app.platform_core.indicators.scanner.service import indicator_scanner_contract_service
from app.v446_indicator_scanner_watchlist.models import IndicatorScannerWatchlistSummaryV446

class IndicatorScannerWatchlistFacadeV446:
    def summary(self):
        return IndicatorScannerWatchlistSummaryV446()

    def sample(self):
        bridge_outputs = [
            {"scanner": {"symbol": "BTCUSDT", "direction": "LONG", "score": 72}},
            {"scanner": {"symbol": "ETHUSDT", "direction": "WAIT", "score": 38}},
            {"scanner": {"symbol": "SOLUSDT", "direction": "SHORT", "score": 81}},
        ]
        return indicator_scanner_contract_service.build(bridge_outputs)

    def contract(self):
        return {
            "ready": True,
            "input": ["bridge_outputs"],
            "output": ["symbol", "indicator", "direction", "score", "grade", "badge"],
            "ranking": "score_desc",
            "execution_allowed": False,
            "mode": "analysis_only",
        }
