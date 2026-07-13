def pivots(candles, left=2, right=2):
    highs = []
    lows = []
    for i in range(left, len(candles) - right):
        h = candles[i]["high"]
        l = candles[i]["low"]
        if all(h >= candles[j]["high"] for j in range(i - left, i + right + 1)):
            highs.append({"index": i, "price": h, "time": candles[i]["time"]})
        if all(l <= candles[j]["low"] for j in range(i - left, i + right + 1)):
            lows.append({"index": i, "price": l, "time": candles[i]["time"]})
    return highs, lows


def detect_bos(candles):
    highs, lows = pivots(candles)
    last_close = candles[-1]["close"] if candles else 0
    if highs and last_close > highs[-1]["price"]:
        return {"detected": True, "direction": "bullish", "level": highs[-1]["price"]}
    if lows and last_close < lows[-1]["price"]:
        return {"detected": True, "direction": "bearish", "level": lows[-1]["price"]}
    return {"detected": False, "direction": "neutral", "level": 0}


def detect_choch(candles):
    highs, lows = pivots(candles)
    if len(highs) < 2 or len(lows) < 2 or not candles:
        return {"detected": False, "direction": "neutral"}
    last_close = candles[-1]["close"]
    bullish_shift = lows[-1]["price"] > lows[-2]["price"] and last_close > highs[-1]["price"]
    bearish_shift = highs[-1]["price"] < highs[-2]["price"] and last_close < lows[-1]["price"]
    if bullish_shift:
        return {"detected": True, "direction": "bullish"}
    if bearish_shift:
        return {"detected": True, "direction": "bearish"}
    return {"detected": False, "direction": "neutral"}


def detect_fvg(candles):
    zones = []
    for i in range(2, len(candles)):
        c0 = candles[i - 2]
        c2 = candles[i]
        if c2["low"] > c0["high"]:
            zones.append({"type": "bullish_fvg", "from": c0["high"], "to": c2["low"], "index": i})
        if c2["high"] < c0["low"]:
            zones.append({"type": "bearish_fvg", "from": c2["high"], "to": c0["low"], "index": i})
    return zones[-10:]


def detect_imbalance(candles):
    zones = []
    for i, c in enumerate(candles[-60:]):
        body = abs(c["close"] - c["open"])
        spread = max(c["high"] - c["low"], 0.0001)
        ratio = body / spread
        if ratio > 0.72:
            zones.append({"index": i, "direction": "bullish" if c["close"] > c["open"] else "bearish", "ratio": round(ratio, 4)})
    return zones[-10:]


def detect_equal_high_low(candles, tolerance_pct=0.08):
    highs, lows = pivots(candles)
    equal_highs = []
    equal_lows = []
    for i in range(1, len(highs)):
        p1, p2 = highs[i - 1]["price"], highs[i]["price"]
        if p1 and abs(p2 - p1) / p1 * 100 <= tolerance_pct:
            equal_highs.append({"level": round((p1 + p2) / 2, 6), "points": [highs[i - 1], highs[i]]})
    for i in range(1, len(lows)):
        p1, p2 = lows[i - 1]["price"], lows[i]["price"]
        if p1 and abs(p2 - p1) / p1 * 100 <= tolerance_pct:
            equal_lows.append({"level": round((p1 + p2) / 2, 6), "points": [lows[i - 1], lows[i]]})
    return {"equal_highs": equal_highs[-5:], "equal_lows": equal_lows[-5:]}


def detect_liquidity_sweep(candles):
    highs, lows = pivots(candles)
    if not candles:
        return {"detected": False, "direction": "neutral"}
    last = candles[-1]
    if highs and last["high"] > highs[-1]["price"] and last["close"] < highs[-1]["price"]:
        return {"detected": True, "direction": "bearish", "swept_level": highs[-1]["price"]}
    if lows and last["low"] < lows[-1]["price"] and last["close"] > lows[-1]["price"]:
        return {"detected": True, "direction": "bullish", "swept_level": lows[-1]["price"]}
    return {"detected": False, "direction": "neutral", "swept_level": 0}


def detect_order_block(candles):
    bos = detect_bos(candles)
    if not bos["detected"] or len(candles) < 10:
        return {"detected": False, "direction": "neutral", "zone": None}
    search = candles[-12:-1]
    if bos["direction"] == "bullish":
        bearish = [c for c in search if c["close"] < c["open"]]
        c = bearish[-1] if bearish else search[-1]
        return {"detected": True, "direction": "bullish", "zone": {"high": c["high"], "low": c["low"], "time": c["time"]}}
    bullish = [c for c in search if c["close"] > c["open"]]
    c = bullish[-1] if bullish else search[-1]
    return {"detected": True, "direction": "bearish", "zone": {"high": c["high"], "low": c["low"], "time": c["time"]}}


def premium_discount(candles):
    if not candles:
        return {"zone": "unknown", "equilibrium": 0}
    highs = [c["high"] for c in candles[-80:]]
    lows = [c["low"] for c in candles[-80:]]
    high = max(highs)
    low = min(lows)
    eq = (high + low) / 2
    close = candles[-1]["close"]
    zone = "premium" if close > eq else "discount" if close < eq else "equilibrium"
    return {"zone": zone, "equilibrium": round(eq, 6), "range_high": high, "range_low": low}


def score_smart_money(bos, choch, sweep, order_block, fvg, premium):
    score = 50
    reasons = []
    if bos["detected"]:
        score += 10 if bos["direction"] == "bullish" else -10
        reasons.append(f"BOS {bos['direction']}")
    if choch["detected"]:
        score += 8 if choch["direction"] == "bullish" else -8
        reasons.append(f"CHoCH {choch['direction']}")
    if sweep["detected"]:
        score += 8 if sweep["direction"] == "bullish" else -8
        reasons.append(f"Liquidity sweep {sweep['direction']}")
    if order_block["detected"]:
        score += 6 if order_block["direction"] == "bullish" else -6
        reasons.append(f"Order block {order_block['direction']}")
    if fvg:
        last = fvg[-1]
        score += 4 if "bullish" in last["type"] else -4
        reasons.append(last["type"])
    if premium["zone"] == "discount":
        score += 4
        reasons.append("discount zone")
    if premium["zone"] == "premium":
        score -= 4
        reasons.append("premium zone")
    score = max(0, min(100, score))
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    return {"score": score, "bias": bias, "reasons": reasons}
