from app.platform_core.indicators.sandbox.models import IndicatorValidationResult

class IndicatorManifestValidator:
    required = ["name", "version", "display_name", "capabilities"]

    def validate(self, manifest: dict):
        errors = [f"missing_{k}" for k in self.required if k not in manifest]
        if manifest.get("allow_live_execution") is True:
            errors.append("live_execution_not_allowed_for_indicator")
        return IndicatorValidationResult(valid=len(errors) == 0, errors=errors).__dict__

indicator_manifest_validator = IndicatorManifestValidator()
