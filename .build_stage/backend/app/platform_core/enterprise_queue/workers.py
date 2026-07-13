from app.platform_core.enterprise_queue.models import WorkerContract

class WorkerContractRegistry:
    def __init__(self):
        self._workers: dict[str, WorkerContract] = {}

    def register(self, worker: WorkerContract):
        self._workers[worker.name] = worker
        return worker

    def list(self):
        return {k: v.__dict__ for k, v in self._workers.items()}

    def seed_defaults(self):
        if not self._workers:
            self.register(WorkerContract(name="diagnostics_worker", queue="diagnostics"))
            self.register(WorkerContract(name="notification_worker", queue="notifications"))
            self.register(WorkerContract(name="plugin_event_worker", queue="plugin_events"))
        return self.list()

worker_contract_registry = WorkerContractRegistry()
