def _value(candle, key, default=0):
    try:
        return float(candle.get(key, default))
    except Exception:
        return float(default)

def confirmed_swings(candles, left=2, right=2):
    highs, lows = [], []
    n = len(candles)
    if n < left + right + 3:
        return {"highs": highs, "lows": lows, "count": 0}
    for i in range(left, n - right):
        high, low = _value(candles[i], "high"), _value(candles[i], "low")
        lh = [_value(candles[j], "high") for j in range(i-left, i)]
        rh = [_value(candles[j], "high") for j in range(i+1, i+right+1)]
        ll = [_value(candles[j], "low") for j in range(i-left, i)]
        rl = [_value(candles[j], "low") for j in range(i+1, i+right+1)]
        if high >= max(lh + rh):
            highs.append({"index": i, "time": candles[i].get("time", i), "price": high, "type": "confirmed_swing_high"})
        if low <= min(ll + rl):
            lows.append({"index": i, "time": candles[i].get("time", i), "price": low, "type": "confirmed_swing_low"})
    return {"highs": highs, "lows": lows, "count": len(highs) + len(lows)}

def _last_before(items, index):
    past = [x for x in items if x["index"] < index]
    return past[-1] if past else None

def detect_bos_choch(candles, swings):
    events, trend = [], "neutral"
    highs, lows = swings.get("highs", []), swings.get("lows", [])
    for i, candle in enumerate(candles):
        close = _value(candle, "close")
        last_high, last_low = _last_before(highs, i), _last_before(lows, i)
        if last_high and close > last_high["price"]:
            event_type = "BOS" if trend in ["bullish", "neutral"] else "CHoCH"
            trend = "bullish"
            events.append({"type": event_type, "direction": "bullish", "index": i, "time": candle.get("time", i), "level": last_high["price"], "close": close, "label": f"{event_type} Bullish"})
        if last_low and close < last_low["price"]:
            event_type = "BOS" if trend in ["bearish", "neutral"] else "CHoCH"
            trend = "bearish"
            events.append({"type": event_type, "direction": "bearish", "index": i, "time": candle.get("time", i), "level": last_low["price"], "close": close, "label": f"{event_type} Bearish"})
    dedup, seen = [], set()
    for e in events:
        key = (e["type"], e["direction"], e["index"], round(e["level"], 8))
        if key not in seen:
            seen.add(key)
            dedup.append(e)
    return dedup[-30:]

def trend_state(events):
    if not events:
        return {"trend": "neutral", "confidence": 35, "reason": "no_structure_break"}
    recent = events[-6:]
    bullish = sum(1 for e in recent if e["direction"] == "bullish")
    bearish = sum(1 for e in recent if e["direction"] == "bearish")
    if bullish > bearish:
        return {"trend": "bullish", "confidence": min(95, 50 + bullish * 10), "reason": "recent_bullish_structure_breaks"}
    if bearish > bullish:
        return {"trend": "bearish", "confidence": min(95, 50 + bearish * 10), "reason": "recent_bearish_structure_breaks"}
    return {"trend": "neutral", "confidence": 45, "reason": "mixed_structure_breaks"}

def range_state(candles, swings, tolerance_percent=0.35):
    highs, lows = swings.get("highs", [])[-4:], swings.get("lows", [])[-4:]
    if len(highs) < 2 or len(lows) < 2:
        return {"ranging": False, "confidence": 30, "reason": "not_enough_swings"}
    hp, lp = [h["price"] for h in highs], [l["price"] for l in lows]
    avg_h, avg_l = sum(hp) / len(hp), sum(lp) / len(lp)
    high_dev = max(abs(h-avg_h)/avg_h*100 for h in hp) if avg_h else 100
    low_dev = max(abs(l-avg_l)/avg_l*100 for l in lp) if avg_l else 100
    ranging = high_dev <= tolerance_percent and low_dev <= tolerance_percent
    return {"ranging": ranging, "confidence": 80 if ranging else 45, "range_high": round(avg_h, 6), "range_low": round(avg_l, 6), "high_deviation_percent": round(high_dev, 4), "low_deviation_percent": round(low_dev, 4), "reason": "equalized_swing_boundaries" if ranging else "wide_swing_deviation"}

def structure_bias(trend, range_info):
    if range_info.get("ranging"):
        return {"bias": "neutral", "confidence": max(45, range_info.get("confidence", 50)), "market_mode": "range"}
    t = trend.get("trend", "neutral")
    return {"bias": "bullish" if t == "bullish" else "bearish" if t == "bearish" else "neutral", "confidence": trend.get("confidence", 50), "market_mode": "trend" if t != "neutral" else "unknown"}

def chart_annotations(swings, events, range_info):
    annotations = []
    for h in swings.get("highs", [])[-8:]:
        annotations.append({"kind": "swing_high", "time": h["time"], "index": h["index"], "price": h["price"], "color": "red", "label": "SH"})
    for l in swings.get("lows", [])[-8:]:
        annotations.append({"kind": "swing_low", "time": l["time"], "index": l["index"], "price": l["price"], "color": "green", "label": "SL"})
    for e in events[-10:]:
        annotations.append({"kind": e["type"].lower(), "time": e["time"], "index": e["index"], "price": e["level"], "color": "green" if e["direction"] == "bullish" else "red", "label": e["label"]})
    if range_info.get("ranging"):
        annotations.append({"kind": "range_high", "price": range_info["range_high"], "color": "blue", "label": "Range High"})
        annotations.append({"kind": "range_low", "price": range_info["range_low"], "color": "blue", "label": "Range Low"})
    return annotations

def score_structure(bias, events, range_info):
    score, reasons = 50, []
    if bias["bias"] == "bullish":
        score += 15; reasons.append("bullish_structure_bias")
    elif bias["bias"] == "bearish":
        score -= 15; reasons.append("bearish_structure_bias")
    else:
        reasons.append("neutral_structure_bias")
    recent_choch = [e for e in events[-6:] if e["type"] == "CHoCH"]
    if recent_choch:
        last = recent_choch[-1]; score += 8 if last["direction"] == "bullish" else -8; reasons.append(f"recent_choch_{last['direction']}")
    recent_bos = [e for e in events[-6:] if e["type"] == "BOS"]
    if recent_bos:
        last = recent_bos[-1]; score += 5 if last["direction"] == "bullish" else -5; reasons.append(f"recent_bos_{last['direction']}")
    if range_info.get("ranging"):
        score = 50; reasons.append("range_mode_reduces_directional_bias")
    score = round(max(0, min(100, score)), 2)
    return {"score": score, "bias": "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral", "reasons": reasons}
