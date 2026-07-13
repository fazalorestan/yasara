from app.v11_strategy_runtime.models import StrategyConditionTypeV11, StrategyConditionV11, StrategyContextV11
from app.v11_strategy_runtime.rule_engine import StrategyRuleEngineV11

def test_strategy_condition_matches():
    engine = StrategyRuleEngineV11()
    ctx = StrategyContextV11(symbol="BTCUSDT", price=200, ai_score=0.8, risk_allowed=True)
    cond = StrategyConditionV11(condition_type=StrategyConditionTypeV11.PRICE_ABOVE, symbol="BTCUSDT", value=100)
    assert engine.condition_matches(cond, ctx) is True
