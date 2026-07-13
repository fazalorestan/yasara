from app.platform_core.enterprise_scheduler.scheduler import EnterpriseScheduler

def test_v436_scheduler():
    s = EnterpriseScheduler()
    assert s.seed()["ready"] is True
    assert s.run_once_report("diagnostics_snapshot")["ready"] is True
