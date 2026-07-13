from uuid import uuid4
from app.platform_core.enterprise_queue.metrics import queue_metrics_reporter
from app.platform_core.enterprise_queue.models import QueueMessage
from app.platform_core.enterprise_queue.queues import queue_store
from app.platform_core.enterprise_queue.registry import queue_registry
from app.platform_core.enterprise_queue.workers import worker_contract_registry

class EnterpriseQueueService:
    def seed(self):
        return {
            "ready": True,
            "queues": queue_registry.seed_defaults(),
            "workers": worker_contract_registry.seed_defaults(),
            "mode": "report_only",
        }

    def enqueue_report(self, topic: str = "diagnostics", payload: dict | None = None, priority: int = 5):
        message = QueueMessage(id=str(uuid4()), topic=topic, payload=payload or {}, priority=priority)
        queue_store.enqueue(message)
        return {"ready": True, "message": message.__dict__, "executed": False, "mode": "report_only"}

    def dequeue_report(self):
        message = queue_store.dequeue()
        return {"ready": True, "message": message.__dict__ if message else None, "executed": False, "mode": "report_only"}

    def snapshot(self):
        return {"ready": True, "snapshot": queue_store.snapshot(), "mode": "report_only"}

    def metrics(self):
        return queue_metrics_reporter.report()

enterprise_queue_service = EnterpriseQueueService()
