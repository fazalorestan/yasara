class ExchangeConnectorContract:
    required_methods = [
        "connect",
        "disconnect",
        "status",
        "symbols",
        "ohlcv",
        "orderbook",
        "trades",
        "ticker",
        "ping",
        "metadata",
    ]

    def contract(self):
        return {
            "ready": True,
            "required_methods": self.required_methods,
            "real_connection_enabled": False,
            "execution_allowed": False,
            "mode": "connector_contract_only",
        }

exchange_connector_contract = ExchangeConnectorContract()
