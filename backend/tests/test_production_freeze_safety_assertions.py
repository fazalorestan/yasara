from app.production_freeze_v1.safety_assertions import ProductionSafetyAssertionsBuilderV1

def test_safety_assertions():
    safety = ProductionSafetyAssertionsBuilderV1().build()
    assert safety.passed is True
    assert any(a.key == "live_trading_disabled_by_default" for a in safety.assertions)
