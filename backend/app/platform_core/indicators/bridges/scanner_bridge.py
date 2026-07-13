class IndicatorScannerBridge:
    def to_scanner_item(self, symbol: str, runtime_output: dict):
        signals = runtime_output.get("signals", [])
        signal = signals[0] if signals else {}
        return {
            "ready": True,
            "symbol": symbol,
            "indicator": "yasara",
            "direction": signal.get("direction", "WAIT"),
            "score": signal.get("confidence", 0),
            "watchlist_ready": True,
            "mode": "analysis_only",
        }

indicator_scanner_bridge = IndicatorScannerBridge()
