from app.platform_core.exchange_layer.candles import exchange_candle_contract_service
from app.platform_core.exchange_layer.market_data_safety import exchange_market_data_safety_service
from app.platform_core.exchange_layer.market_metadata import exchange_market_metadata_service
from app.platform_core.exchange_layer.orderbook import exchange_orderbook_snapshot_service
from app.platform_core.exchange_layer.symbols import exchange_symbol_registry_service
from app.platform_core.exchange_layer.ticker import exchange_ticker_snapshot_service

class ExchangeMarketDataReportService:
    def report(self):
        symbol = "BTCUSDT"
        return {
            "ready": True,
            "symbols": exchange_symbol_registry_service.symbols(),
            "metadata": exchange_market_metadata_service.metadata(symbol),
            "ticker": exchange_ticker_snapshot_service.ticker(symbol),
            "orderbook": exchange_orderbook_snapshot_service.orderbook(symbol),
            "candles": exchange_candle_contract_service.candles(symbol),
            "safety": exchange_market_data_safety_service.policy(),
            "real_exchange_connection": False,
            "execution_allowed": False,
        }

exchange_market_data_report_service = ExchangeMarketDataReportService()
