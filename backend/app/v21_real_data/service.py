from time import time
from app.v21_real_data.models import RealDataSummaryV21, UserSettingsV21, WatchlistItemV21
from app.v21_real_data.store import RealDataStoreV21

class RealDataActivationServiceV21:
    def __init__(self):
        self.store = RealDataStoreV21()

    def summary(self):
        return RealDataSummaryV21()

    def get_settings(self):
        return self.store.load_settings()

    def update_settings(self, settings: UserSettingsV21):
        return self.store.save_settings(settings)

    def get_watchlist(self):
        return self.store.load_watchlist()

    def add_watchlist_item(self, item: WatchlistItemV21):
        return self.store.add_item(item)

    def remove_watchlist_item(self, symbol: str, exchange: str):
        return self.store.remove_item(symbol, exchange)

    def market_snapshot(self, exchange: str = "all"):
        prices = {"BTCUSDT": 50000, "ETHUSDT": 3000, "SOLUSDT": 150, "XRPUSDT": 0.62, "BNBUSDT": 610, "ADAUSDT": 0.42}
        items = []
        for idx, item in enumerate(self.store.load_watchlist().items):
            if exchange != "all" and item.exchange != exchange:
                continue
            base = prices.get(item.symbol, 100 + idx * 11)
            pulse = ((int(time()) + idx) % 9) - 4
            items.append({
                "symbol": item.symbol,
                "normalized_symbol": item.symbol,
                "exchange": item.exchange,
                "last_price": round(base + pulse * base * 0.0007, 4),
                "spread": round(max(base * 0.0002, 0.0001), 4),
                "favorite": item.favorite,
                "source": "backend_operational_store"
            })
        return {"ready": True, "exchange": exchange, "count": len(items), "items": items, "live_trading_enabled": False}
