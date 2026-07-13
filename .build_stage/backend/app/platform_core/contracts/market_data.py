from app.platform_core.contracts.base import BaseContract

class MarketDataContract(BaseContract):
    contract_name = "market_data"

    def fetch(self, symbol: str, timeframe: str):
        raise NotImplementedError("Market data plugins must implement fetch(symbol, timeframe)")
