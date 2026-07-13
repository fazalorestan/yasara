from app.platform_core.indicators.sandbox.models import IndicatorValidationResult

class IndicatorRuntimeOutputValidator:
    required = ["indicator", "version", "overlays", "signals", "mode"]

    def validate(self, output: dict):
        errors = [f"missing_{k}" for k in self.required if k not in output]
        if output.get("mode") != "analysis_only":
            errors.append("runtime_mode_must_be_analysis_only")
        for signal in output.get("signals", []):
            if signal.get("execution_allowed") is not False:
                errors.append("signal_execution_must_be_false")
        return IndicatorValidationResult(valid=len(errors) == 0, errors=errors).__dict__

indicator_runtime_output_validator = IndicatorRuntimeOutputValidator()
