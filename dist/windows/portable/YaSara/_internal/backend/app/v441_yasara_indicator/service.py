from app.platform_core.indicators.registry import indicator_registry
from app.platform_core.indicators.signal_adapter import yasara_signal_adapter
from app.platform_core.indicators.yasara_contract import yasara_indicator_contract
from app.v441_yasara_indicator.models import YaSaraIndicatorSummaryV441

class YaSaraIndicatorServiceV441:
    def summary(self):
        return YaSaraIndicatorSummaryV441()

    def registry(self):
        return {"ready": True, "indicators": indicator_registry.seed_defaults()}

    def contract(self):
        return {"ready": True, "contract": yasara_indicator_contract.overlay_contract()}

    def normalize_signal(self, raw: dict | None = None):
        return {"ready": True, "signal": yasara_signal_adapter.normalize(raw or {"direction": "WAIT", "score": 0})}

    def default_state(self):
        indicator_registry.seed_defaults()
        item = indicator_registry.get("yasara")
        return {"ready": True, "name": "yasara", "display_name": "YaSara", "enabled": bool(item.enabled_by_default), "overlay": True, "script_slot": "frontend/src/indicators/yasara/yasara-script.ts"}

