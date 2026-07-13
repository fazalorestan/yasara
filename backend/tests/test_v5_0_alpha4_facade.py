from app.v500_alpha4_indicator_lifecycle.service import IndicatorLifecycleFacadeV500Alpha4

def test_v500_alpha4_facade():
    f = IndicatorLifecycleFacadeV500Alpha4()
    assert f.summary().ready is True
    assert f.states()["ready"] is True
    assert f.contract()["execution_allowed"] is False
