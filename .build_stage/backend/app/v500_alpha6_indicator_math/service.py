from app.platform_core.indicators.math_runtime.kernel import indicator_calculation_kernel
from app.v500_alpha6_indicator_math.models import IndicatorMathSummaryV500Alpha6

class IndicatorMathFacadeV500Alpha6:
    def summary(self):
        return IndicatorMathSummaryV500Alpha6()

    def sample_candles(self):
        return [
            {"open": 100 + i, "high": 102 + i, "low": 99 + i, "close": 101 + i, "volume": 1000 + i}
            for i in range(80)
        ]

    def calculate_sample(self):
        return indicator_calculation_kernel.calculate(self.sample_candles())

    def contract(self):
        return {
            "ready": True,
            "math_modules": ["sma", "ema", "rsi", "macd", "atr"],
            "pure_functions": True,
            "execution_allowed": False,
            "mode": "math_only",
        }
