class DIContainerV1:
    def __init__(self):
        self._items = {}

    def register(self, key: str, value):
        self._items[key] = value
        return value

    def resolve(self, key: str):
        return self._items.get(key)

    def has(self, key: str) -> bool:
        return key in self._items
