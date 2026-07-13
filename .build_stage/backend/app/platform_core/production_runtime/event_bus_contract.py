class RuntimeEventBusContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "runtime_event_bus_contract",
            "events": ["runtime_started", "runtime_stopped", "runtime_restarted", "dashboard_refreshed"],
            "publish_enabled": True,
            "subscribe_enabled": True,
            "external_broker_required": False,
            "real_execution_enabled": False,
        }

runtime_event_bus_contract_service = RuntimeEventBusContractService()
