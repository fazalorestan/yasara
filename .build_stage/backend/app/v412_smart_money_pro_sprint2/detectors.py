def liquidity_grab(candles, liquidity_zones):
    if len(candles) < 2:
        return {"detected": False, "direction": "neutral", "reason": "not_enough_candles"}
    last = candles[-1]
    prev = candles[-2]
    for zone in liquidity_zones.get("buy_side_liquidity", [])[-6:]:
        level = zone["level"]
        if prev["close"] <= level and last["high"] > level and last["close"] < level:
            return {"detected": True, "direction": "bearish", "level": level, "type": "buy_side_liquidity_grab"}
    for zone in liquidity_zones.get("sell_side_liquidity", [])[-6:]:
        level = zone["level"]
        if prev["close"] >= level and last["low"] < level and last["close"] > level:
            return {"detected": True, "direction": "bullish", "level": level, "type": "sell_side_liquidity_grab"}
    return {"detected": False, "direction": "neutral", "reason": "no_grab"}

def sweep_pro(candles, basic_sweep, liquidity_grab_result):
    if basic_sweep.get("detected") and liquidity_grab_result.get("detected"):
        confidence = 85 if basic_sweep.get("direction") == liquidity_grab_result.get("direction") else 55
        return {
            "detected": True,
            "direction": basic_sweep.get("direction"),
            "confidence": confidence,
            "type": "confirmed_sweep_and_grab",
            "level": basic_sweep.get("level"),
        }
    if basic_sweep.get("detected"):
        return {"detected": True, "direction": basic_sweep.get("direction"), "confidence": 65, "type": "sweep_only", "level": basic_sweep.get("level")}
    if liquidity_grab_result.get("detected"):
        return {"detected": True, "direction": liquidity_grab_result.get("direction"), "confidence": 70, "type": "grab_only", "level": liquidity_grab_result.get("level")}
    return {"detected": False, "direction": "neutral", "confidence": 0, "type": "none", "level": 0}

def premium_discount_entry(pd_context, direction):
    zone = pd_context.get("zone", "unknown")
    if direction == "bullish" and zone == "discount":
        return {"aligned": True, "zone": zone, "quality": 85, "reason": "bullish_in_discount"}
    if direction == "bearish" and zone == "premium":
        return {"aligned": True, "zone": zone, "quality": 85, "reason": "bearish_in_premium"}
    if zone == "equilibrium":
        return {"aligned": False, "zone": zone, "quality": 50, "reason": "equilibrium"}
    return {"aligned": False, "zone": zone, "quality": 35, "reason": "poor_premium_discount_alignment"}

def ob_fvg_confluence(order_blocks, fair_value_gaps):
    confluences = []
    for ob in order_blocks[-6:]:
        ob_low, ob_high = min(ob.get("low", 0), ob.get("high", 0)), max(ob.get("low", 0), ob.get("high", 0))
        ob_bias = "bullish" if "bullish" in ob.get("type", "") else "bearish" if "bearish" in ob.get("type", "") else "neutral"
        for fvg in fair_value_gaps[-6:]:
            fvg_low, fvg_high = min(fvg.get("from", 0), fvg.get("to", 0)), max(fvg.get("from", 0), fvg.get("to", 0))
            fvg_bias = "bullish" if "bullish" in fvg.get("type", "") else "bearish" if "bearish" in fvg.get("type", "") else "neutral"
            overlaps = ob_low <= fvg_high and fvg_low <= ob_high
            if overlaps and ob_bias == fvg_bias and ob_bias != "neutral":
                confluences.append({
                    "bias": ob_bias,
                    "ob_type": ob.get("type"),
                    "fvg_type": fvg.get("type"),
                    "zone_low": max(ob_low, fvg_low),
                    "zone_high": min(ob_high, fvg_high),
                    "quality": 80,
                })
    return confluences[-8:]

def entry_quality_score(sweep, pd_entry, confluences, structure_bias, smc_bias):
    score = 50
    reasons = []
    direction = smc_bias
    if sweep.get("detected"):
        score += 12 if sweep.get("direction") == "bullish" else -12
        direction = sweep.get("direction")
        reasons.append(f"sweep_pro_{sweep.get('direction')}")
    if pd_entry.get("aligned"):
        score += 10 if direction == "bullish" else -10
        reasons.append(pd_entry.get("reason"))
    if confluences:
        last = confluences[-1]
        score += 10 if last["bias"] == "bullish" else -10
        reasons.append(f"ob_fvg_confluence_{last['bias']}")
    if structure_bias == direction and direction in ["bullish", "bearish"]:
        score += 8 if direction == "bullish" else -8
        reasons.append("structure_smc_aligned")
    if smc_bias == direction and direction in ["bullish", "bearish"]:
        score += 6 if direction == "bullish" else -6
        reasons.append("smc_bias_confirmed")
    score = round(max(0, min(100, score)), 2)
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    risk = "low" if score >= 75 or score <= 25 else "medium" if score >= 60 or score <= 40 else "high"
    return {"score": score, "bias": bias, "risk": risk, "reasons": reasons}
