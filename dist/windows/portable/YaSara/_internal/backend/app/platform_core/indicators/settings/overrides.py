from app.platform_core.indicators.settings.presets import yasara_preset_registry
from app.platform_core.indicators.settings.validation import yasara_settings_validator

class YasaraUserSettingsOverrideService:
    def apply_override(self, preset_name: str = "default", overrides: dict | None = None):
        preset = yasara_preset_registry.get(preset_name) or yasara_preset_registry.get("default")
        settings = dict(preset["settings"])
        settings.update(overrides or {})
        validation = yasara_settings_validator.validate(settings)
        return {
            "ready": validation.valid,
            "preset": preset_name,
            "settings": settings,
            "validation": validation.__dict__,
            "mode": "contract_only",
        }

yasara_user_settings_override_service = YasaraUserSettingsOverrideService()
