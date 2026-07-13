from app.v433_operations_runbook.models import OperationsRunbookSummaryV433

def test_v433_summary():
    s = OperationsRunbookSummaryV433()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
