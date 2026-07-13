from app.v500_alpha8_signal_logic_expansion.service import SignalLogicExpansionFacadeV500Alpha8
def test_v500_alpha8_facade():
    f = SignalLogicExpansionFacadeV500Alpha8()
    assert f.summary().ready is True
    assert f.evaluate_sample()["ready"] is True
