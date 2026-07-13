from app.platform_core.market_data.normalizer import market_data_normalizer
from app.platform_core.market_data.readiness import market_data_readiness_gate
from app.platform_core.market_data.registry import market_data_registry
from app.platform_core.market_data.snapshot_service import market_data_snapshot_service
from app.platform_core.market_data.validation import market_data_quality_validator

class MarketDataFoundationService:
    def symbols(self):
        return {"ready": True, "symbols": market_data_registry.seed_defaults()}

    def symbol(self, symbol: str):
        normalized = market_data_normalizer.normalize_symbol(symbol)
        return {"ready": True, "symbol": market_data_registry.get_symbol(normalized), "normalized": normalized}

    def samples(self, symbol: str = "BTCUSDT"):
        return {
            "ready": True,
            "ohlcv": market_data_snapshot_service.sample_ohlcv(symbol),
            "orderbook": market_data_snapshot_service.sample_orderbook(symbol),
            "trade": market_data_snapshot_service.sample_trade(symbol),
            "snapshot": market_data_snapshot_service.sample_snapshot(symbol),
            "execution_allowed": False,
        }

    def validate_sample(self, symbol: str = "BTCUSDT"):
        samples = self.samples(symbol)
        return {
            "ready": True,
            "ohlcv": market_data_quality_validator.validate_ohlcv(samples["ohlcv"]),
            "orderbook": market_data_quality_validator.validate_orderbook(samples["orderbook"]),
            "trade": market_data_quality_validator.validate_trade(samples["trade"]),
        }

    def readiness(self):
        return market_data_readiness_gate.run()

market_data_foundation_service = MarketDataFoundationService()
