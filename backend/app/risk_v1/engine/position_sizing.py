from app.decision_v1.domain.models import DecisionObject, DecisionDirection
from app.risk_v1.domain.models import AccountSnapshot, PositionSize, PositionSizingMethod, RiskLimits

class PositionSizingEngineV1:
    def fixed_fractional(self, account: AccountSnapshot, decision: DecisionObject, limits: RiskLimits) -> PositionSize:
        entry = self._entry(decision)
        stop = decision.signal.stop_loss
        if entry is None or stop is None or account.equity <= 0:
            return PositionSize(method=PositionSizingMethod.FIXED_FRACTIONAL, quantity=0, notional=0, risk_amount=0, risk_pct=0)
        risk_amount = account.equity * limits.max_risk_per_trade_pct / 100
        stop_distance = abs(entry - stop)
        quantity = risk_amount / stop_distance if stop_distance > 0 else 0
        notional = quantity * entry
        leverage = min(limits.max_leverage, max(1.0, decision.scores.confidence / 20))
        return PositionSize(
            method=PositionSizingMethod.FIXED_FRACTIONAL,
            quantity=max(0, quantity),
            notional=max(0, notional),
            risk_amount=risk_amount,
            risk_pct=limits.max_risk_per_trade_pct,
            leverage=leverage,
            margin_required=notional / leverage if leverage else notional,
        )

    def confidence_adjusted(self, account: AccountSnapshot, decision: DecisionObject, limits: RiskLimits, adjustment_factor: float = 1.0) -> PositionSize:
        base = self.fixed_fractional(account, decision, limits)
        confidence_factor = max(0.25, min(1.25, decision.scores.confidence / 80))
        factor = confidence_factor * adjustment_factor
        return base.model_copy(update={
            "method": PositionSizingMethod.CONFIDENCE_ADJUSTED,
            "quantity": base.quantity * factor,
            "notional": base.notional * factor,
            "risk_amount": base.risk_amount * factor,
            "risk_pct": base.risk_pct * factor,
            "margin_required": base.margin_required * factor,
        })

    def _entry(self, decision: DecisionObject) -> float | None:
        low = decision.signal.entry_zone_low
        high = decision.signal.entry_zone_high
        if low is None or high is None:
            return None
        return (low + high) / 2
