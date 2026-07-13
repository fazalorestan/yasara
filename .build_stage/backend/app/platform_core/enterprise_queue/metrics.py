from app.platform_core.enterprise_queue.queues import queue_store

class QueueMetricsReporter:
    def report(self):
        return {
            "ready": True,
            "default_size": queue_store.default.size(),
            "retry_size": queue_store.retry.size(),
            "dead_letter_size": queue_store.dead_letter.size(),
            "mode": "report_only",
        }

queue_metrics_reporter = QueueMetricsReporter()
