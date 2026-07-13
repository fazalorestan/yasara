from app.v500_alpha8_signal_logic_expansion.models import SignalLogicExpansionSummaryV500Alpha8
def test_v500_alpha8_summary():
    s = SignalLogicExpansionSummaryV500Alpha8()
    assert s.ready is True
    assert s.test_pack_size == 20
