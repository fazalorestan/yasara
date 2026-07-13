class ScannerWatchlistService:
    def default_watchlist(self):
        return {"ready": True, "name": "default_crypto", "symbols": ["BTCUSDT", "ETHUSDT", "BNBUSDT", "SOLUSDT"], "market_type": "crypto", "enabled": True}
scanner_watchlist_service = ScannerWatchlistService()
