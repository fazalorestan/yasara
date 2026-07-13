def clamp(value, lo, hi):
    return max(lo, min(hi, value))


def risk_amount(equity, risk_percent):
    return round(equity * risk_percent / 100, 6)


def stop_distance(entry, stop):
    return abs(entry - stop)


def position_size(equity, risk_percent, entry, stop):
    dist = stop_distance(entry, stop)
    if dist <= 0:
        return 0
    return round(risk_amount(equity, risk_percent) / dist, 8)


def notional(size, entry):
    return round(size * entry, 6)


def leverage_required(notional_value, equity):
    if equity <= 0:
        return 0
    return round(notional_value / equity, 4)


def reward_risk(entry, stop, tp):
    risk = abs(entry - stop)
    reward = abs(tp - entry)
    if risk <= 0:
        return 0
    return round(reward / risk, 4)


def kelly_fraction(win_rate, rr):
    # Kelly = W - (1-W)/R
    w = clamp(win_rate, 0, 1)
    r = max(rr, 0.0001)
    return round(clamp(w - ((1 - w) / r), 0, 1), 6)


def risk_limits(profile, state):
    reasons = []
    if state.kill_switch_active:
        reasons.append("kill_switch_active")
    if state.daily_loss_percent >= profile.daily_risk_limit_percent:
        reasons.append("daily_risk_limit_reached")
    if state.weekly_loss_percent >= profile.weekly_risk_limit_percent:
        reasons.append("weekly_risk_limit_reached")
    if state.monthly_loss_percent >= profile.monthly_risk_limit_percent:
        reasons.append("monthly_risk_limit_reached")
    if state.current_drawdown_percent >= profile.max_drawdown_percent:
        reasons.append("max_drawdown_reached")
    return reasons


def circuit_breaker(profile, state):
    reasons = risk_limits(profile, state)
    active = len(reasons) > 0
    return {"active": active, "reasons": reasons}


def recovery_mode(profile, state):
    if not profile.recovery_mode_enabled:
        return {"active": False, "risk_multiplier": 1.0, "reason": "disabled"}
    if state.current_drawdown_percent >= profile.max_drawdown_percent * 0.5:
        return {"active": True, "risk_multiplier": 0.5, "reason": "drawdown_recovery"}
    if state.daily_loss_percent >= profile.daily_risk_limit_percent * 0.6:
        return {"active": True, "risk_multiplier": 0.6, "reason": "daily_loss_recovery"}
    return {"active": False, "risk_multiplier": 1.0, "reason": "normal"}
