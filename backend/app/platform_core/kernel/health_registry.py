class HealthRegistry:
    def __init__(self):
        self._items = {}
    def set(self, name, ready, detail=""):
        self._items[name] = {"name": name, "ready": bool(ready), "detail": detail}
        return self._items[name]
    def summary(self):
        items = list(self._items.values())
        return {"ready": all(i["ready"] for i in items) if items else True, "count": len(items), "items": items}

health_registry = HealthRegistry()
