from app.platform_core.risk_engine.order_preflight import OrderRiskPreflight

def test_v500_alpha23_order_preflight_ok():
    r=OrderRiskPreflight().check({'daily_loss_pct':1,'drawdown_pct':2,'symbol_exposure_pct':10,'portfolio_exposure_pct':30}); assert r['allowed'] is True; assert r['execution_allowed'] is False
