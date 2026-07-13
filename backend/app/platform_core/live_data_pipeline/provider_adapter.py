class LiveDataProviderAdapterContract:
    def adapter_contract(self):
        return {
            "ready": True,
            "adapter_mode": "contract_only",
            "required_methods": ["metadata", "fetch_snapshot", "health"],
            "real_provider_connection": False,
            "execution_allowed": False,
        }

    def simulated_snapshot(self):
        return {
            "ready": True,
            "source_id": "sim.exchange",
            "symbol": "BTCUSDT",
            "price": 50000.0,
            "timestamp": 0,
            "provider": "simulated",
            "real_connection": False,
        }

live_data_provider_adapter_contract = LiveDataProviderAdapterContract()
