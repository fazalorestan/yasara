from app.platform_core.api_routing.health import auto_router_health_report

class AutoRouterReadinessGate:
    def run(self):
        report = auto_router_health_report.report()
        return {
            "ready": report["ready"],
            "score": 100.0 if report["ready"] else 0.0,
            "report": report,
            "execution_allowed": False,
            "mode": "auto_router_discovery_foundation",
        }

auto_router_readiness_gate = AutoRouterReadinessGate()
