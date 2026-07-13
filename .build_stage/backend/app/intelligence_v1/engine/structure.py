from app.intelligence_v1.domain.models import MarketStructurePack, TrendDirection
from app.market_data.domain.models import Candle

class MarketStructureAnalyzer:
    def analyze(self, candles: list[Candle]) -> MarketStructurePack:
        if len(candles) < 10:
            return MarketStructurePack()

        swing_highs: list[tuple[int, float]] = []
        swing_lows: list[tuple[int, float]] = []
        for i in range(2, len(candles) - 2):
            window = candles[i-2:i+3]
            if candles[i].high == max(c.high for c in window):
                swing_highs.append((i, candles[i].high))
            if candles[i].low == min(c.low for c in window):
                swing_lows.append((i, candles[i].low))

        higher_high = len(swing_highs) >= 2 and swing_highs[-1][1] > swing_highs[-2][1]
        lower_high = len(swing_highs) >= 2 and swing_highs[-1][1] < swing_highs[-2][1]
        higher_low = len(swing_lows) >= 2 and swing_lows[-1][1] > swing_lows[-2][1]
        lower_low = len(swing_lows) >= 2 and swing_lows[-1][1] < swing_lows[-2][1]

        if higher_high and higher_low:
            trend = TrendDirection.BULLISH
        elif lower_high and lower_low:
            trend = TrendDirection.BEARISH
        else:
            trend = TrendDirection.SIDEWAYS

        last_high = swing_highs[-1][1] if swing_highs else None
        last_low = swing_lows[-1][1] if swing_lows else None
        close = candles[-1].close
        bos = bool((last_high and close > last_high) or (last_low and close < last_low))

        return MarketStructurePack(
            trend=trend,
            higher_high=higher_high,
            higher_low=higher_low,
            lower_high=lower_high,
            lower_low=lower_low,
            last_swing_high=last_high,
            last_swing_low=last_low,
            break_of_structure=bos,
        )
