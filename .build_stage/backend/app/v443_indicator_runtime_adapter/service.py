from app.platform_core.indicators.runtime.models import CandleInput, IndicatorRuntimeInput
from app.platform_core.indicators.runtime.yasara_runtime import yasara_indicator_runtime_adapter
from app.v443_indicator_runtime_adapter.models import IndicatorRuntimeAdapterSummaryV443

class IndicatorRuntimeAdapterServiceV443:
    def summary(self):
        return IndicatorRuntimeAdapterSummaryV443()

    def sample_input(self):
        candles = [
            CandleInput(time=i, open=100+i, high=101+i, low=99+i, close=100+i, volume=1000+i).__dict__
            for i in range(30)
        ]
        return {"ready": True, "input": {"symbol": "BTCUSDT", "timeframe": "4H", "candles": candles}}

    def run_sample(self):
        candles = [CandleInput(time=i, open=100+i, high=101+i, low=99+i, close=100+i, volume=1000+i) for i in range(30)]
        output = yasara_indicator_runtime_adapter.run(IndicatorRuntimeInput(symbol="BTCUSDT", timeframe="4H", candles=candles))
        return {"ready": True, "output": output.__dict__ | {"overlays": [o.__dict__ for o in output.overlays], "signals": [s.__dict__ for s in output.signals]}}

    def runtime_contract(self):
        return {
            "ready": True,
            "input": ["symbol", "timeframe", "candles", "settings"],
            "candle": ["time", "open", "high", "low", "close", "volume"],
            "output": ["indicator", "version", "overlays", "signals", "panels", "mode"],
            "execution_allowed": False,
            "mode": "analysis_only",
        }
