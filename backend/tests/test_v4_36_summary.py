from app.v436_enterprise_scheduler.models import EnterpriseSchedulerSummaryV436

def test_v436_summary():
    s = EnterpriseSchedulerSummaryV436()
    assert s.ready is True
    assert s.no_new_trading_features is True
    assert s.live_execution_enabled is False
