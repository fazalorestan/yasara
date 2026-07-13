from app.platform_core.enterprise_queue.models import QueueDefinition

class QueueRegistry:
    def __init__(self):
        self._queues: dict[str, QueueDefinition] = {}

    def register(self, queue: QueueDefinition):
        self._queues[queue.name] = queue
        return queue

    def get(self, name: str):
        return self._queues.get(name)

    def list(self):
        return {k: v.__dict__ for k, v in self._queues.items()}

    def seed_defaults(self):
        if not self._queues:
            self.register(QueueDefinition(name="default"))
            self.register(QueueDefinition(name="plugin_events"))
            self.register(QueueDefinition(name="notifications"))
            self.register(QueueDefinition(name="diagnostics"))
        return self.list()

queue_registry = QueueRegistry()
