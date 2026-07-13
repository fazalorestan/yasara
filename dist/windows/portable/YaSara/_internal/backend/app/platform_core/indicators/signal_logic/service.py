from app.platform_core.indicators.signal_logic.composite import composite_signal_scorer
from app.platform_core.indicators.signal_logic.reasons import signal_reason_builder
from app.platform_core.indicators.signal_logic.resolver import signal_direction_resolver

class YaSaraRuntimeSignalLogicService:
    def evaluate(self, math_output: dict):
        composite = composite_signal_scorer.score(math_output)
        direction = signal_direction_resolver.resolve(composite)
        return {
            "ready": True,
            "indicator": "yasara",
            "direction": direction,
            "confidence": composite["score"],
            "reasons": signal_reason_builder.build(composite),
            "execution_allowed": False,
            "mode": "analysis_only",
        }

yasara_runtime_signal_logic_service = YaSaraRuntimeSignalLogicService()
