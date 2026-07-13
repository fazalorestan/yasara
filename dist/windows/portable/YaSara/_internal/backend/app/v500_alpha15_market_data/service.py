from app.platform_core.market_data.service import market_data_foundation_service
from app.v500_alpha15_market_data.models import MarketDataSummaryV500Alpha15

class MarketDataFacadeV500Alpha15:
    def summary(self):
        return MarketDataSummaryV500Alpha15()

    def symbols(self):
        return market_data_foundation_service.symbols()

    def symbol(self, symbol: str = "BTCUSDT"):
        return market_data_foundation_service.symbol(symbol)

    def samples(self, symbol: str = "BTCUSDT"):
        return market_data_foundation_service.samples(symbol)

    def validate_sample(self, symbol: str = "BTCUSDT"):
        return market_data_foundation_service.validate_sample(symbol)

    def readiness(self):
        return market_data_foundation_service.readiness()

    def contract(self):
        return {
            "ready": True,
            "contracts": ["symbol", "ohlcv", "orderbook", "trade_tick", "market_snapshot", "quality_validator"],
            "real_exchange_connection": False,
            "execution_allowed": False,
            "mode": "foundation_only",
        }
