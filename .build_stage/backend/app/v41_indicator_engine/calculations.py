def closes(candles): return [c["close"] for c in candles]
def highs(candles): return [c["high"] for c in candles]
def lows(candles): return [c["low"] for c in candles]
def vols(candles): return [c.get("volume", 0) for c in candles]

def sma(values, period=20):
    if not values: return 0
    src = values[-period:] if len(values) >= period else values
    return round(sum(src) / len(src), 6)

def ema(values, period=20):
    if not values: return 0
    alpha = 2 / (period + 1)
    result = values[0]
    for v in values[1:]:
        result = alpha * v + (1 - alpha) * result
    return round(result, 6)

def rsi(values, period=14):
    if len(values) <= period: return 50.0
    gains, losses = [], []
    for i in range(1, len(values)):
        diff = values[i] - values[i-1]
        gains.append(max(diff, 0))
        losses.append(abs(min(diff, 0)))
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0: return 100.0
    return round(100 - (100 / (1 + avg_gain / avg_loss)), 4)

def macd(values):
    line = ema(values, 12) - ema(values, 26)
    signal = line * 0.75
    return {"line": round(line, 6), "signal": round(signal, 6), "histogram": round(line - signal, 6)}

def atr(candles, period=14):
    if len(candles) < 2: return 0
    trs = []
    for i in range(1, len(candles)):
        h, l, pc = candles[i]["high"], candles[i]["low"], candles[i-1]["close"]
        trs.append(max(h-l, abs(h-pc), abs(l-pc)))
    src = trs[-period:] if len(trs) >= period else trs
    return round(sum(src) / len(src), 6)

def bollinger(values, period=20, mult=2):
    if not values: return {"middle":0,"upper":0,"lower":0,"width":0}
    src = values[-period:] if len(values) >= period else values
    mid = sum(src) / len(src)
    var = sum((x-mid)**2 for x in src) / len(src)
    std = var ** 0.5
    up, lo = mid + mult*std, mid - mult*std
    return {"middle": round(mid,6), "upper": round(up,6), "lower": round(lo,6), "width": round((up-lo)/mid if mid else 0,6)}

def vwap(candles):
    if not candles: return 0
    pv = sum(((c["high"]+c["low"]+c["close"])/3) * c.get("volume",0) for c in candles)
    v = sum(c.get("volume",0) for c in candles)
    return round(pv / v, 6) if v else 0

def obv(candles):
    if len(candles) < 2: return 0
    total = 0
    for i in range(1, len(candles)):
        vol = candles[i].get("volume", 0)
        if candles[i]["close"] > candles[i-1]["close"]: total += vol
        elif candles[i]["close"] < candles[i-1]["close"]: total -= vol
    return round(total, 3)

def stochastic(candles, period=14):
    if not candles: return {"k":50,"d":50}
    src = candles[-period:] if len(candles) >= period else candles
    h, l, c = max(x["high"] for x in src), min(x["low"] for x in src), candles[-1]["close"]
    k = 50 if h == l else ((c-l)/(h-l))*100
    return {"k": round(k,4), "d": round(k,4)}

def donchian(candles, period=20):
    if not candles: return {"upper":0,"lower":0,"middle":0}
    src = candles[-period:] if len(candles) >= period else candles
    up, lo = max(c["high"] for c in src), min(c["low"] for c in src)
    return {"upper": up, "lower": lo, "middle": round((up+lo)/2,6)}

def keltner(candles, period=20):
    c = closes(candles)
    mid = ema(c, period)
    a = atr(candles, 14)
    return {"middle": mid, "upper": round(mid + 2*a, 6), "lower": round(mid - 2*a, 6)}

def supertrend(candles):
    if not candles: return {"value":0,"trend":"neutral"}
    a = atr(candles, 10)
    last = candles[-1]
    hl2 = (last["high"] + last["low"]) / 2
    lower = hl2 - 3*a
    upper = hl2 + 3*a
    trend = "bullish" if last["close"] >= lower else "bearish"
    return {"value": round(lower if trend == "bullish" else upper, 6), "trend": trend}

def adx(candles, period=14):
    # lightweight directional-strength proxy for foundation phase
    a = atr(candles, period)
    price = candles[-1]["close"] if candles else 0
    score = (a / price * 1000) if price else 0
    return round(min(max(score, 0), 100), 4)

def mfi(candles, period=14):
    if len(candles) <= period: return 50.0
    pos, neg = 0, 0
    for i in range(1, len(candles)):
        tp = (candles[i]["high"]+candles[i]["low"]+candles[i]["close"])/3
        prev = (candles[i-1]["high"]+candles[i-1]["low"]+candles[i-1]["close"])/3
        flow = tp * candles[i].get("volume",0)
        if tp > prev: pos += flow
        elif tp < prev: neg += flow
    if neg == 0: return 100.0
    return round(100 - (100/(1+pos/neg)), 4)

def cci(candles, period=20):
    if not candles: return 0
    src = candles[-period:] if len(candles) >= period else candles
    tps = [(c["high"]+c["low"]+c["close"])/3 for c in src]
    ma = sum(tps)/len(tps)
    md = sum(abs(x-ma) for x in tps)/len(tps)
    return round((tps[-1]-ma)/(0.015*md), 4) if md else 0

def parabolic_sar(candles):
    if not candles: return {"sar":0,"trend":"neutral"}
    trend = "bullish" if candles[-1]["close"] >= candles[0]["close"] else "bearish"
    sar = min(lows(candles[-10:])) if trend == "bullish" else max(highs(candles[-10:]))
    return {"sar": round(sar,6), "trend": trend}
