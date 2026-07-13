def detect_swings(candles, left=2, right=2):
    swing_highs = []
    swing_lows = []
    for i in range(left, len(candles) - right):
        high = candles[i]["high"]
        low = candles[i]["low"]
        is_high = all(high >= candles[j]["high"] for j in range(i - left, i + right + 1))
        is_low = all(low <= candles[j]["low"] for j in range(i - left, i + right + 1))
        if is_high:
            swing_highs.append({"index": i, "price": high, "time": candles[i]["time"]})
        if is_low:
            swing_lows.append({"index": i, "price": low, "time": candles[i]["time"]})
    return {"highs": swing_highs, "lows": swing_lows}


def detect_bos(candles, swings):
    if not candles:
        return {"detected": False, "direction": "neutral", "level": 0}
    close = candles[-1]["close"]
    highs = swings.get("highs", [])
    lows = swings.get("lows", [])
    last_high = highs[-1]["price"] if highs else None
    last_low = lows[-1]["price"] if lows else None
    if last_high is not None and close > last_high:
        return {"detected": True, "direction": "bullish", "level": last_high}
    if last_low is not None and close < last_low:
        return {"detected": True, "direction": "bearish", "level": last_low}
    return {"detected": False, "direction": "neutral", "level": 0}


def trend_state(swings):
    highs = swings.get("highs", [])
    lows = swings.get("lows", [])
    if len(highs) < 2 or len(lows) < 2:
        return {"state": "unknown", "reason": "not_enough_swings"}
    hh = highs[-1]["price"] > highs[-2]["price"]
    hl = lows[-1]["price"] > lows[-2]["price"]
    lh = highs[-1]["price"] < highs[-2]["price"]
    ll = lows[-1]["price"] < lows[-2]["price"]
    if hh and hl:
        return {"state": "bullish", "reason": "higher_high_higher_low"}
    if lh and ll:
        return {"state": "bearish", "reason": "lower_high_lower_low"}
    return {"state": "range", "reason": "mixed_swings"}


def detect_choch(candles, swings, trend):
    bos = detect_bos(candles, swings)
    if not bos["detected"]:
        return {"detected": False, "direction": "neutral", "reason": "no_structure_break"}
    if trend["state"] == "bullish" and bos["direction"] == "bearish":
        return {"detected": True, "direction": "bearish", "reason": "bullish_trend_broken_down"}
    if trend["state"] == "bearish" and bos["direction"] == "bullish":
        return {"detected": True, "direction": "bullish", "reason": "bearish_trend_broken_up"}
    return {"detected": False, "direction": "neutral", "reason": "bos_with_trend"}


def range_state(candles, lookback=60):
    if not candles:
        return {"is_range": False, "width_percent": 0}
    src = candles[-lookback:] if len(candles) >= lookback else candles
    high = max(c["high"] for c in src)
    low = min(c["low"] for c in src)
    mid = (high + low) / 2
    width = ((high - low) / mid * 100) if mid else 0
    return {"is_range": width < 2.5, "width_percent": round(width, 4), "high": high, "low": low}


def premium_discount(candles, lookback=80):
    if not candles:
        return {"zone": "unknown", "equilibrium": 0}
    src = candles[-lookback:] if len(candles) >= lookback else candles
    high = max(c["high"] for c in src)
    low = min(c["low"] for c in src)
    eq = (high + low) / 2
    close = candles[-1]["close"]
    zone = "premium" if close > eq else "discount" if close < eq else "equilibrium"
    return {"zone": zone, "equilibrium": round(eq, 6), "range_high": high, "range_low": low}


def context_score(trend, bos, choch, range_info, pd):
    score = 50
    reasons = []
    if trend["state"] == "bullish":
        score += 12; reasons.append("trend_bullish")
    if trend["state"] == "bearish":
        score -= 12; reasons.append("trend_bearish")
    if bos["detected"]:
        score += 10 if bos["direction"] == "bullish" else -10
        reasons.append(f"bos_{bos['direction']}")
    if choch["detected"]:
        score += 8 if choch["direction"] == "bullish" else -8
        reasons.append(f"choch_{choch['direction']}")
    if range_info["is_range"]:
        score = (score + 50) / 2
        reasons.append("range_market")
    if pd["zone"] == "discount":
        score += 4; reasons.append("discount_zone")
    if pd["zone"] == "premium":
        score -= 4; reasons.append("premium_zone")
    score = round(max(0, min(100, score)), 2)
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    return {"score": score, "bias": bias, "reasons": reasons}
