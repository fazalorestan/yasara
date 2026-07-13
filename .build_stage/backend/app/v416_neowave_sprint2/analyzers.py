def safe_div(a, b):
    return round(a / b, 6) if b else 0

def wave_ratios(waves):
    ratios = []
    for i in range(1, len(waves)):
        prev = waves[i-1].get("price_change_abs", 0)
        cur = waves[i].get("price_change_abs", 0)
        ratios.append({
            "wave": waves[i].get("wave_id", f"W{i+1}"),
            "price_ratio_to_previous": safe_div(cur, prev),
            "duration_ratio_to_previous": safe_div(waves[i].get("duration", 0), waves[i-1].get("duration", 0)),
        })
    return ratios

def complexity_engine(waves):
    if len(waves) < 3:
        return {"level": "unknown", "score": 0, "reason": "not_enough_waves"}
    direction_changes = 0
    for i in range(1, len(waves)):
        if waves[i].get("direction") != waves[i-1].get("direction"):
            direction_changes += 1
    avg_duration = sum(w.get("duration", 0) for w in waves) / max(len(waves), 1)
    if direction_changes >= len(waves) - 2 and avg_duration >= 2:
        return {"level": "medium", "score": 65, "reason": "alternating_waves"}
    if direction_changes < len(waves) / 2:
        return {"level": "low", "score": 45, "reason": "directional_sequence"}
    return {"level": "high", "score": 80, "reason": "dense_alternation"}

def time_rules(waves):
    checks = []
    for w in waves:
        checks.append(w.get("duration", 0) > 0)
    passed = sum(1 for x in checks if x)
    score = round(passed / max(len(checks), 1) * 100, 2)
    return {"valid": score >= 70, "score": score, "passed": passed, "total": len(checks)}

def price_rules(waves):
    checks = []
    for w in waves:
        checks.append(w.get("price_change_abs", 0) > 0)
    passed = sum(1 for x in checks if x)
    score = round(passed / max(len(checks), 1) * 100, 2)
    return {"valid": score >= 70, "score": score, "passed": passed, "total": len(checks)}

def ratio_quality(ratios):
    if not ratios:
        return {"score": 0, "quality": "unknown"}
    valid = 0
    for r in ratios:
        pr = r.get("price_ratio_to_previous", 0)
        if 0.236 <= pr <= 4.236:
            valid += 1
    score = round(valid / len(ratios) * 100, 2)
    quality = "good" if score >= 70 else "weak" if score >= 40 else "poor"
    return {"score": score, "quality": quality}

def pattern_confidence(base_pattern, validation, complexity, time_rule, price_rule, ratio_q):
    score = 0
    weights = {
        "base_pattern": 0.20,
        "validation": 0.25,
        "complexity": 0.15,
        "time": 0.15,
        "price": 0.15,
        "ratio": 0.10,
    }
    base_score = base_pattern.get("confidence", 0)
    score += base_score * weights["base_pattern"]
    score += validation.get("confidence", 0) * weights["validation"]
    score += complexity.get("score", 0) * weights["complexity"]
    score += time_rule.get("score", 0) * weights["time"]
    score += price_rule.get("score", 0) * weights["price"]
    score += ratio_q.get("score", 0) * weights["ratio"]
    score = round(max(0, min(100, score)), 2)
    bias = base_pattern.get("bias", "neutral")
    if score < 45:
        bias = "neutral"
    return {"confidence": score, "bias": bias, "quality": "high" if score >= 75 else "medium" if score >= 55 else "low"}
