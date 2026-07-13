from app.v500_alpha7_runtime_signal_logic.models import RuntimeSignalLogicSummaryV500Alpha7

def test_v500_alpha7_summary():
    s = RuntimeSignalLogicSummaryV500Alpha7()
    assert s.ready is True
    assert s.live_execution_enabled is False
