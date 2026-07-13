from app.v500_alpha6_indicator_math.service import IndicatorMathFacadeV500Alpha6

def test_v500_alpha6_facade():
    f = IndicatorMathFacadeV500Alpha6()
    assert f.summary().ready is True
    assert f.calculate_sample()["ready"] is True
