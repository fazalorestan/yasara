from app.v52_dashboard_provider_hub.models import ApprovedDashboardSnapshot, ProviderState

def _safe_import(path, attr):
    try:
        module = __import__(path, fromlist=[attr])
        return getattr(module, attr)
    except Exception:
        return None

class DashboardProviderHub:
    def snapshot(self):
        providers = []
        ai = _safe_import("app.v52_ai_decision_engine.service", "ai_decision_facade")
        if ai is None:
            providers.append(ProviderState(name="ai", available=False, source="ai_decision_core", error="provider_unavailable"))
            ai_payload = {}
        else:
            try:
                timeline = ai.timeline(1)
                ai_payload = timeline[0] if timeline else {}
                providers.append(ProviderState(name="ai", available=True, source="ai_decision_core", payload=ai_payload))
            except Exception as exc:
                ai_payload = {}
                providers.append(ProviderState(name="ai", available=False, source="ai_decision_core", error=str(exc)))

        router = _safe_import("app.platform_core.auto_router_registry.runtime_registry", "runtime_auto_router_registry")
        dev_payload = {
            "registered_routes": len(getattr(router, "registered", [])) if router else None,
            "failed_routes": len(getattr(router, "failed", [])) if router else None,
        }
        providers.append(ProviderState(name="developer", available=router is not None, source="auto_router_registry", payload=dev_payload))

        widgets = {
            "ai_decision": ai_payload.get("decision"),
            "ai_confidence": ai_payload.get("confidence"),
            "signal_quality": ai_payload.get("quality_score"),
            "registered_routes": dev_payload.get("registered_routes"),
            "failed_routes": dev_payload.get("failed_routes"),
            "market": None,
            "portfolio": None,
            "risk": None,
            "orders": None,
            "positions": None,
            "watchlist": None,
        }
        return ApprovedDashboardSnapshot(providers=providers, widgets=widgets)

dashboard_provider_hub = DashboardProviderHub()
