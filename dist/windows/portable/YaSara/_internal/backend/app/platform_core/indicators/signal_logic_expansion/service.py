from app.platform_core.indicators.signal_logic.service import yasara_runtime_signal_logic_service
from app.platform_core.indicators.signal_logic_expansion.confidence_policy import direction_confidence_policy
from app.platform_core.indicators.signal_logic_expansion.edge_cases import signal_edge_case_resolver
from app.platform_core.indicators.signal_logic_expansion.reason_codes import signal_reason_code_mapper
from app.platform_core.indicators.signal_logic_expansion.safety import runtime_signal_safety_report
from app.platform_core.indicators.signal_logic_expansion.score_bands import signal_score_band_resolver
from app.platform_core.indicators.signal_logic_expansion.validator import runtime_signal_validator

class RuntimeSignalExpansionService:
    def evaluate(self, math_output: dict):
        edge = signal_edge_case_resolver.resolve_math_output(math_output)
        if not edge["ready"]:
            signal = {
                "ready": True,
                "indicator": "yasara",
                "direction": "WAIT",
                "confidence": 0,
                "band": "no_trade",
                "reasons": [edge["reason"]],
                "reason_codes": ["EDGE_CASE"],
                "execution_allowed": False,
                "mode": "analysis_only",
            }
            return signal | {"validation": runtime_signal_validator.validate(signal)}

        base = yasara_runtime_signal_logic_service.evaluate(math_output)
        direction = direction_confidence_policy.normalize_direction(base["direction"], base["confidence"])
        signal = {
            **base,
            "direction": direction,
            "band": signal_score_band_resolver.band(base["confidence"]),
            "reason_codes": signal_reason_code_mapper.map(base.get("reasons", [])),
        }
        return signal | {"validation": runtime_signal_validator.validate(signal)}

    def safety(self):
        return runtime_signal_safety_report.report()

runtime_signal_expansion_service = RuntimeSignalExpansionService()
