from app.platform_core.config_center.profiles import environment_profile_registry
from app.platform_core.config_center.runtime_config import runtime_config_store
from app.platform_core.config_center.secrets import secret_reference_registry
from app.platform_core.config_center.versioning import config_version_registry
from app.platform_core.config_center.validation import config_validator

class ConfigSnapshotService:
    def snapshot(self):
        profiles = environment_profile_registry.seed_defaults()
        secrets = secret_reference_registry.seed_defaults()
        runtime = runtime_config_store.all()
        validation = config_validator.validate(runtime or {"live_execution_enabled": False, "debug": False})
        return {
            "ready": validation.valid,
            "profiles": profiles,
            "runtime": runtime,
            "secret_references": secrets,
            "versions": config_version_registry.history(),
            "validation": validation.__dict__,
            "mode": "report_only",
            "no_new_trading_features": True,
        }

config_snapshot_service = ConfigSnapshotService()
