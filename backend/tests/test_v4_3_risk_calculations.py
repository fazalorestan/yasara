from app.v43_risk_engine import calculations as c

def test_v43_calculations():
    assert c.risk_amount(10000, 1) == 100
    assert c.position_size(10000, 1, 50000, 49000) > 0
    assert c.reward_risk(50000, 49000, 53000) == 3
    assert 0 <= c.kelly_fraction(0.55, 2) <= 1
