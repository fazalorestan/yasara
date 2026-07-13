from app.platform_core.indicators.scanner.ranking import indicator_ranking_service
from app.platform_core.indicators.scanner.watchlist_adapter import indicator_watchlist_adapter

class IndicatorScannerContractService:
    def build(self, bridge_outputs: list[dict]):
        items = [indicator_watchlist_adapter.from_bridge_output(item) for item in bridge_outputs]
        return {
            "ready": True,
            "indicator": "yasara",
            "items": indicator_ranking_service.rank(items),
            "count": len(items),
            "execution_allowed": False,
            "mode": "analysis_only",
        }

indicator_scanner_contract_service = IndicatorScannerContractService()
