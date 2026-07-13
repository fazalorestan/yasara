from app.platform_core.capabilities import CAPABILITIES, capability_registry
from app.platform_core.contracts.base import StandardAPIResponse
from app.platform_core.sdk.platform_sdk import platform_sdk
from app.platform_core.sdk_health import sdk_health_reporter
from app.platform_core.versioning import version_compatibility_checker
from app.v426_platform_contracts_sdk.models import PlatformContractsSDKSummaryV426

class PlatformContractsSDKServiceV426:
    def summary(self):
        return PlatformContractsSDKSummaryV426()

    def standard_response(self):
        return StandardAPIResponse(module="platform_contracts_sdk", data={"standard": True}).to_dict()

    def capabilities(self):
        return {"ready": True, "capabilities": CAPABILITIES, "registered": capability_registry.list()}

    def compatibility(self, plugin: str = "market_structure_pro"):
        return {"ready": True, "compatibility": version_compatibility_checker.check(plugin)}

    def sdk_health(self):
        sdk_health_reporter.set("platform_sdk", "healthy", "SDK foundation ready")
        return {"ready": True, "health": sdk_health_reporter.list()}

    def sdk_smoke(self):
        platform_sdk.increment_metric("sdk_smoke")
        platform_sdk.health("sdk_smoke", True, "SDK smoke test")
        event = platform_sdk.publish_event("SDKSmokeTest", {"ok": True})
        return {
            "ready": True,
            "event": event.name,
            "no_new_trading_features": True,
        }
