from app.platform_core.ai_decision.safety import AIDecisionSafetyContract

def test_v500_alpha33_a_safety(): assert AIDecisionSafetyContract().policy()['auto_trading_allowed'] is False
