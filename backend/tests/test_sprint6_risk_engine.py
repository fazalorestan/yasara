from datetime import datetime, timezone
from app.decision_v1.domain.models import (
    ConfidenceBreakdown, DecisionClass, DecisionDirection, DecisionExplanation,
    DecisionObject, DecisionScores, DecisionWeights, SignalPlan
)
from app.risk_v1.domain.models import AccountSnapshot, RiskDecision
from app.risk_v1.engine.risk_engine import RiskIntelligenceEngineV1

def decision():
    return DecisionObject(
        exchange="binance_futures",
        symbol="BTC/USDT",
        direction=DecisionDirection.LONG,
        decision_class=DecisionClass.BUY,
        scores=DecisionScores(confidence=75, probability=70, quality=80, reliability=80, risk=50, reward=70),
        confidence_breakdown=ConfidenceBreakdown(),
        weights=DecisionWeights(),
        signal=SignalPlan(entry_zone_low=100, entry_zone_high=100, stop_loss=98, tp1=103, tp2=105, tp3=108),
        explanation=DecisionExplanation(summary="test"),
    )

def test_risk_engine_approves_normal_account():
    account = AccountSnapshot(equity=10000, daily_pnl=0, current_exposure=0)
    result = RiskIntelligenceEngineV1().assess(decision(), account)
    assert result.risk_decision in {RiskDecision.APPROVED, RiskDecision.REDUCED}
    assert result.position_size.quantity > 0

def test_risk_engine_rejects_daily_loss():
    account = AccountSnapshot(equity=10000, daily_pnl=-500)
    result = RiskIntelligenceEngineV1().assess(decision(), account)
    assert result.risk_decision == RiskDecision.REJECTED
