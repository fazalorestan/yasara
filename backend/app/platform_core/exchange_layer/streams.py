class ExchangeStreamContractService:
    def stream_contract(self):
        return {
            "ready": True,
            "streams": ["ticker", "orderbook", "trades", "candles"],
            "mode": "contract_only",
            "websocket_live": False,
            "real_connection": False,
            "execution_allowed": False,
        }

    def subscribe_preview(self, symbol: str = "BTCUSDT", stream: str = "ticker"):
        return {
            "ready": True,
            "symbol": symbol,
            "stream": stream,
            "subscribed": False,
            "dry_run": True,
            "real_connection": False,
            "execution_allowed": False,
        }

exchange_stream_contract_service = ExchangeStreamContractService()
