from app.v443_indicator_runtime_adapter.service import IndicatorRuntimeAdapterServiceV443

def test_v443_service():
    s = IndicatorRuntimeAdapterServiceV443()
    assert s.summary().ready is True
    assert s.run_sample()["ready"] is True
    assert s.runtime_contract()["execution_allowed"] is False
