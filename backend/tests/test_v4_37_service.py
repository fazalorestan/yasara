from app.platform_core.enterprise_queue.service import EnterpriseQueueService

def test_v437_service():
    s = EnterpriseQueueService()
    assert s.seed()["ready"] is True
    assert s.enqueue_report()["ready"] is True
    assert s.metrics()["ready"] is True
