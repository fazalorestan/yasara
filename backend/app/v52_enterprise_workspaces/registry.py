from collections import OrderedDict
from threading import RLock
from app.v52_enterprise_workspaces.models import WorkspaceDescriptor

class WorkspaceRegistry:
    def __init__(self):
        self._items = OrderedDict()
        self._lock = RLock()

    def register(self, descriptor: WorkspaceDescriptor):
        with self._lock:
            self._items[descriptor.id] = descriptor
            self._items = OrderedDict(sorted(self._items.items(), key=lambda item: item[1].order))

    def get(self, workspace_id: str):
        with self._lock:
            return self._items.get(workspace_id)

    def list(self):
        with self._lock:
            return list(self._items.values())

    def report(self):
        with self._lock:
            return {"registered_count": len(self._items), "workspace_ids": list(self._items.keys())}

workspace_registry = WorkspaceRegistry()
