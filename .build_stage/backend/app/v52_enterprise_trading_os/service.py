from __future__ import annotations

import os
import platform
import time
from typing import Any

from app.v52_enterprise_trading_os.models import MetricValue, TradingOSSnapshot, WorkspaceSnapshot


def _safe_import(path: str, attr: str) -> Any:
    try:
        module = __import__(path, fromlist=[attr])
        return getattr(module, attr)
    except Exception:
        return None


def _service_registry_report() -> dict[str, Any]:
    registry = _safe_import("app.platform_core.service_registry.container", "service_registry")
    if registry is None:
        return {"available": False, "registered_services": [], "instantiated_services": []}
    try:
        report = registry.report()
        report["available"] = True
        return report
    except Exception as exc:
        return {"available": False, "error": str(exc), "registered_services": [], "instantiated_services": []}


def _router_registry_report() -> dict[str, Any]:
    registry = _safe_import("app.platform_core.auto_router_registry.runtime_registry", "runtime_auto_router_registry")
    if registry is None:
        return {"available": False, "registered_count": 0, "failed_count": 0}
    return {
        "available": True,
        "registered_count": len(getattr(registry, "registered", [])),
        "failed_count": len(getattr(registry, "failed", [])),
        "registered": getattr(registry, "registered", []),
        "failed": getattr(registry, "failed", []),
    }


def _metric(key: str, label: str, value: Any, source: str) -> MetricValue:
    status = "ok" if value not in (None, "", [], {}) else "unavailable"
    return MetricValue(
        key=key,
        label=label,
        value=value,
        status=status,
        source=source,
        updated_at=time.time(),
    )


class EnterpriseTradingOSService:
    build_id = "2026.43.ENTERPRISE.001"

    def snapshot(self) -> TradingOSSnapshot:
        router_report = _router_registry_report()
        service_report = _service_registry_report()

        runtime = {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "pid": os.getpid(),
            "timestamp": time.time(),
        }

        trader = WorkspaceSnapshot(
            workspace="trader",
            metrics=[
                _metric("market_connection", "Market Connection", None, "market_data_runtime"),
                _metric("open_positions", "Open Positions", None, "portfolio_runtime"),
                _metric("daily_pnl", "Daily PnL", None, "portfolio_runtime"),
                _metric("risk_level", "Risk Level", None, "risk_engine"),
            ],
            panels={
                "chart": {"source": "market_data_runtime", "ready": False},
                "orders": {"source": "order_manager", "ready": False},
                "positions": {"source": "portfolio_runtime", "ready": False},
                "watchlist": {"source": "market_data_runtime", "ready": False},
            },
        )

        ai = WorkspaceSnapshot(
            workspace="ai",
            metrics=[
                _metric("ai_provider", "AI Provider", None, "ai_router"),
                _metric("confidence", "Confidence", None, "ai_decision_engine"),
                _metric("decision", "Decision", None, "ai_decision_engine"),
                _metric("latency", "Latency", None, "ai_router"),
            ],
            panels={
                "decision": {"source": "ai_decision_engine", "ready": False},
                "explainability": {"source": "ai_router", "ready": False},
                "signal_timeline": {"source": "event_bus", "ready": False},
                "provider_health": {"source": "ai_router", "ready": False},
            },
        )

        portfolio = WorkspaceSnapshot(
            workspace="portfolio",
            metrics=[
                _metric("equity", "Equity", None, "portfolio_engine"),
                _metric("drawdown", "Drawdown", None, "portfolio_engine"),
                _metric("exposure", "Exposure", None, "portfolio_engine"),
                _metric("allocation", "Allocation", None, "portfolio_engine"),
            ],
            panels={
                "allocation": {"source": "portfolio_engine", "ready": False},
                "performance": {"source": "portfolio_engine", "ready": False},
                "correlation": {"source": "portfolio_engine", "ready": False},
                "journal": {"source": "trading_journal", "ready": False},
            },
        )

        developer = WorkspaceSnapshot(
            workspace="developer",
            metrics=[
                _metric("registered_routes", "Registered Routes", router_report.get("registered_count"), "auto_router_registry"),
                _metric("failed_routes", "Failed Routes", router_report.get("failed_count"), "auto_router_registry"),
                _metric("registered_services", "Registered Services", len(service_report.get("registered_services", [])), "service_registry"),
                _metric("instantiated_services", "Instantiated Services", len(service_report.get("instantiated_services", [])), "service_registry"),
            ],
            panels={
                "auto_router_registry": router_report,
                "service_registry": service_report,
                "runtime": runtime,
                "build": {
                    "build_id": self.build_id,
                    "signal_only_default": True,
                    "auto_trading_enabled": False,
                },
            },
        )

        doctor = {
            "ready": router_report.get("failed_count", 0) == 0,
            "checks": {
                "auto_router_registry": router_report,
                "service_registry": service_report,
                "runtime": runtime,
            },
        }

        return TradingOSSnapshot(
            build_id=self.build_id,
            ready=True,
            real_data_only=True,
            mock_data=False,
            signal_only_default=True,
            auto_trading_enabled=False,
            workspaces=[trader, ai, portfolio, developer],
            doctor=doctor,
            runtime=runtime,
        )


enterprise_trading_os_service = EnterpriseTradingOSService()
