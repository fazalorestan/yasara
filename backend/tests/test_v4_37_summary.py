from app.v437_enterprise_queue.models import EnterpriseQueueSummaryV437

def test_v437_summary():
    s = EnterpriseQueueSummaryV437()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
