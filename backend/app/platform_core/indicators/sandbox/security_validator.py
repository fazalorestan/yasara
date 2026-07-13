from app.platform_core.indicators.sandbox.models import IndicatorSandboxPolicy, IndicatorValidationResult

class IndicatorSecurityPolicyValidator:
    def policy(self):
        return IndicatorSandboxPolicy().__dict__

    def validate(self, requested: dict):
        errors = []
        if requested.get("allow_network") is True:
            errors.append("network_access_not_allowed")
        if requested.get("allow_file_write") is True:
            errors.append("file_write_not_allowed")
        if requested.get("allow_live_execution") is True:
            errors.append("live_execution_not_allowed")
        if requested.get("allow_exchange_orders") is True:
            errors.append("exchange_orders_not_allowed")
        return IndicatorValidationResult(valid=len(errors) == 0, errors=errors).__dict__

indicator_security_policy_validator = IndicatorSecurityPolicyValidator()
