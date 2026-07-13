from app.platform_core.exchanges.sdk.capability_negotiation import connector_capability_negotiator
from app.platform_core.exchanges.sdk.events import exchange_connector_event_publisher
from app.platform_core.exchanges.sdk.health_watchdog import exchange_connector_health_watchdog
from app.platform_core.exchanges.sdk.lifecycle import exchange_connector_lifecycle
from app.platform_core.exchanges.sdk.manager import exchange_connector_manager
from app.platform_core.exchanges.sdk.readiness import exchange_sdk_readiness_gate
from app.platform_core.exchanges.sdk.sandbox import exchange_connector_sandbox_contract

class ExchangeSDKLifecycleService:
    def lifecycle(self):
        return {"ready": True, "states": exchange_connector_lifecycle.states()}

    def register(self, exchange_id: str = "binance"):
        return exchange_connector_manager.register_connector(exchange_id)

    def enable(self, exchange_id: str = "binance"):
        return exchange_connector_manager.enable_connector(exchange_id)

    def connectors(self):
        return {"ready": True, "connectors": exchange_connector_manager.list_connectors()}

    def health(self):
        return exchange_connector_health_watchdog.snapshot()

    def negotiate(self, exchange_id: str = "binance"):
        return connector_capability_negotiator.negotiate(exchange_id)

    def sandbox(self):
        return exchange_connector_sandbox_contract.policy()

    def events(self):
        return {"ready": True, "events": exchange_connector_event_publisher.supported_events()}

    def readiness(self):
        return exchange_sdk_readiness_gate.run()

exchange_sdk_lifecycle_service = ExchangeSDKLifecycleService()
