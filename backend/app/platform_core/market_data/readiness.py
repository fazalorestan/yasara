from app.platform_core.market_data.registry import market_data_registry
from app.platform_core.market_data.snapshot_service import market_data_snapshot_service
from app.platform_core.market_data.validation import market_data_quality_validator

class MarketDataReadinessGate:
    def run(self):
        registry = market_data_registry.seed_defaults()
        candle = market_data_snapshot_service.sample_ohlcv()
        book = market_data_snapshot_service.sample_orderbook()
        trade = market_data_snapshot_service.sample_trade()
        checks = {
            "registry_ready": len(registry) >= 4,
            "ohlcv_valid": market_data_quality_validator.validate_ohlcv(candle)["valid"],
            "orderbook_valid": market_data_quality_validator.validate_orderbook(book)["valid"],
            "trade_valid": market_data_quality_validator.validate_trade(trade)["valid"],
            "real_exchange_connection": False,
            "execution_allowed": False,
        }
        ready = checks["registry_ready"] and checks["ohlcv_valid"] and checks["orderbook_valid"] and checks["trade_valid"]
        return {"ready": ready, "checks": checks, "mode": "market_data_foundation_only"}

market_data_readiness_gate = MarketDataReadinessGate()
