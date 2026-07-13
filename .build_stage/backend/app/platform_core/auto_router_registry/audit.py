class AutoRouterRegistryAudit:
    def summarize(self, result: dict) -> dict:
        return {"ready": result.get("failed_count", 0) == 0, "discovered": result.get("discovered", 0), "registered_count": result.get("registered_count", 0), "skipped_count": result.get("skipped_count", 0), "failed_count": result.get("failed_count", 0)}

auto_router_registry_audit = AutoRouterRegistryAudit()
