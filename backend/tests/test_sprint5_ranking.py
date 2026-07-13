from app.decision_v1.domain.models import DecisionObject, DecisionDirection, DecisionClass, DecisionScores, ConfidenceBreakdown, DecisionWeights, SignalPlan, DecisionExplanation
from app.decision_v1.engine.ranking import DecisionRankingEngineV1

def obj(symbol, score):
    return DecisionObject(
        exchange="binance_futures",
        symbol=symbol,
        direction=DecisionDirection.LONG,
        decision_class=DecisionClass.BUY,
        scores=DecisionScores(confidence=score, quality=score, reliability=score, reward=score),
        confidence_breakdown=ConfidenceBreakdown(),
        weights=DecisionWeights(),
        signal=SignalPlan(),
        explanation=DecisionExplanation(summary="test"),
        rank_score=score,
    )

def test_ranking_order():
    batch = DecisionRankingEngineV1().rank([obj("ETH/USDT", 50), obj("BTC/USDT", 90)])
    assert batch.decisions[0].decision.symbol == "BTC/USDT"
