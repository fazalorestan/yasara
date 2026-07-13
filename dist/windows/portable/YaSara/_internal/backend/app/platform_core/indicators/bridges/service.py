from app.platform_core.indicators.bridges.ai_bridge import indicator_ai_bridge
from app.platform_core.indicators.bridges.confidence_bridge import indicator_confidence_bridge
from app.platform_core.indicators.bridges.event_publisher import indicator_event_publisher
from app.platform_core.indicators.bridges.risk_bridge import indicator_risk_bridge
from app.platform_core.indicators.bridges.scanner_bridge import indicator_scanner_bridge

class IndicatorEngineBridgeService:
    def bridge(self, symbol: str, runtime_output: dict):
        signal = runtime_output.get("signals", [{}])[0]
        confidence = signal.get("confidence", 0)
        return {
            "ready": True,
            "ai_decision": indicator_ai_bridge.to_ai_decision(runtime_output),
            "risk_panel": indicator_risk_bridge.to_risk_panel(runtime_output),
            "scanner": indicator_scanner_bridge.to_scanner_item(symbol, runtime_output),
            "confidence": {
                "score": indicator_confidence_bridge.normalize(confidence),
                "grade": indicator_confidence_bridge.grade(confidence),
            },
            "event": indicator_event_publisher.publish_signal(runtime_output),
            "execution_allowed": False,
            "mode": "analysis_only",
        }

indicator_engine_bridge_service = IndicatorEngineBridgeService()
