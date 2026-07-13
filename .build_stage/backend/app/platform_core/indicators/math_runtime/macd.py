from app.platform_core.indicators.math_runtime.moving_average import moving_average_math

class MACDMath:
    def macd(self, closes: list[float], fast: int = 12, slow: int = 26, signal: int = 9):
        if len(closes) < slow:
            return None
        fast_series = moving_average_math.ema_series(closes, fast)
        slow_series = moving_average_math.ema_series(closes, slow)
        size = min(len(fast_series), len(slow_series))
        macd_line = [fast_series[-size + i] - slow_series[-size + i] for i in range(size)]
        signal_line = moving_average_math.ema(macd_line, signal)
        current_macd = macd_line[-1]
        hist = current_macd - signal_line if signal_line is not None else 0
        return {"macd": current_macd, "signal": signal_line, "histogram": hist}

macd_math = MACDMath()
