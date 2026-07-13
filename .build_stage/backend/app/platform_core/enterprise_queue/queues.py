from app.platform_core.enterprise_queue.memory_queue import MemoryQueue
from app.platform_core.enterprise_queue.models import QueueMessage

class QueueStore:
    def __init__(self):
        self.default = MemoryQueue()
        self.retry = MemoryQueue()
        self.dead_letter = MemoryQueue()

    def enqueue(self, message: QueueMessage):
        return self.default.push(message)

    def dequeue(self):
        return self.default.pop()

    def retry_message(self, message: QueueMessage):
        message.attempts += 1
        return self.retry.push(message)

    def dead_letter_message(self, message: QueueMessage):
        return self.dead_letter.push(message)

    def snapshot(self):
        return {
            "default": self.default.list(),
            "retry": self.retry.list(),
            "dead_letter": self.dead_letter.list(),
        }

queue_store = QueueStore()
