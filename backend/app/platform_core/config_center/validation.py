from app.platform_core.config_center.models import ConfigValidationResult

class ConfigValidator:
    def validate(self, values: dict):
        errors = []
        warnings = []

        if values.get("live_execution_enabled") is True:
            errors.append("live_execution_enabled_must_remain_false_in_current_phase")

        if "debug" not in values:
            warnings.append("debug_not_declared")

        return ConfigValidationResult(valid=len(errors) == 0, errors=errors, warnings=warnings)

config_validator = ConfigValidator()
