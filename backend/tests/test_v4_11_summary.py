from app.v411_smart_money_pro.service import SmartMoneyProServiceV411
def test_v411_summary():
    s=SmartMoneyProServiceV411().summary()
    assert s.ready is True
    assert s.constitution_compliant is True
