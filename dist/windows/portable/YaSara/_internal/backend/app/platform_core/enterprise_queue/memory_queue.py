from app.platform_core.enterprise_queue.models import QueueMessage

class MemoryQueue:
    def __init__(self):
        self._items: list[QueueMessage] = []

    def push(self, message: QueueMessage):
        self._items.append(message)
        self._items.sort(key=lambda m: m.priority)
        return message

    def pop(self):
        return self._items.pop(0) if self._items else None

    def size(self):
        return len(self._items)

    def list(self):
        return [m.__dict__ for m in self._items]
