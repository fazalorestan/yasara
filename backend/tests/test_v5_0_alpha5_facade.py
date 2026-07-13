from app.v500_alpha5_indicator_release_gate.service import IndicatorReleaseGateFacadeV500Alpha5

def test_v500_alpha5_facade():
    f = IndicatorReleaseGateFacadeV500Alpha5()
    assert f.summary().ready is True
    assert f.full_report()["ready"] is True
