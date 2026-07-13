from app.v11_risk_control.risk_config import RiskConfigServiceV11

def test_risk_config_rules():
    rules = RiskConfigServiceV11().rules()
    assert any(rule.key == "max_order_notional" for rule in rules)
    assert any(rule.key == "live_trading_disabled" for rule in rules)
