from time import perf_counter

class StartupProfiler:
    def __init__(self):
        self._startup = {}

    def measure(self, plugin: str, fn=None):
        start = perf_counter()
        result = fn() if fn else None
        elapsed = round((perf_counter() - start) * 1000, 4)
        self._startup[plugin] = elapsed
        return {"plugin": plugin, "startup_ms": elapsed, "result": result}

    def set(self, plugin: str, startup_ms: float):
        self._startup[plugin] = float(startup_ms)

    def report(self):
        return dict(self._startup)

startup_profiler = StartupProfiler()
