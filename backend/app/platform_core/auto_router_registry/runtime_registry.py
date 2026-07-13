from __future__ import annotations

import importlib
import json
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from fastapi import APIRouter


SKIP_MODULES = {"__init__", "health"}


@dataclass
class RuntimeAutoRouterRegistry:
    registered: list[dict[str, Any]] = field(default_factory=list)
    failed: list[dict[str, Any]] = field(default_factory=list)

    def discover_route_modules(self) -> list[str]:
        # BUGFIX: this file lives at app/platform_core/auto_router_registry/
        # runtime_registry.py. parents[2] is "app"; the routes package is
        # app/api/v1/routes. The previous parents[3] pointed one level too
        # high (the repo root, sibling to "app"), so routes_dir.exists()
        # was always False and NOTHING was ever auto-registered, no matter
        # how many router modules existed on disk.
        routes_dir = Path(__file__).resolve().parents[2] / "api" / "v1" / "routes"
        modules: list[str] = []
        if routes_dir.exists():
            for file in sorted(routes_dir.glob("*.py")):
                stem = file.stem
                if stem not in SKIP_MODULES:
                    modules.append(f"app.api.v1.routes.{stem}")
        return modules

    def register_all(self, api_router: APIRouter) -> dict[str, Any]:
        started = time.time()
        self.registered.clear()
        self.failed.clear()

        for module_name in self.discover_route_modules():
            self._register_one(api_router, module_name)

        result = {
            "ready": True,
            "registered_count": len(self.registered),
            "failed_count": len(self.failed),
            "registered": self.registered,
            "failed": self.failed,
            "duration_ms": round((time.time() - started) * 1000, 2),
            "mode": "isolated_auto_router_registry",
        }
        self._write_report(result)
        return result

    def _register_one(self, api_router: APIRouter, module_name: str) -> None:
        started = time.time()
        try:
            module = importlib.import_module(module_name)
            router = getattr(module, "router", None)
            if router is None:
                self.failed.append({"module": module_name, "error": "missing_router"})
                return
            api_router.include_router(router)
            self.registered.append({
                "module": module_name,
                "status": "ok",
                "duration_ms": round((time.time() - started) * 1000, 2),
            })
        except Exception as exc:
            self.failed.append({
                "module": module_name,
                "error": str(exc),
                "traceback": traceback.format_exc()[-4000:],
                "duration_ms": round((time.time() - started) * 1000, 2),
            })

    def _write_report(self, result: dict[str, Any]) -> None:
        for root in [Path.cwd(), Path.cwd().parent]:
            try:
                reports = root / "runtime_reports"
                reports.mkdir(parents=True, exist_ok=True)
                (reports / "auto_router_registry_report.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
                return
            except Exception:
                continue


runtime_auto_router_registry = RuntimeAutoRouterRegistry()
