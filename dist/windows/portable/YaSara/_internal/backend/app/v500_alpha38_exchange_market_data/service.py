from app.platform_core.exchange_layer.candles import exchange_candle_contract_service
from app.platform_core.exchange_layer.market_data_readiness import exchange_market_data_readiness_gate
from app.platform_core.exchange_layer.market_data_report import exchange_market_data_report_service
from app.platform_core.exchange_layer.market_data_safety import exchange_market_data_safety_service
from app.platform_core.exchange_layer.market_metadata import exchange_market_metadata_service
from app.platform_core.exchange_layer.orderbook import exchange_orderbook_snapshot_service
from app.platform_core.exchange_layer.symbols import exchange_symbol_registry_service
from app.platform_core.exchange_layer.ticker import exchange_ticker_snapshot_service
from app.v500_alpha38_exchange_market_data.models import ExchangeMarketDataSummaryV500Alpha38

class ExchangeMarketDataFacadeV500Alpha38:
    def summary(self): return ExchangeMarketDataSummaryV500Alpha38()
    def symbols(self): return exchange_symbol_registry_service.symbols()
    def normalize_symbol(self): return exchange_symbol_registry_service.normalize("btc/usdt")
    def metadata(self): return exchange_market_metadata_service.metadata()
    def ticker(self): return exchange_ticker_snapshot_service.ticker()
    def orderbook(self): return exchange_orderbook_snapshot_service.orderbook()
    def candles(self): return exchange_candle_contract_service.candles()
    def safety(self): return exchange_market_data_safety_service.policy()
    def validate_symbol(self): return exchange_market_data_safety_service.validate_symbol("BTCUSDT")
    def report(self): return exchange_market_data_report_service.report()
    def readiness(self): return exchange_market_data_readiness_gate.run()
    def contract(self): return {"ready": True, "exchange_layer": "package_b_market_data_symbols", "execution_allowed": False}

exchange_market_data_facade_v500_alpha38 = ExchangeMarketDataFacadeV500Alpha38()
