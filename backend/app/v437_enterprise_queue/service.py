from app.platform_core.enterprise_queue.service import enterprise_queue_service
from app.v437_enterprise_queue.models import EnterpriseQueueSummaryV437

class EnterpriseQueueFacadeV437:
    def summary(self):
        return EnterpriseQueueSummaryV437()

    def seed(self):
        return enterprise_queue_service.seed()

    def enqueue(self, topic: str = "diagnostics", payload: dict | None = None, priority: int = 5):
        return enterprise_queue_service.enqueue_report(topic, payload, priority)

    def dequeue(self):
        return enterprise_queue_service.dequeue_report()

    def snapshot(self):
        return enterprise_queue_service.snapshot()

    def metrics(self):
        return enterprise_queue_service.metrics()
