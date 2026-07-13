class Scheduler:
    def __init__(self):
        self._tasks = {}
    def register(self, name, interval_seconds=60, enabled=True):
        self._tasks[name] = {"name": name, "interval_seconds": interval_seconds, "enabled": enabled}
        return self._tasks[name]
    def list(self):
        return list(self._tasks.values())

scheduler = Scheduler()
