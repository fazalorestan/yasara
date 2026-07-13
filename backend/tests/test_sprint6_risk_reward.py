from app.decision_v1.domain.models import DecisionDirection, SignalPlan
from app.risk_v1.engine.risk_reward import RiskRewardEngineV1

def test_risk_reward_long_valid():
    signal = SignalPlan(entry_zone_low=100, entry_zone_high=100, stop_loss=98, tp1=103, tp2=105, tp3=108)
    rr = RiskRewardEngineV1().validate(DecisionDirection.LONG, signal, 1.5)
    assert rr.valid is True
    assert rr.rr_tp1 == 1.5

def test_risk_reward_short_valid():
    signal = SignalPlan(entry_zone_low=100, entry_zone_high=100, stop_loss=102, tp1=97, tp2=95, tp3=92)
    rr = RiskRewardEngineV1().validate(DecisionDirection.SHORT, signal, 1.5)
    assert rr.valid is True
    assert rr.rr_tp1 == 1.5
