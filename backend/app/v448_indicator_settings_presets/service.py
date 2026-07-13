from app.platform_core.indicators.settings.overrides import yasara_user_settings_override_service
from app.platform_core.indicators.settings.presets import yasara_preset_registry
from app.platform_core.indicators.settings.validation import yasara_settings_validator
from app.platform_core.indicators.settings.versioning import yasara_preset_version_registry
from app.v448_indicator_settings_presets.models import IndicatorSettingsPresetsSummaryV448

class IndicatorSettingsPresetsFacadeV448:
    def summary(self):
        return IndicatorSettingsPresetsSummaryV448()

    def presets(self):
        return {"ready": True, "presets": yasara_preset_registry.seed_defaults()}

    def preset(self, name: str = "default"):
        return {"ready": True, "preset": yasara_preset_registry.get(name)}

    def validate(self, settings: dict | None = None):
        result = yasara_settings_validator.validate(settings or yasara_preset_registry.get("default")["settings"])
        return {"ready": result.valid, "validation": result.__dict__}

    def apply_override(self, preset: str = "default", overrides: dict | None = None):
        return yasara_user_settings_override_service.apply_override(preset, overrides)

    def versions(self):
        return yasara_preset_version_registry.versions()
