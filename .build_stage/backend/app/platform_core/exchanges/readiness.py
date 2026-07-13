from app.platform_core.exchanges.capabilities import exchange_capability_matrix
from app.platform_core.exchanges.connector_contract import exchange_connector_contract
from app.platform_core.exchanges.health import exchange_health_monitor
from app.platform_core.exchanges.metadata import exchange_metadata_registry
from app.platform_core.exchanges.registry import exchange_registry

class ExchangeConnectorReadinessGate:
    def run(self):
        exchanges = exchange_registry.seed_defaults()
        capabilities = exchange_capability_matrix.seed_defaults()
        metadata = exchange_metadata_registry.seed_defaults()
        health = exchange_health_monitor.seed_defaults(list(exchanges.keys()))
        checks = {
            "registry_ready": len(exchanges) >= 18,
            "bitunix_registered": "bitunix" in exchanges,
            "toobit_registered": "toobit" in exchanges,
            "lbank_registered": "lbank" in exchanges,
            "capabilities_ready": len(capabilities) >= 18,
            "metadata_ready": len(metadata) >= 18,
            "health_ready": len(health) >= 18,
            "contract_ready": exchange_connector_contract.contract()["ready"],
            "real_connection_enabled": False,
            "execution_allowed": False,
        }
        ready = all(v is True for k, v in checks.items() if k not in ["real_connection_enabled", "execution_allowed"])
        return {"ready": ready, "checks": checks, "mode": "exchange_connector_framework_only"}

exchange_connector_readiness_gate = ExchangeConnectorReadinessGate()
