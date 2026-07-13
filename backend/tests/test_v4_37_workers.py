from app.platform_core.enterprise_queue.workers import WorkerContractRegistry

def test_v437_workers():
    r = WorkerContractRegistry()
    workers = r.seed_defaults()
    assert "diagnostics_worker" in workers
