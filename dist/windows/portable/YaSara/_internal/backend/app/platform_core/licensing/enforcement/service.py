from app.platform_core.licensing.enforcement.audit import license_audit_event_publisher
from app.platform_core.licensing.enforcement.demo_limits import demo_limitation_enforcer
from app.platform_core.licensing.enforcement.feature_flag_bridge import license_feature_flag_bridge
from app.platform_core.licensing.enforcement.feature_gate import license_feature_gate
from app.platform_core.licensing.enforcement.plugin_guard import plugin_access_guard
from app.platform_core.licensing.enforcement.usage_counter import feature_usage_counter

class LicenseEnforcementService:
    def check_feature(self, payload: dict, feature: str):
        result = license_feature_gate.check(payload, feature)
        license_audit_event_publisher.publish("feature_check", payload)
        if result["allowed"]:
            feature_usage_counter.increment(feature)
        return result

    def build_flags(self, payload: dict):
        return license_feature_flag_bridge.build_flags(payload)

    def check_plugin(self, payload: dict, plugin: str):
        result = plugin_access_guard.can_use_plugin(payload, plugin)
        license_audit_event_publisher.publish("plugin_check", payload)
        return result

    def check_demo_usage(self, usage: dict):
        return demo_limitation_enforcer.check_usage(usage)

    def usage(self):
        return feature_usage_counter.snapshot()

license_enforcement_service = LicenseEnforcementService()
