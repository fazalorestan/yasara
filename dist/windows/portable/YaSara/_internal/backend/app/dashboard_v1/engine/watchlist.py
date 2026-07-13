from app.dashboard_v1.domain.models import DashboardWatchlistItem

class DashboardWatchlistEngineV1:
    def build_default(self) -> list[DashboardWatchlistItem]:
        return [
            DashboardWatchlistItem(symbol="BTC/USDT", price=0, change_percent=0, confidence=0),
            DashboardWatchlistItem(symbol="ETH/USDT", price=0, change_percent=0, confidence=0),
            DashboardWatchlistItem(symbol="BNB/USDT", price=0, change_percent=0, confidence=0),
        ]

    def enrich(self, prices: dict[str, float], confidences: dict[str, float] | None = None) -> list[DashboardWatchlistItem]:
        confidences = confidences or {}
        return [
            DashboardWatchlistItem(symbol=symbol, price=price, confidence=confidences.get(symbol, 0))
            for symbol, price in prices.items()
        ]
