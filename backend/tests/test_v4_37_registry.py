from app.platform_core.enterprise_queue.registry import QueueRegistry

def test_v437_registry():
    r = QueueRegistry()
    queues = r.seed_defaults()
    assert "default" in queues
    assert "diagnostics" in queues
