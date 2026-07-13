from app.platform_core.auto_router_registry.service import auto_router_registry_service

class AutoRouterRegistryReadinessGate:
    def run(self):
        discovery = auto_router_registry_service.discover()
        contract = auto_router_registry_service.contract()
        return {"ready": discovery["ready"] and contract["ready"], "checks": {"discovery_ready": discovery["ready"], "contract_ready": contract["ready"], "manual_router_patch_required_after_this": False, "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

auto_router_registry_readiness_gate = AutoRouterRegistryReadinessGate()
