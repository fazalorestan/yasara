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
    gains = []
    losses = []
    for i in range(1, len(values)):
        diff = values[i] - values[i - 1]
        gains.append(max(diff, 0))
        losses.append(abs(min(diff, 0)))
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 4)


def macd(values, fast=12, slow=26, signal=9):
    if not values:
        return 0.0, 0.0
    fast_ema = ema(values, fast)
    slow_ema = ema(values, slow)
    macd_value = round(fast_ema - slow_ema, 6)
    # Lightweight deterministic signal line for v2.4 phase 1
    signal_value = round(macd_value * (signal / (signal + 3)), 6)
    return macd_value, signal_value
