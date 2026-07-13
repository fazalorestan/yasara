from app.platform_core.indicators.models import IndicatorManifest

class IndicatorRegistry:
    def __init__(self):
        self._items = {}

    def register(self, manifest: IndicatorManifest):
        self._items[manifest.name] = manifest
        return manifest

    def get(self, name: str):
        return self._items.get(name)

    def list(self):
        return {k: v.__dict__ for k, v in self._items.items()}

    def seed_defaults(self):
        if "yasara" not in self._items:
            self.register(IndicatorManifest(
                name="yasara",
                version="v1.0",
                enabled_by_default=True,
                overlay=True,
                capabilities=[
                    "ema_overlay", "smc_labels", "fvg_zones", "entry_sl_tp",
                    "dynamic_sl", "relative_strength", "confidence_score", "alerts_contract"
                ],
                metadata={"display_name": "YaSara", "source": "pine_script_adapted", "update_strategy": "independent_script_slot"},
            ))
        return self.list()

indicator_registry = IndicatorRegistry()
