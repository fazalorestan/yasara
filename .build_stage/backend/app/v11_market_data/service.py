from app.v11_market_data.engine import MarketDataEngineV11
from app.v11_market_data.models import SubscriptionRequestV11


class MarketDataServiceV11:
    def __init__(self):
        self.engine = MarketDataEngineV11()

    def bootstrap_demo(self):
        self.engine.subscribe(SubscriptionRequestV11(exchange="binance", symbols=["BTCUSDT", "ETHUSDT"]))
        self.engine.subscribe(SubscriptionRequestV11(exchange="bitunix", symbols=["BTC-USDT"]))
        self.engine.subscribe(SubscriptionRequestV11(exchange="toobit", symbols=["SOL_USDT"]))
        self.engine.ingest_synthetic_ticker("binance", "BTCUSDT", 50000)
        self.engine.ingest_synthetic_ticker("binance", "ETHUSDT", 3000)
        self.engine.ingest_synthetic_ticker("bitunix", "BTC-USDT", 50010)
        self.engine.ingest_synthetic_ticker("toobit", "SOL_USDT", 150)
        return self.engine.status()
