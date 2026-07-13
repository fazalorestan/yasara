from app.platform_core.indicators.runtime.models import (
    CandleInput,
    IndicatorOverlayOutput,
    IndicatorRuntimeInput,
    IndicatorRuntimeOutput,
    IndicatorSignalOutput,
)

class YaSaraIndicatorRuntimeAdapter:
    version = "v1.0"

    def _sma(self, values: list[float], length: int):
        if len(values) < length:
            return None
        return sum(values[-length:]) / length

    def run(self, runtime_input: IndicatorRuntimeInput):
        closes = [c.close for c in runtime_input.candles]
        overlays = []
        if closes:
            for name, length in [("SMA7", 7), ("SMA26", 26), ("SMA99", 99)]:
                value = self._sma(closes, length)
                if value is not None:
                    overlays.append(IndicatorOverlayOutput(name=name, value=round(value, 6), kind="line", color="default"))

        direction = "WAIT"
        confidence = 0
        reason = "insufficient_data"
        if len(closes) >= 26:
            fast = self._sma(closes, 7)
            slow = self._sma(closes, 26)
            if fast and slow and fast > slow:
                direction = "LONG"
                confidence = 60
                reason = "sma_fast_above_slow"
            elif fast and slow and fast < slow:
                direction = "SHORT"
                confidence = 60
                reason = "sma_fast_below_slow"
            else:
                reason = "neutral_structure"

        return IndicatorRuntimeOutput(
            indicator="yasara",
            version=self.version,
            overlays=overlays,
            signals=[IndicatorSignalOutput(direction=direction, confidence=confidence, reason=reason, execution_allowed=False)],
            panels={
                "ai_decision": {"direction": direction, "confidence": confidence},
                "risk_panel": {"execution_allowed": False, "mode": "analysis_only"},
            },
        )

yasara_indicator_runtime_adapter = YaSaraIndicatorRuntimeAdapter()
