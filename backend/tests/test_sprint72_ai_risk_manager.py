from app.ai_trading_v1.risk_manager import AIRiskInputV1, AIRiskManagerV1

def test_ai_risk_manager_blocks_critical():
    result = AIRiskManagerV1().evaluate(AIRiskInputV1(signal_confidence=20, volatility_percent=20, portfolio_risk_score=50))
    assert result.approved is False
    assert result.recommendation == "block_trade"
