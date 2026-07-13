def kill_zone(timestamp):
    hour = int((timestamp // 3600) % 24)
    if 0 <= hour < 3:
        return {"zone": "asia", "active": True, "quality": 55}
    if 7 <= hour < 10:
        return {"zone": "london", "active": True, "quality": 80}
    if 12 <= hour < 16:
        return {"zone": "new_york", "active": True, "quality": 85}
    if 16 <= hour < 18:
        return {"zone": "london_close", "active": True, "quality": 65}
    return {"zone": "off_session", "active": False, "quality": 35}

def session_range(candles, lookback=40):
    src = candles[-lookback:] if len(candles) >= lookback else candles
    if not src:
        return {"high": 0, "low": 0, "mid": 0}
    high = max(c["high"] for c in src)
    low = min(c["low"] for c in src)
    return {"high": high, "low": low, "mid": round((high + low) / 2, 6)}

def judas_swing(candles, structure_bias="neutral"):
    if len(candles) < 10:
        return {"detected": False, "direction": "neutral", "reason": "not_enough_candles"}
    rng = session_range(candles[:-1], 30)
    last = candles[-1]
    if last["high"] > rng["high"] and last["close"] < rng["high"]:
        return {"detected": True, "direction": "bearish", "swept": "range_high", "level": rng["high"], "reason": "false_push_above_range"}
    if last["low"] < rng["low"] and last["close"] > rng["low"]:
        return {"detected": True, "direction": "bullish", "swept": "range_low", "level": rng["low"], "reason": "false_push_below_range"}
    return {"detected": False, "direction": "neutral", "reason": "no_judas_swing"}

def power_of_three(candles):
    if len(candles) < 30:
        return {"phase": "unknown", "confidence": 0}
    first = candles[-30:-20]
    mid = candles[-20:-10]
    last = candles[-10:]
    first_range = max(c["high"] for c in first) - min(c["low"] for c in first)
    mid_range = max(c["high"] for c in mid) - min(c["low"] for c in mid)
    last_change = last[-1]["close"] - last[0]["open"]
    if first_range < mid_range * 0.8 and abs(last_change) > first_range * 0.5:
        phase = "distribution" if last_change > 0 else "markdown"
    elif first_range < mid_range:
        phase = "manipulation"
    else:
        phase = "accumulation"
    return {"phase": phase, "confidence": 65 if phase != "unknown" else 0}

def ote_zone(candles):
    if not candles:
        return {"ready": False}
    high = max(c["high"] for c in candles[-80:])
    low = min(c["low"] for c in candles[-80:])
    diff = high - low
    bullish_ote = {"from": round(high - diff * 0.79, 6), "to": round(high - diff * 0.62, 6)}
    bearish_ote = {"from": round(low + diff * 0.62, 6), "to": round(low + diff * 0.79, 6)}
    close = candles[-1]["close"]
    in_bull = bullish_ote["from"] <= close <= bullish_ote["to"]
    in_bear = bearish_ote["from"] <= close <= bearish_ote["to"]
    return {"ready": True, "bullish_ote": bullish_ote, "bearish_ote": bearish_ote, "in_bullish_ote": in_bull, "in_bearish_ote": in_bear}

def ict_liquidity_model(structure, smc):
    mtf_bias = structure.get("multi_timeframe_structure", {}).get("bias", "neutral")
    smc_bias = smc.get("engine_output", {}).get("bias", "neutral")
    sweep = smc.get("smart_money_pro_sprint2", {}).get("sweep_pro", {})
    model = "neutral"
    if sweep.get("detected") and sweep.get("direction") == "bullish" and mtf_bias != "bearish":
        model = "bullish_liquidity_reversal"
    elif sweep.get("detected") and sweep.get("direction") == "bearish" and mtf_bias != "bullish":
        model = "bearish_liquidity_reversal"
    elif mtf_bias == smc_bias and mtf_bias in ["bullish", "bearish"]:
        model = f"{mtf_bias}_continuation"
    return {"model": model, "mtf_bias": mtf_bias, "smc_bias": smc_bias, "sweep": sweep}

def ict_context_score(kz, judas, po3, ote, liquidity):
    score = 50
    reasons = []
    model = liquidity.get("model", "neutral")
    if kz.get("active"):
        score += (kz.get("quality", 50) - 50) * 0.2
        reasons.append(f"kill_zone_{kz.get('zone')}")
    if judas.get("detected"):
        score += 12 if judas.get("direction") == "bullish" else -12
        reasons.append(f"judas_{judas.get('direction')}")
    if po3.get("phase") in ["distribution", "markdown"]:
        score += 5 if po3.get("phase") == "distribution" else -5
        reasons.append(f"po3_{po3.get('phase')}")
    if ote.get("in_bullish_ote"):
        score += 8; reasons.append("bullish_ote")
    if ote.get("in_bearish_ote"):
        score -= 8; reasons.append("bearish_ote")
    if "bullish" in model:
        score += 10; reasons.append(model)
    if "bearish" in model:
        score -= 10; reasons.append(model)
    score = round(max(0, min(100, score)), 2)
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    return {"score": score, "bias": bias, "reasons": reasons}
