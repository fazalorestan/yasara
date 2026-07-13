from app.platform_core.indicators.bridges.service import indicator_engine_bridge_service
from app.platform_core.indicators.runtime.models import CandleInput, IndicatorRuntimeInput
from app.platform_core.indicators.runtime.yasara_runtime import yasara_indicator_runtime_adapter
from app.v445_indicator_engine_bridge.models import IndicatorEngineBridgeSummaryV445

class IndicatorEngineBridgeFacadeV445:
    def summary(self):
        return IndicatorEngineBridgeSummaryV445()

    def bridge_sample(self):
        candles = [CandleInput(time=i, open=100+i, high=101+i, low=99+i, close=100+i, volume=1000+i) for i in range(30)]
        runtime = yasara_indicator_runtime_adapter.run(IndicatorRuntimeInput(symbol="BTCUSDT", timeframe="4H", candles=candles))
        runtime_dict = runtime.__dict__ | {
            "overlays": [o.__dict__ for o in runtime.overlays],
            "signals": [s.__dict__ for s in runtime.signals],
        }
        return indicator_engine_bridge_service.bridge("BTCUSDT", runtime_dict)

    def bridge_contract(self):
        return {
            "ready": True,
            "inputs": ["symbol", "runtime_output"],
            "outputs": ["ai_decision", "risk_panel", "scanner", "confidence", "event"],
            "execution_allowed": False,
            "mode": "analysis_only",
        }
