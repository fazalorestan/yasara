from app.platform_core.indicators.math_runtime.atr import atr_math
from app.platform_core.indicators.math_runtime.macd import macd_math
from app.platform_core.indicators.math_runtime.moving_average import moving_average_math
from app.platform_core.indicators.math_runtime.rsi import rsi_math

class IndicatorCalculationKernel:
    def calculate(self, candles: list[dict]):
        closes = [float(c["close"]) for c in candles]
        highs = [float(c["high"]) for c in candles]
        lows = [float(c["low"]) for c in candles]
        return {
            "ready": True,
            "sma_7": moving_average_math.sma(closes, 7),
            "ema_21": moving_average_math.ema(closes, 21),
            "ema_55": moving_average_math.ema(closes, 55),
            "rsi_14": rsi_math.rsi(closes, 14),
            "macd": macd_math.macd(closes),
            "atr_14": atr_math.atr(highs, lows, closes, 14),
            "mode": "math_only",
            "execution_allowed": False,
        }

indicator_calculation_kernel = IndicatorCalculationKernel()
