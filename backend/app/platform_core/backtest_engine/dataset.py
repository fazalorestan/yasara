from app.platform_core.clock import utc_now_iso

class HistoricalDatasetContract:
    def sample(self):
        return {
            "ready": True,
            "symbol": "BTCUSDT",
            "timeframe": "1h",
            "candles": [
                {"timestamp": utc_now_iso(), "open": 100.0, "high": 105.0, "low": 99.0, "close": 104.0, "volume": 1000.0},
                {"timestamp": utc_now_iso(), "open": 104.0, "high": 108.0, "low": 103.0, "close": 107.0, "volume": 1200.0},
                {"timestamp": utc_now_iso(), "open": 107.0, "high": 109.0, "low": 101.0, "close": 102.0, "volume": 1400.0},
            ],
            "real_market_data": False,
        }

historical_dataset_contract = HistoricalDatasetContract()
