from app.platform_core.indicators.v5_expansion.models import GenericIndicatorPluginContract

class MultiIndicatorRegistryV5:
    def __init__(self):
        self._items = {}
    def register(self, item: GenericIndicatorPluginContract):
        self._items[item.name] = item
        return item
    def seed_defaults(self):
        if not self._items:
            self.register(GenericIndicatorPluginContract(
                name="yasara", version="v1.0", display_name="YaSara",
                overlay=True, enabled_by_default=True,
                capabilities=["runtime","chart_overlay","scanner","alerts","settings","readiness"],
                required_contracts=["manifest","runtime_adapter","chart_overlay_contract","engine_bridge"],
                metadata={"status":"ready_for_v5"}))
            self.register(GenericIndicatorPluginContract(
                name="future_indicator_template", version="v0.1", display_name="Future Indicator Template",
                overlay=True, enabled_by_default=False, capabilities=[],
                required_contracts=["manifest"], metadata={"status":"template_only"}))
        return {k:v.__dict__ for k,v in self._items.items()}
multi_indicator_registry_v5 = MultiIndicatorRegistryV5()
