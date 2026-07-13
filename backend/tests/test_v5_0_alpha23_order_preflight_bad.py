from app.platform_core.risk_engine.order_preflight import OrderRiskPreflight

def test_v500_alpha23_order_preflight_bad():
    r=OrderRiskPreflight().check({'daily_loss_pct':4,'drawdown_pct':2,'symbol_exposure_pct':10,'portfolio_exposure_pct':30}); assert r['allowed'] is False
