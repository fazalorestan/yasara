from app.v443_indicator_runtime_adapter.models import IndicatorRuntimeAdapterSummaryV443

def test_v443_summary():
    s = IndicatorRuntimeAdapterSummaryV443()
    assert s.ready is True
    assert s.indicator_name == "yasara"
    assert s.live_execution_enabled is False
