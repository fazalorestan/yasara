from app.platform_core.indicators.math_runtime.kernel import indicator_calculation_kernel
from app.platform_core.indicators.signal_logic_expansion.service import runtime_signal_expansion_service
from app.v500_alpha8_signal_logic_expansion.models import SignalLogicExpansionSummaryV500Alpha8

class SignalLogicExpansionFacadeV500Alpha8:
    def summary(self):
        return SignalLogicExpansionSummaryV500Alpha8()

    def sample_candles(self, trend: str = "up"):
        if trend == "down":
            return [{"open": 200 - i, "high": 202 - i, "low": 199 - i, "close": 201 - i, "volume": 1000 + i} for i in range(80)]
        return [{"open": 100 + i, "high": 102 + i, "low": 99 + i, "close": 101 + i, "volume": 1000 + i} for i in range(80)]

    def evaluate_sample(self, trend: str = "up"):
        math_output = indicator_calculation_kernel.calculate(self.sample_candles(trend))
        return runtime_signal_expansion_service.evaluate(math_output)

    def safety(self):
        return runtime_signal_expansion_service.safety()

    def contract(self):
        return {
            "ready": True,
            "outputs": ["direction", "confidence", "band", "reasons", "reason_codes", "validation"],
            "execution_allowed": False,
            "mode": "analysis_only",
        }
