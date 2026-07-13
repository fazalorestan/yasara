class BrokerCapabilityContract:
    def capabilities(self):
        return {"ready": True, "market_orders": True, "limit_orders": True, "stop_orders": False, "reduce_only": True, "position_query": True, "wallet_query": True, "live_execution": False, "paper_execution": False, "auto_trading": False}
broker_capability_contract = BrokerCapabilityContract()
