def candle_direction(c):
    return "bullish" if c["close"] > c["open"] else "bearish" if c["close"] < c["open"] else "neutral"

def body_ratio(c):
    spread = max(c["high"] - c["low"], 0.000001)
    return abs(c["close"] - c["open"]) / spread

def order_blocks(candles, structure_bias="neutral"):
    zones = []
    for i in range(3, len(candles) - 1):
        c = candles[i]
        nxt = candles[i + 1]
        direction = candle_direction(c)
        next_direction = candle_direction(nxt)
        displacement = body_ratio(nxt) > 0.6
        if direction == "bearish" and next_direction == "bullish" and displacement:
            zones.append({"type": "bullish_order_block", "index": i, "time": c["time"], "high": c["high"], "low": c["low"], "strength": round(body_ratio(nxt)*100, 2), "structure_bias": structure_bias})
        if direction == "bullish" and next_direction == "bearish" and displacement:
            zones.append({"type": "bearish_order_block", "index": i, "time": c["time"], "high": c["high"], "low": c["low"], "strength": round(body_ratio(nxt)*100, 2), "structure_bias": structure_bias})
    return zones[-12:]

def fair_value_gaps(candles):
    zones = []
    for i in range(2, len(candles)):
        left = candles[i - 2]
        mid = candles[i - 1]
        right = candles[i]
        if right["low"] > left["high"]:
            zones.append({"type": "bullish_fvg", "index": i, "from": left["high"], "to": right["low"], "mid_time": mid["time"], "size": round(right["low"] - left["high"], 6)})
        if right["high"] < left["low"]:
            zones.append({"type": "bearish_fvg", "index": i, "from": right["high"], "to": left["low"], "mid_time": mid["time"], "size": round(left["low"] - right["high"], 6)})
    return zones[-12:]

def imbalance_zones(candles):
    zones = []
    for i, c in enumerate(candles):
        ratio = body_ratio(c)
        if ratio >= 0.72:
            zones.append({"index": i, "time": c["time"], "direction": candle_direction(c), "ratio": round(ratio, 4), "high": c["high"], "low": c["low"]})
    return zones[-12:]

def mitigation_status(candles, zones):
    close = candles[-1]["close"] if candles else 0
    output = []
    for z in zones:
        low, high = min(z.get("low", z.get("from", 0)), z.get("to", z.get("high", 0))), max(z.get("high", z.get("to", 0)), z.get("from", 0))
        touched = any(c["low"] <= high and c["high"] >= low for c in candles[z.get("index", 0)+1:])
        invalidated = close < low if "bullish" in z.get("type", "") else close > high if "bearish" in z.get("type", "") else False
        item = dict(z)
        item["mitigated"] = bool(touched)
        item["invalidated"] = bool(invalidated)
        output.append(item)
    return output

def breaker_candidates(order_block_zones):
    candidates = []
    for z in order_block_zones:
        if z.get("invalidated"):
            direction = "bearish" if "bullish" in z["type"] else "bullish"
            candidates.append({"type": "breaker_candidate", "origin": z["type"], "direction": direction, "high": z["high"], "low": z["low"], "time": z["time"]})
    return candidates[-8:]

def smart_money_score(order_blocks_out, fvg_out, imbalance_out, breaker_out, structure_bias="neutral"):
    score = 50
    reasons = []
    latest_ob = order_blocks_out[-1] if order_blocks_out else None
    latest_fvg = fvg_out[-1] if fvg_out else None
    if latest_ob:
        if "bullish" in latest_ob["type"]:
            score += 10; reasons.append("bullish_order_block")
        if "bearish" in latest_ob["type"]:
            score -= 10; reasons.append("bearish_order_block")
        if latest_ob.get("mitigated"):
            score += 3 if "bullish" in latest_ob["type"] else -3
            reasons.append("order_block_mitigated")
    if latest_fvg:
        if "bullish" in latest_fvg["type"]:
            score += 7; reasons.append("bullish_fvg")
        if "bearish" in latest_fvg["type"]:
            score -= 7; reasons.append("bearish_fvg")
    if imbalance_out:
        last = imbalance_out[-1]
        if last["direction"] == "bullish":
            score += 5; reasons.append("bullish_imbalance")
        if last["direction"] == "bearish":
            score -= 5; reasons.append("bearish_imbalance")
    if breaker_out:
        last = breaker_out[-1]
        score += 6 if last["direction"] == "bullish" else -6
        reasons.append(f"breaker_{last['direction']}")
    if structure_bias == "bullish":
        score += 6; reasons.append("structure_bias_bullish")
    if structure_bias == "bearish":
        score -= 6; reasons.append("structure_bias_bearish")
    score = round(max(0, min(100, score)), 2)
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    return {"score": score, "bias": bias, "reasons": reasons}
