from app.v500_alpha3_indicator_sandbox.service import IndicatorSandboxFacadeV500Alpha3

def test_v500_alpha3_facade():
    f = IndicatorSandboxFacadeV500Alpha3()
    assert f.summary().ready is True
    assert f.install_gate()["ready"] is True
