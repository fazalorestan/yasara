from app.platform_core.enterprise_scheduler.status import TaskStatusRegistry

def test_v436_status():
    s = TaskStatusRegistry()
    item = s.mark_run("x")
    assert item.run_count == 1
    assert item.status == "completed"
