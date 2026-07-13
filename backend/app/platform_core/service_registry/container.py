from __future__ import annotations

import threading
from dataclasses import dataclass
from typing import Any, Callable


@dataclass
class ServiceDefinition:
    key: str
    factory: Callable[[], Any]
    singleton: bool = True


class ServiceRegistry:
    def __init__(self) -> None:
        self._definitions: dict[str, ServiceDefinition] = {}
        self._singletons: dict[str, Any] = {}
        self._lock = threading.RLock()

    def register(self, key: str, factory: Callable[[], Any], singleton: bool = True) -> None:
        with self._lock:
            self._definitions[key] = ServiceDefinition(key, factory, singleton)

    def resolve(self, key: str) -> Any:
        with self._lock:
            if key not in self._definitions:
                raise KeyError(f"service_not_registered:{key}")
            definition = self._definitions[key]
            if not definition.singleton:
                return definition.factory()
            if key not in self._singletons:
                self._singletons[key] = definition.factory()
            return self._singletons[key]

    def has(self, key: str) -> bool:
        with self._lock:
            return key in self._definitions

    def clear_instances(self) -> None:
        with self._lock:
            self._singletons.clear()

    def report(self) -> dict[str, Any]:
        with self._lock:
            return {
                "registered_services": sorted(self._definitions),
                "instantiated_services": sorted(self._singletons),
                "lazy_initialization": True,
            }


service_registry = ServiceRegistry()
