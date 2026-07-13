from app.v436_enterprise_scheduler.service import EnterpriseSchedulerServiceV436

def test_v436_service():
    s = EnterpriseSchedulerServiceV436()
    assert s.summary().ready is True
    assert s.tasks()["ready"] is True
    assert s.metrics()["ready"] is True
