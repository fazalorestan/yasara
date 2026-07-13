def build_swing_points(swings):
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
    return dedup[-14:]

def parse_waves(points):
    waves = []
    for i in range(1, len(points)):
        a, b = points[i-1], points[i]
        direction = "up" if b["price"] > a["price"] else "down" if b["price"] < a["price"] else "flat"
        waves.append({
            "raw_id": f"R{i}",
            "from": a,
            "to": b,
            "direction": direction,
            "price_change": round(b["price"] - a["price"], 6),
            "price_change_abs": round(abs(b["price"] - a["price"]), 6),
            "duration": b["index"] - a["index"],
        })
    return waves

def number_impulse(waves):
    selected = waves[-5:] if len(waves) >= 5 else waves
    labels = ["1", "2", "3", "4", "5"]
    return [{**w, "wave": labels[i]} for i, w in enumerate(selected)]

def number_correction(waves):
    selected = waves[-3:] if len(waves) >= 3 else waves
    labels = ["A", "B", "C"]
    return [{**w, "wave": labels[i]} for i, w in enumerate(selected)]

def fibonacci_base(waves):
    ratios = []
    for i in range(1, len(waves)):
        prev = waves[i-1].get("price_change_abs", 0)
        cur = waves[i].get("price_change_abs", 0)
        ratio = round(cur / prev, 6) if prev else 0
        fib_like = any(abs(ratio - f) <= 0.12 for f in [0.382, 0.5, 0.618, 1.0, 1.272, 1.618, 2.618])
        ratios.append({"wave": waves[i].get("wave", waves[i].get("raw_id")), "ratio": ratio, "fib_like": fib_like})
    score = round(sum(1 for r in ratios if r["fib_like"]) / max(len(ratios), 1) * 100, 2) if ratios else 0
    return {"ratios": ratios, "score": score, "valid": score >= 40}

def classify_elliott_pattern(impulse_validation, correction_validation, impulse_waves, correction_waves):
    if impulse_validation["valid"] and len(impulse_waves) >= 5:
        direction = impulse_waves[0]["direction"]
        return {"pattern": "impulse_candidate", "bias": "bullish" if direction == "up" else "bearish", "confidence": impulse_validation["score"]}
    if correction_validation["valid"] and len(correction_waves) >= 3:
        return {"pattern": "correction_candidate", "bias": "neutral", "confidence": correction_validation["score"]}
    return {"pattern": "invalid_or_incomplete_count", "bias": "neutral", "confidence": max(impulse_validation["score"], correction_validation["score"])}

def elliott_context_score(pattern, fib, impulse_validation, correction_validation):
    score = 50
    reasons = []
    if pattern["pattern"] == "impulse_candidate":
        score += 14 if pattern["bias"] == "bullish" else -14
        reasons.append(f"elliott_{pattern['bias']}_impulse")
    elif pattern["pattern"] == "correction_candidate":
        reasons.append("elliott_correction_candidate")
    else:
        score -= 4
        reasons.append("elliott_invalid_or_incomplete")
    score += (fib.get("score", 0) - 50) * 0.15
    if impulse_validation.get("valid"):
        reasons.append("impulse_rules_valid")
    if correction_validation.get("valid"):
        reasons.append("correction_rules_valid")
    if fib.get("valid"):
        reasons.append("fib_base_valid")
    score = round(max(0, min(100, score)), 2)
    bias = "bullish" if score >= 60 else "bearish" if score <= 40 else "neutral"
    return {"score": score, "bias": bias, "reasons": reasons}
