from app.platform_core.indicators.release_gate.rc_contract import IndicatorReleaseCandidateContract

def test_v500_alpha5_rc_contract():
    c = IndicatorReleaseCandidateContract().contract()
    assert c["ready"] is True
    assert c["execution_allowed"] is False
