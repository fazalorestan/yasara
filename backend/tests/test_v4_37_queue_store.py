from app.platform_core.enterprise_queue.models import QueueMessage
from app.platform_core.enterprise_queue.queues import QueueStore

def test_v437_queue_store():
    s = QueueStore()
    m = QueueMessage(id="1", topic="t")
    s.enqueue(m)
    assert s.dequeue().id == "1"
    s.retry_message(m)
    assert s.retry.size() == 1
    s.dead_letter_message(m)
    assert s.dead_letter.size() == 1
