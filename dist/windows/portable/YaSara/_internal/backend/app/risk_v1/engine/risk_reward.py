from app.decision_v1.domain.models import DecisionDirection, SignalPlan
from app.risk_v1.domain.models import RiskRewardValidation

class RiskRewardEngineV1:
    def validate(self, direction: DecisionDirection, signal: SignalPlan, min_rr: float) -> RiskRewardValidation:
        entry = self._entry(signal)
        if direction not in {DecisionDirection.LONG, DecisionDirection.SHORT}:
            return RiskRewardValidation(valid=False, reason="No directional decision.")
        if entry is None or signal.stop_loss is None:
            return RiskRewardValidation(valid=False, reason="Entry or stop loss missing.")

        risk = abs(entry - signal.stop_loss)
        if risk <= 0:
            return RiskRewardValidation(valid=False, reason="Invalid stop distance.")

        rr_tp1 = self._rr(direction, entry, signal.tp1, risk)
        rr_tp2 = self._rr(direction, entry, signal.tp2, risk)
        rr_tp3 = self._rr(direction, entry, signal.tp3, risk)
        best = max([x for x in [rr_tp1, rr_tp2, rr_tp3] if x is not None], default=0)
        return RiskRewardValidation(
            rr_tp1=rr_tp1,
            rr_tp2=rr_tp2,
            rr_tp3=rr_tp3,
            valid=best >= min_rr,
            reason="Risk/reward accepted." if best >= min_rr else f"Best RR {best:.2f} below minimum {min_rr:.2f}.",
        )

    def _entry(self, signal: SignalPlan) -> float | None:
        if signal.entry_zone_low is None or signal.entry_zone_high is None:
            return None
        return (signal.entry_zone_low + signal.entry_zone_high) / 2

    def _rr(self, direction: DecisionDirection, entry: float, tp: float | None, risk: float) -> float | None:
        if tp is None:
            return None
        reward = (tp - entry) if direction == DecisionDirection.LONG else (entry - tp)
        return reward / risk
