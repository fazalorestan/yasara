def sma(values, period):
    if len(values) < period:
        return sum(values) / len(values) if values else 0
    return sum(values[-period:]) / period


def ema(values, period):
    if not values:
        return 0.0
    alpha = 2 / (period + 1)
    result = values[0]
    for value in values[1:]:
        result = alpha * value + (1 - alpha) * result
    return round(result, 6)


def rsi(values, period=14):
    if len(values) <= period:
        return 50.0
    gains, losses = [], []
    for i in range(1, len(values)):
        diff = values[i] - values[i - 1]
        gains.append(max(diff, 0))
        losses.append(abs(min(diff, 0)))
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0:
        return 100.0
    return round(100 - (100 / (1 + avg_gain / avg_loss)), 4)


def macd(values, fast=12, slow=26, signal=9):
    macd_line = ema(values, fast) - ema(values, slow)
    signal_line = macd_line * (signal / (signal + 3))
    histogram = macd_line - signal_line
    return round(macd_line, 6), round(signal_line, 6), round(histogram, 6)


def atr(candles, period=14):
    if len(candles) < 2:
        return 0.0
    trs = []
    for i in range(1, len(candles)):
        high = candles[i]["high"]
        low = candles[i]["low"]
        prev_close = candles[i - 1]["close"]
        trs.append(max(high - low, abs(high - prev_close), abs(low - prev_close)))
    return round(sum(trs[-period:]) / min(period, len(trs)), 6)


def bollinger(values, period=20, multiplier=2):
    if not values:
        return {"middle": 0, "upper": 0, "lower": 0, "width": 0}
    source = values[-period:] if len(values) >= period else values
    middle = sum(source) / len(source)
    variance = sum((x - middle) ** 2 for x in source) / len(source)
    std = variance ** 0.5
    upper = middle + multiplier * std
    lower = middle - multiplier * std
    width = (upper - lower) / middle if middle else 0
    return {"middle": round(middle, 6), "upper": round(upper, 6), "lower": round(lower, 6), "width": round(width, 6)}


def supertrend(candles, period=10, multiplier=3):
    if not candles:
        return {"value": 0, "trend": "neutral"}
    a = atr(candles, period)
    last = candles[-1]
    hl2 = (last["high"] + last["low"]) / 2
    upper = hl2 + multiplier * a
    lower = hl2 - multiplier * a
    trend = "bullish" if last["close"] >= lower else "bearish"
    value = lower if trend == "bullish" else upper
    return {"value": round(value, 6), "trend": trend}


def ichimoku(candles):
    highs = [c["high"] for c in candles]
    lows = [c["low"] for c in candles]
    closes = [c["close"] for c in candles]
    def mid(period):
        if len(highs) < period:
            return (max(highs) + min(lows)) / 2 if highs else 0
        return (max(highs[-period:]) + min(lows[-period:])) / 2
    tenkan = mid(9)
    kijun = mid(26)
    senkou_a = (tenkan + kijun) / 2
    senkou_b = mid(52)
    cloud = "bullish" if closes and closes[-1] > max(senkou_a, senkou_b) else "bearish" if closes and closes[-1] < min(senkou_a, senkou_b) else "neutral"
    return {"tenkan": round(tenkan, 6), "kijun": round(kijun, 6), "senkou_a": round(senkou_a, 6), "senkou_b": round(senkou_b, 6), "cloud": cloud}
