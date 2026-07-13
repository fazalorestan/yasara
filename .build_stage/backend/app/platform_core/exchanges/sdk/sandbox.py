class ExchangeConnectorSandboxContract:
    def policy(self):
        return {
            "ready": True,
            "network_allowed": False,
            "file_write_allowed": False,
            "live_orders_allowed": False,
            "secrets_access": "restricted",
            "crash_isolation": True,
            "kernel_protected": True,
            "mode": "sandbox_contract_only",
        }

exchange_connector_sandbox_contract = ExchangeConnectorSandboxContract()
