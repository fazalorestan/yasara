class AIMemoryStore:
    def __init__(self):
        self._items = []

    def put(self, key: str = "sample", value: str = "memory"):
        item = {"key": key, "value": value, "scope": "yasara_owned"}
        self._items.append(item)
        return {"ready": True, "stored": True, "item": item}

    def list_items(self):
        if not self._items:
            self.put()
        return {"ready": True, "items": list(self._items), "count": len(self._items)}

ai_memory_store = AIMemoryStore()
