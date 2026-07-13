from app.platform_core.indicators.math_runtime.kernel import indicator_calculation_kernel
from app.platform_core.indicators.signal_logic.service import yasara_runtime_signal_logic_service
from app.v500_alpha7_runtime_signal_logic.models import RuntimeSignalLogicSummaryV500Alpha7

class RuntimeSignalLogicFacadeV500Alpha7:
    def summary(self):
        return RuntimeSignalLogicSummaryV500Alpha7()

    def sample_candles(self):
        return [{"open": 100 + i, "high": 102 + i, "low": 99 + i, "close": 101 + i, "volume": 1000 + i} for i in range(80)]

    def evaluate_sample(self):
        math_output = indicator_calculation_kernel.calculate(self.sample_candles())
        return yasara_runtime_signal_logic_service.evaluate(math_output)

    def contract(self):
        return {
            "ready": True,
            "inputs": ["math_output"],
            "outputs": ["direction", "confidence", "reasons"],
            "execution_allowed": False,
            "mode": "analysis_only",
        }
