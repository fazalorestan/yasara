from app.platform_core.kernel.event_bus import PlatformEvent, event_bus

class IndicatorEventPublisher:
    def publish_signal(self, runtime_output: dict):
        signals = runtime_output.get("signals", [])
        signal = signals[0] if signals else {}
        event = PlatformEvent(
            name="IndicatorSignalGenerated",
            source="yasara_indicator",
            payload={
                "indicator": "yasara",
                "direction": signal.get("direction", "WAIT"),
                "confidence": signal.get("confidence", 0),
                "execution_allowed": False,
            },
        )
        event_bus.publish(event)
        return {"ready": True, "event": event.__dict__, "mode": "analysis_only"}

indicator_event_publisher = IndicatorEventPublisher()
