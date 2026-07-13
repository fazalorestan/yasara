from app.platform_core.indicators.settings.models import YasaraIndicatorSettings, YasaraPreset

class YasaraPresetRegistry:
    def __init__(self):
        self._presets = {}

    def seed_defaults(self):
        if not self._presets:
            self._presets["default"] = YasaraPreset(
                name="default",
                description="Balanced default YaSara indicator settings",
                settings=YasaraIndicatorSettings().__dict__,
            )
            self._presets["scalping"] = YasaraPreset(
                name="scalping",
                description="Faster settings for short timeframes",
                settings=YasaraIndicatorSettings(ema_fast=9, ema_mid=21, ema_slow=100, min_score=65, mode="scalping").__dict__,
            )
            self._presets["swing"] = YasaraPreset(
                name="swing",
                description="Balanced swing trading settings",
                settings=YasaraIndicatorSettings(ema_fast=21, ema_mid=55, ema_slow=200, min_score=60, mode="swing").__dict__,
            )
            self._presets["conservative"] = YasaraPreset(
                name="conservative",
                description="Higher confirmation threshold",
                settings=YasaraIndicatorSettings(ema_fast=21, ema_mid=55, ema_slow=200, min_score=75, mode="conservative").__dict__,
            )
        return {k: v.__dict__ for k, v in self._presets.items()}

    def get(self, name: str):
        self.seed_defaults()
        item = self._presets.get(name)
        return item.__dict__ if item else None

yasara_preset_registry = YasaraPresetRegistry()
