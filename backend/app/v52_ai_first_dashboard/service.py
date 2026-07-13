from __future__ import annotations
import time
from typing import Any
from app.v52_ai_first_dashboard.models import (
    AIFirstDashboardSnapshot,
    DashboardMetric,
    DashboardSection,
)

def _safe_import(path: str, attr: str) -> Any:
    try:
        module = __import__(path, fromlist=[attr])
        return getattr(module, attr)
    except Exception:
        return None

def _metric(key: str, label: str, value: Any, source: str) -> DashboardMetric:
    return DashboardMetric(
        key=key,
        label=label,
        value=value,
        status="ok" if value not in (None, "", [], {}) else "unavailable",
        source=source,
        updated_at=time.time(),
    )

class AIFirstDashboardService:
    build_id = "2026.45.ENTERPRISE.001"

    def _ai_decision(self):
        facade = _safe_import("app.v52_ai_decision_engine.service", "ai_decision_facade")
        if facade is None:
            return None
        try:
            timeline = facade.timeline(1)
            return timeline[0] if timeline else None
        except Exception:
            return None

    def _developer_health(self):
        registry = _safe_import(
            "app.platform_core.auto_router_registry.runtime_registry",
            "runtime_auto_router_registry",
        )
        if registry is None:
            return None
        return {
            "registered_routes": len(getattr(registry, "registered", [])),
            "failed_routes": len(getattr(registry, "failed", [])),
        }

    def snapshot(self) -> AIFirstDashboardSnapshot:
        ai = self._ai_decision()
        developer = self._developer_health()

        metrics = [
            _metric("ai_decision", "AI Decision", (ai or {}).get("decision"), "ai_decision_core"),
            _metric("ai_confidence", "AI Confidence", (ai or {}).get("confidence"), "ai_decision_core"),
            _metric("signal_quality", "Signal Quality", (ai or {}).get("quality_score"), "ai_decision_core"),
            _metric("risk", "Risk", None, "risk_engine"),
            _metric("equity", "Equity", None, "portfolio_engine"),
            _metric("open_positions", "Open Positions", None, "portfolio_engine"),
        ]

        sections = [
            DashboardSection(
                key="ai_signal_matrix",
                title="AI Signal Matrix",
                status="ok" if ai else "unavailable",
                source="ai_decision_core",
                payload=ai or {},
            ),
            DashboardSection(
                key="confirmations",
                title="Confirmations",
                status="unavailable",
                source="ai_decision_core",
                payload={},
            ),
            DashboardSection(
                key="market_chart",
                title="Market Chart",
                status="unavailable",
                source="market_data_runtime",
                payload={},
            ),
            DashboardSection(
                key="risk_engine",
                title="Risk Engine",
                status="unavailable",
                source="risk_engine",
                payload={},
            ),
            DashboardSection(
                key="portfolio",
                title="Portfolio",
                status="unavailable",
                source="portfolio_engine",
                payload={},
            ),
            DashboardSection(
                key="developer_health",
                title="Developer Health",
                status="ok" if developer else "unavailable",
                source="auto_router_registry",
                payload=developer or {},
            ),
        ]

        doctor = {
            "ready": True,
            "real_data_only": True,
            "checks": {
                "ai_decision": ai is not None,
                "auto_router_registry": developer is not None,
                "market_data": False,
                "risk_engine": False,
                "portfolio_engine": False,
            },
        }

        return AIFirstDashboardSnapshot(
            metrics=metrics,
            sections=sections,
            doctor=doctor,
        )

ai_first_dashboard_service = AIFirstDashboardService()
