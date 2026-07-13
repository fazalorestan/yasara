def classify_internal_external(swings):
    highs = swings.get("highs", [])
    lows = swings.get("lows", [])
    return {
        "external": {
            "range_high": max([x["price"] for x in highs], default=0),
            "range_low": min([x["price"] for x in lows], default=0),
        },
        "internal": {"recent_highs": highs[-5:], "recent_lows": lows[-5:]},
    }

def equal_levels(points, tolerance_percent=0.08):
    zones = []
    for i in range(1, len(points)):
        a, b = points[i - 1], points[i]
        if a["price"] == 0:
            continue
        diff = abs(b["price"] - a["price"]) / a["price"] * 100
        if diff <= tolerance_percent:
            zones.append({"level": round((a["price"] + b["price"]) / 2, 6), "points": [a, b], "tolerance_percent": round(diff, 6)})
    return zones[-8:]

def liquidity_zones(swings, tolerance_percent=0.08):
    eqh = equal_levels(swings.get("highs", []), tolerance_percent)
    eql = equal_levels(swings.get("lows", []), tolerance_percent)
    return {
        "equal_highs": eqh,
        "equal_lows": eql,
        "buy_side_liquidity": [{"level": x["level"], "type": "buy_side"} for x in eqh],
        "sell_side_liquidity": [{"level": x["level"], "type": "sell_side"} for x in eql],
    }

def liquidity_sweep(candles, zones):
    if not candles:
        return {"detected": False, "direction": "neutral", "level": 0}
    last = candles[-1]
    for zone in zones.get("buy_side_liquidity", [])[-5:]:
        level = zone["level"]
        if last["high"] > level and last["close"] < level:
            return {"detected": True, "direction": "bearish", "level": level, "type": "buy_side_sweep"}
    for zone in zones.get("sell_side_liquidity", [])[-5:]:
        level = zone["level"]
        if last["low"] < level and last["close"] > level:
            return {"detected": True, "direction": "bullish", "level": level, "type": "sell_side_sweep"}
    return {"detected": False, "direction": "neutral", "level": 0}

def structure_strength(v49_result, zones, sweep):
    score = v49_result["structure"]["context_score"]["score"]
    reasons = list(v49_result["structure"]["context_score"]["reasons"])
    if zones["equal_highs"] or zones["equal_lows"]:
        score += 4
        reasons.append("liquidity_zones_mapped")
    if sweep["detected"]:
        score += 8 if sweep["direction"] == "bullish" else -8
        reasons.append(f"liquidity_sweep_{sweep['direction']}")
    score = round(max(0, min(100, score)), 2)
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    return {"score": score, "bias": bias, "reasons": reasons}

def mtf_context(items):
    bullish = sum(1 for x in items if x["strength"]["bias"] == "bullish")
    bearish = sum(1 for x in items if x["strength"]["bias"] == "bearish")
    neutral = len(items) - bullish - bearish
    bias = "bullish" if bullish > bearish else "bearish" if bearish > bullish else "neutral"
    alignment = round(max(bullish, bearish, neutral) / max(len(items), 1) * 100, 2)
    return {"bias": bias, "alignment_percent": alignment, "votes": {"bullish": bullish, "bearish": bearish, "neutral": neutral}}
