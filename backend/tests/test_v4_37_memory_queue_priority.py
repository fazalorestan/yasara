from app.platform_core.enterprise_queue.memory_queue import MemoryQueue
from app.platform_core.enterprise_queue.models import QueueMessage

def test_v437_memory_queue_priority():
    q = MemoryQueue()
    q.push(QueueMessage(id="b", topic="x", priority=9))
    q.push(QueueMessage(id="a", topic="x", priority=1))
    assert q.pop().id == "a"
