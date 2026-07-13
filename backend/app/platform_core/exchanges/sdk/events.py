from app.platform_core.kernel.event_bus import PlatformEvent, event_bus

class ExchangeConnectorEventPublisher:
    def publish(self, name: str, exchange_id: str):
        event = PlatformEvent(
            name=name,
            source="exchange_connector_sdk",
            payload={"exchange_id": exchange_id, "execution_allowed": False},
        )
        event_bus.publish(event)
        return {"ready": True, "event": event.__dict__}

    def supported_events(self):
        return [
            "ConnectorLoaded",
            "ConnectorReady",
            "ConnectorDisconnected",
            "ConnectorRecovered",
            "ConnectorFailed",
            "HeartbeatReceived",
            "CapabilityUpdated",
        ]

exchange_connector_event_publisher = ExchangeConnectorEventPublisher()
