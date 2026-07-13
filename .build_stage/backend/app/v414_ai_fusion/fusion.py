def normalize_confidence(value):
    try:
        value = float(value)
    except Exception:
        value = 50
    if value <= 1:
        value *= 100
    return round(max(0, min(100, value)), 2)

def bias_to_direction(bias):
    if bias in ["bullish", "long", "buy"]:
        return "bullish"
    if bias in ["bearish", "short", "sell"]:
        return "bearish"
    return "neutral"

def directional_score(bias, confidence):
    conf = normalize_confidence(confidence)
    b = bias_to_direction(bias)
    if b == "bullish":
        return conf
    if b == "bearish":
        return 100 - conf
    return 50

def default_weights():
    return {
        "market_context": 1.05,
        "market_structure": 1.25,
        "smart_money": 1.35,
        "ict": 1.25,
        "indicator": 0.85,
        "risk": 1.10,
    }

def dynamic_weight(module, base_weight, module_output):
    confidence = normalize_confidence(module_output.get("confidence", 50))
    bias = bias_to_direction(module_output.get("bias", "neutral"))
    weight = base_weight
    if confidence >= 80 and bias != "neutral":
        weight *= 1.15
    if confidence <= 40 or bias == "neutral":
        weight *= 0.85
    return round(weight, 4)

def agreement_score(modules):
    active = [m for m in modules if m.get("enabled", True)]
    if not active:
        return {"agreement_percent": 0, "dominant_bias": "neutral", "votes": {"bullish": 0, "bearish": 0, "neutral": 0}}
    votes = {"bullish": 0, "bearish": 0, "neutral": 0}
    for m in active:
        votes[bias_to_direction(m.get("bias", "neutral"))] += 1
    dominant = max(votes, key=votes.get)
    return {"agreement_percent": round(votes[dominant] / len(active) * 100, 2), "dominant_bias": dominant, "votes": votes}

def conflict_detection(modules):
    bullish = [m["module"] for m in modules if bias_to_direction(m.get("bias")) == "bullish"]
    bearish = [m["module"] for m in modules if bias_to_direction(m.get("bias")) == "bearish"]
    conflicts = []
    if bullish and bearish:
        conflicts.append({"type": "bullish_bearish_conflict", "bullish": bullish, "bearish": bearish})
    return {"has_conflict": bool(conflicts), "conflicts": conflicts}

def weak_signal_filter(score, confidence, agreement):
    if confidence < 35:
        return {"filtered": True, "reason": "low_final_confidence"}
    if agreement.get("agreement_percent", 0) < 45:
        return {"filtered": True, "reason": "low_engine_agreement"}
    if 45 <= score <= 55:
        return {"filtered": True, "reason": "neutral_score_zone"}
    return {"filtered": False, "reason": "signal_passed_filter"}

def strong_signal_booster(score, confidence, agreement):
    boosted = score
    reasons = []
    if confidence >= 75 and agreement.get("agreement_percent", 0) >= 70:
        boosted += 4 if score > 50 else -4
        reasons.append("high_confidence_high_agreement_boost")
    boosted = round(max(0, min(100, boosted)), 2)
    return {"score": boosted, "reasons": reasons}

def decision_from_score(score, filtered):
    if filtered.get("filtered"):
        return "WAIT"
    if score >= 62:
        return "LONG"
    if score <= 38:
        return "SHORT"
    return "WAIT"

def confidence_class(confidence):
    if confidence >= 75:
        return "HIGH"
    if confidence >= 55:
        return "MEDIUM"
    return "LOW"

def fuse_modules(modules):
    weights = default_weights()
    weighted_sum = 0
    total_weight = 0
    normalized_modules = []
    for m in modules:
        module = m.get("module")
        base = weights.get(module, 1.0)
        weight = dynamic_weight(module, base, m)
        score = directional_score(m.get("bias", "neutral"), m.get("confidence", 50))
        weighted_sum += score * weight
        total_weight += weight
        item = dict(m)
        item["normalized_score"] = round(score, 2)
        item["weight"] = weight
        normalized_modules.append(item)

    final_score = round(weighted_sum / total_weight, 2) if total_weight else 50
    final_confidence = round(abs(final_score - 50) * 2, 2)
    agreement = agreement_score(normalized_modules)
    conflicts = conflict_detection(normalized_modules)
    booster = strong_signal_booster(final_score, final_confidence, agreement)
    filtered = weak_signal_filter(booster["score"], final_confidence, agreement)
    decision = decision_from_score(booster["score"], filtered)

    return {
        "final_score": booster["score"],
        "raw_score": final_score,
        "final_confidence": final_confidence,
        "confidence_class": confidence_class(final_confidence),
        "decision": decision,
        "agreement": agreement,
        "conflict": conflicts,
        "filter": filtered,
        "booster": booster,
        "modules": normalized_modules,
    }

def explain(fusion):
    explanation = []
    explanation.append(f"Final decision is {fusion['decision']} with {fusion['confidence_class']} confidence.")
    explanation.append(f"Agreement is {fusion['agreement']['agreement_percent']}% with dominant bias {fusion['agreement']['dominant_bias']}.")
    if fusion["conflict"]["has_conflict"]:
        explanation.append("Conflicting engine outputs detected; decision confidence is reduced.")
    if fusion["filter"]["filtered"]:
        explanation.append(f"Signal filtered because: {fusion['filter']['reason']}.")
    for m in fusion["modules"]:
        explanation.append(f"{m['module']} bias={m.get('bias')} confidence={m.get('confidence')} weight={m.get('weight')}.")
    return explanation[:12]
