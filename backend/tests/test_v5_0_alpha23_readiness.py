from app.platform_core.risk_engine.readiness import RiskEngineReadinessGate

def test_v500_alpha23_readiness():
    r=RiskEngineReadinessGate().run(); assert r['ready'] is True; assert r['execution_allowed'] is False
