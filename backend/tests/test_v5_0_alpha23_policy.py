from app.platform_core.risk_engine.policy import RiskPolicyProvider

def test_v500_alpha23_policy():
    p=RiskPolicyProvider().default_policy(); assert p['max_risk_per_trade_pct'] == 1.0; assert p['auto_trading_allowed'] is False
