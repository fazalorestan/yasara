def build_wave_points(swings):
    points = []
    for h in swings.get("highs", []):
        points.append({"type": "high", "index": h["index"], "price": h["price"], "time": h.get("time", h["index"])})
    for l in swings.get("lows", []):
        points.append({"type": "low", "index": l["index"], "price": l["price"], "time": l.get("time", l["index"])})
    points = sorted(points, key=lambda x: x["index"])
    dedup = []
    for p in points:
        if not dedup or p["index"] != dedup[-1]["index"]:
            dedup.append(p)
    return dedup[-12:]

def build_waves(points):
    waves = []
    for i in range(1, len(points)):
        a, b = points[i-1], points[i]
        direction = "up" if b["price"] > a["price"] else "down" if b["price"] < a["price"] else "flat"
        price_change = b["price"] - a["price"]
        duration = b["index"] - a["index"]
        waves.append({
            "wave_id": f"W{i}",
            "from": a,
            "to": b,
            "direction": direction,
            "price_change": round(price_change, 6),
            "price_change_abs": round(abs(price_change), 6),
            "duration": duration,
        })
    return waves

def classify_pattern_skeleton(waves):
    if len(waves) < 3:
        return {"pattern": "unknown", "confidence": 0, "reason": "not_enough_waves"}
    directions = [w["direction"] for w in waves if w["direction"] != "flat"]
    up = directions.count("up")
    down = directions.count("down")
    if len(waves) >= 5 and up > down:
        return {"pattern": "impulse_candidate", "confidence": 65, "bias": "bullish"}
    if len(waves) >= 5 and down > up:
        return {"pattern": "impulse_candidate", "confidence": 65, "bias": "bearish"}
    if len(waves) >= 3:
        return {"pattern": "correction_candidate", "confidence": 55, "bias": "neutral"}
    return {"pattern": "unknown", "confidence": 0, "bias": "neutral"}

def neowave_context_score(validation, pattern):
    score = 50
    reasons = []
    score += (validation.get("confidence", 50) - 50) * 0.35
    if pattern.get("pattern") == "impulse_candidate":
        score += 12 if pattern.get("bias") == "bullish" else -12 if pattern.get("bias") == "bearish" else 0
        reasons.append(f"neowave_{pattern.get('bias')}_impulse_candidate")
    if pattern.get("pattern") == "correction_candidate":
        reasons.append("neowave_correction_candidate")
    if validation.get("valid"):
        reasons.append("neowave_rules_valid")
    else:
        reasons.append("neowave_rules_weak")
    score = round(max(0, min(100, score)), 2)
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    return {"score": score, "bias": bias, "reasons": reasons}
