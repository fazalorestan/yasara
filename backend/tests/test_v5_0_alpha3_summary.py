from app.v500_alpha3_indicator_sandbox.models import IndicatorSandboxSummaryV500Alpha3

def test_v500_alpha3_summary():
    s = IndicatorSandboxSummaryV500Alpha3()
    assert s.ready is True
    assert s.live_execution_enabled is False
