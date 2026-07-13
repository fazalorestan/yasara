from app.v500_alpha7_runtime_signal_logic.service import RuntimeSignalLogicFacadeV500Alpha7

def test_v500_alpha7_facade():
    f = RuntimeSignalLogicFacadeV500Alpha7()
    assert f.summary().ready is True
    assert f.evaluate_sample()["ready"] is True
