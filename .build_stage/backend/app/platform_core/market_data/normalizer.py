class MarketDataNormalizer:
    def normalize_symbol(self, symbol: str):
        return symbol.replace("/", "").replace("-", "").replace("_", "").upper()

    def normalize_timeframe(self, timeframe: str):
        aliases = {"15m": "15m", "15M": "15m", "1h": "1h", "1H": "1h", "4h": "4h", "4H": "4h", "1d": "1d", "1D": "1d"}
        return aliases.get(timeframe, timeframe.lower())

market_data_normalizer = MarketDataNormalizer()
