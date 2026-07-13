from app.platform_core.config_center.profiles import environment_profile_registry
from app.platform_core.config_center.runtime_config import runtime_config_store
from app.platform_core.config_center.secrets import secret_reference_registry
from app.platform_core.config_center.snapshot import config_snapshot_service
from app.platform_core.config_center.validation import config_validator
from app.platform_core.config_center.versioning import config_version_registry
from app.v435_configuration_center.models import ConfigurationCenterSummaryV435

class ConfigurationCenterServiceV435:
    def summary(self):
        return ConfigurationCenterSummaryV435()

    def profiles(self):
        return {"ready": True, "profiles": environment_profile_registry.seed_defaults()}

    def runtime(self):
        return {"ready": True, "runtime": runtime_config_store.all()}

    def set_runtime(self, key: str, value):
        return {"ready": True, "item": runtime_config_store.set(key, value)}

    def validate(self):
        result = config_validator.validate(runtime_config_store.all() or {"live_execution_enabled": False, "debug": False})
        return {"ready": result.valid, "validation": result.__dict__}

    def secrets(self):
        return {"ready": True, "secrets": secret_reference_registry.seed_defaults()}

    def commit(self, label: str = "manual"):
        return {"ready": True, "version": config_version_registry.commit(label, runtime_config_store.all())}

    def snapshot(self):
        return config_snapshot_service.snapshot()
