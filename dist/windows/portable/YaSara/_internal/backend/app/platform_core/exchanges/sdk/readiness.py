from app.platform_core.exchanges.sdk.base import BaseExchangeConnector
from app.platform_core.exchanges.sdk.capability_negotiation import connector_capability_negotiator
from app.platform_core.exchanges.sdk.events import exchange_connector_event_publisher
from app.platform_core.exchanges.sdk.health_watchdog import exchange_connector_health_watchdog
from app.platform_core.exchanges.sdk.lifecycle import exchange_connector_lifecycle
from app.platform_core.exchanges.sdk.manager import exchange_connector_manager
from app.platform_core.exchanges.sdk.sandbox import exchange_connector_sandbox_contract

class ExchangeSDKReadinessGate:
    def run(self):
        connector = BaseExchangeConnector("binance")
        registered = exchange_connector_manager.register_connector("binance")
        enabled = exchange_connector_manager.enable_connector("binance")
        heartbeat = exchange_connector_health_watchdog.heartbeat("binance")
        capability = connector_capability_negotiator.negotiate("binance", ["spot", "rest"])
        sandbox = exchange_connector_sandbox_contract.policy()
        event = exchange_connector_event_publisher.publish("ConnectorReady", "binance")
        checks = {
            "sdk_ready": connector.sdk_version == "1.0",
            "lifecycle_ready": "connected" in exchange_connector_lifecycle.states(),
            "manager_ready": registered["ready"] and enabled["ready"],
            "health_ready": heartbeat["ready"],
            "capability_ready": capability["ready"],
            "sandbox_ready": sandbox["ready"],
            "event_ready": event["ready"],
            "real_connection_enabled": False,
            "execution_allowed": False,
        }
        ready = all(v is True for k, v in checks.items() if k not in ["real_connection_enabled", "execution_allowed"])
        return {"ready": ready, "checks": checks, "mode": "exchange_sdk_lifecycle_only"}

exchange_sdk_readiness_gate = ExchangeSDKReadinessGate()
