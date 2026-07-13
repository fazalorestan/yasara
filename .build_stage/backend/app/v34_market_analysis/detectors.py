def safe_last(values, default=0):
    return values[-1] if values else default


def detect_trend(closes):
    if len(closes) < 20:
        return {"trend": "unknown", "strength": 0}
    short = sum(closes[-10:]) / 10
    long = sum(closes[-30:]) / min(30, len(closes)) if len(closes) >= 10 else short
    diff_pct = ((short - long) / long * 100) if long else 0
    if diff_pct > 0.25:
        return {"trend": "bullish", "strength": round(min(abs(diff_pct) * 10, 100), 2)}
    if diff_pct < -0.25:
        return {"trend": "bearish", "strength": round(min(abs(diff_pct) * 10, 100), 2)}
    return {"trend": "sideways", "strength": round(abs(diff_pct) * 10, 2)}


def detect_range(candles):
    if not candles:
        return {"is_range": False, "range_percent": 0}
    highs = [c["high"] for c in candles[-40:]]
    lows = [c["low"] for c in candles[-40:]]
    mid = (max(highs) + min(lows)) / 2 if highs and lows else 0
    width = ((max(highs) - min(lows)) / mid * 100) if mid else 0
    return {"is_range": width < 2.5, "range_percent": round(width, 4), "high": max(highs), "low": min(lows)}


def detect_volatility(candles):
    if len(candles) < 2:
        return {"volatility": "unknown", "score": 0}
    trs = []
    for i in range(1, len(candles)):
        high = candles[i]["high"]
        low = candles[i]["low"]
        prev_close = candles[i - 1]["close"]
        trs.append(max(high - low, abs(high - prev_close), abs(low - prev_close)))
    avg_tr = sum(trs[-20:]) / min(20, len(trs))
    price = candles[-1]["close"]
    pct = (avg_tr / price * 100) if price else 0
    label = "high" if pct > 1.5 else "medium" if pct > 0.6 else "low"
    return {"volatility": label, "score": round(pct, 4)}


def detect_momentum(closes):
    if len(closes) < 15:
        return {"momentum": "unknown", "score": 0}
    change = closes[-1] - closes[-15]
    pct = (change / closes[-15] * 100) if closes[-15] else 0
    label = "positive" if pct > 0.3 else "negative" if pct < -0.3 else "neutral"
    return {"momentum": label, "score": round(pct, 4)}


def analyze_volume(candles):
    if not candles:
        return {"volume_state": "unknown", "relative_volume": 0}
    volumes = [c.get("volume", 0) for c in candles]
    avg = sum(volumes[-30:]) / min(30, len(volumes))
    rv = volumes[-1] / avg if avg else 0
    state = "expanding" if rv > 1.25 else "contracting" if rv < 0.75 else "normal"
    return {"volume_state": state, "relative_volume": round(rv, 4)}


def detect_regime(trend, range_data, volatility, momentum):
    if range_data["is_range"]:
        return "range"
    if trend["trend"] in ["bullish", "bearish"] and volatility["volatility"] in ["medium", "high"]:
        return "trending"
    if volatility["volatility"] == "high" and momentum["momentum"] != "neutral":
        return "volatile_momentum"
    return "mixed"


def session_analysis(timestamp):
    hour = (timestamp // 3600) % 24
    if 0 <= hour < 7:
        session = "asia"
    elif 7 <= hour < 13:
        session = "london"
    elif 13 <= hour < 21:
        session = "new_york"
    else:
        session = "after_hours"
    return {"session": session, "hour_utc": hour}
