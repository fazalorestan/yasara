from app.platform_core.indicators.settings.models import SettingsValidationResult

class YasaraSettingsValidator:
    def validate(self, settings: dict):
        errors = []
        warnings = []

        if int(settings.get("ema_fast", 21)) >= int(settings.get("ema_mid", 55)):
            errors.append("ema_fast_must_be_less_than_ema_mid")
        if int(settings.get("ema_mid", 55)) >= int(settings.get("ema_slow", 200)):
            errors.append("ema_mid_must_be_less_than_ema_slow")
        if int(settings.get("min_score", 60)) < 30 or int(settings.get("min_score", 60)) > 95:
            errors.append("min_score_out_of_safe_range")
        if int(settings.get("rsi_len", 14)) < 5:
            warnings.append("rsi_len_is_very_short")

        return SettingsValidationResult(valid=len(errors) == 0, errors=errors, warnings=warnings)

yasara_settings_validator = YasaraSettingsValidator()
