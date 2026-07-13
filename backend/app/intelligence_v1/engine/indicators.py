from app.market_data.domain.models import Candle

def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0

class IndicatorCalculator:
    def sma(self, values: list[float], period: int) -> float | None:
        if len(values) < period:
            return None
        return mean(values[-period:])

    def ema_series(self, values: list[float], period: int) -> list[float]:
        if len(values) < period:
            return []
        k = 2 / (period + 1)
        out = [mean(values[:period])]
        for value in values[period:]:
            out.append(value * k + out[-1] * (1 - k))
        return out

    def ema(self, values: list[float], period: int) -> float | None:
        series = self.ema_series(values, period)
        return series[-1] if series else None

    def rsi(self, values: list[float], period: int = 14) -> float | None:
        if len(values) <= period:
            return None
        gains = []
        losses = []
        for a, b in zip(values[-period-1:-1], values[-period:]):
            delta = b - a
            gains.append(max(delta, 0))
            losses.append(abs(min(delta, 0)))
        avg_gain = mean(gains)
        avg_loss = mean(losses)
        if avg_loss == 0:
            return 100.0
        return 100 - (100 / (1 + avg_gain / avg_loss))

    def macd(self, values: list[float]) -> tuple[float | None, float | None, float | None]:
        fast = self.ema_series(values, 12)
        slow = self.ema_series(values, 26)
        if not fast or not slow:
            return None, None, None
        n = min(len(fast), len(slow))
        macd_values = [a - b for a, b in zip(fast[-n:], slow[-n:])]
        signal = self.ema_series(macd_values, 9)
        if not signal:
            return macd_values[-1], None, None
        return macd_values[-1], signal[-1], macd_values[-1] - signal[-1]

    def atr(self, candles: list[Candle], period: int = 14) -> float | None:
        if len(candles) < period + 1:
            return None
        trs = []
        for i in range(1, len(candles)):
            current = candles[i]
            previous = candles[i - 1]
            trs.append(max(
                current.high - current.low,
                abs(current.high - previous.close),
                abs(current.low - previous.close),
            ))
        return mean(trs[-period:]) if len(trs) >= period else None

    def relative_volume(self, candles: list[Candle], period: int = 20) -> tuple[float | None, float | None]:
        if len(candles) < period + 1:
            return None, None
        avg = mean([c.volume for c in candles[-period-1:-1]])
        if avg == 0:
            return avg, None
        return avg, candles[-1].volume / avg
