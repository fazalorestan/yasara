class Metrics:
    def __init__(self):
        self._counters = {}
    def increment(self, name, amount=1):
        self._counters[name] = self._counters.get(name, 0) + amount
        return self._counters[name]
    def snapshot(self):
        return dict(self._counters)

metrics = Metrics()
