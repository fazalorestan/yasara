from app.v35_smart_money.service import SmartMoneyEngineServiceV35

def test_v35_summary():
    s = SmartMoneyEngineServiceV35().summary()
    assert s.product_progress_percent == 78
    assert s.constitution_compliant is True
