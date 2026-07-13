from app.platform_core.auto_router_lazy_service_registry.report import auto_router_lazy_service_registry_report_service

class AutoRouterLazyServiceRegistryReadinessGate:
    def run(self):
        r = auto_router_lazy_service_registry_report_service.report()
        return {"ready": r["ready"] and r["auto_router_registry"] and r["lazy_initialization"] and r["service_registry"] and not r["auto_trading_enabled"], "checks": r}

auto_router_lazy_service_registry_readiness_gate = AutoRouterLazyServiceRegistryReadinessGate()
