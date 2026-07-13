from app.platform_core.kernel.event_bus import PlatformEvent, event_bus
from app.platform_core.kernel.plugin_registry import PluginManifest, plugin_registry
from app.platform_core.kernel.service_registry import service_registry
from app.platform_core.kernel.configuration import configuration_manager
from app.platform_core.kernel.health_registry import health_registry
from app.platform_core.governance.feature_flags import feature_flag_center
from app.platform_core.governance.metrics import metrics
from app.platform_core.governance.audit_log import audit_log

class PlatformSDK:
    def register_plugin(self, manifest: PluginManifest):
        return plugin_registry.register(manifest)

    def publish_event(self, name: str, payload: dict | None = None, source: str = "plugin_sdk"):
        return event_bus.publish(PlatformEvent(name=name, payload=payload or {}, source=source))

    def subscribe_event(self, name: str, handler):
        return event_bus.subscribe(name, handler)

    def get_service(self, name: str):
        return service_registry.get(name)

    def get_config(self, key: str, default=None):
        return configuration_manager.get(key, default)

    def get_feature(self, name: str):
        return feature_flag_center.is_enabled(name)

    def log(self, action: str, payload: dict | None = None):
        return audit_log.write(action=action, actor="platform_sdk", payload=payload or {})

    def increment_metric(self, name: str, amount: int = 1):
        return metrics.increment(name, amount)

    def health(self, name: str, ready: bool, detail: str = ""):
        return health_registry.set(name, ready, detail)

platform_sdk = PlatformSDK()
