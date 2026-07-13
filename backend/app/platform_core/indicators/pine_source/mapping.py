from app.platform_core.indicators.pine_source.models import PineRuntimeMapping

class PineToRuntimeMappingRegistry:
    def __init__(self):
        self._items: list[PineRuntimeMapping] = []

    def seed_defaults(self):
        if not self._items:
            mappings = [
                ("TREND", "overlays.moving_averages"),
                ("MACD", "panels.engine_scores"),
                ("RSI", "panels.engine_scores"),
                ("VOLUME", "panels.engine_scores"),
                ("ATR", "panels.risk_panel"),
                ("SMC", "overlays.smc_labels"),
                ("FVG", "overlays.fvg_zones"),
                ("RS vs BTC", "panels.ai_decision"),
                ("COMBINED SIGNAL", "signals.direction_confidence"),
                ("SL / TP", "overlays.entry_sl_tp"),
                ("ALERTS", "events.alert_contract"),
            ]
            self._items = [PineRuntimeMapping(pine_section=a, runtime_target=b) for a, b in mappings]
        return [m.__dict__ for m in self._items]

pine_to_runtime_mapping_registry = PineToRuntimeMappingRegistry()
