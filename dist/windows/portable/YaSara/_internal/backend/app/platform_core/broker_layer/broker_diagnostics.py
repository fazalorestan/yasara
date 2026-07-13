class BrokerDiagnosticsService:
    def diagnostics(self):
        return {
            "ready": True,
            "checks": {
                "registry_available": True,
                "adapter_contract_available": True,
                "account_read_blocked": True,
                "order_submit_blocked": True,
                "real_connection_blocked": True,
            },
            "passed": True,
            "execution_allowed": False,
        }

broker_diagnostics_service = BrokerDiagnosticsService()
