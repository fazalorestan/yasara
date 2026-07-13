from app.platform_core.config_center.models import ConfigProfile

class EnvironmentProfileRegistry:
    def __init__(self):
        self._profiles: dict[str, ConfigProfile] = {}

    def register(self, profile: ConfigProfile):
        self._profiles[profile.name] = profile
        return profile

    def get(self, name: str):
        return self._profiles.get(name)

    def list(self):
        return {k: v.__dict__ for k, v in self._profiles.items()}

    def seed_defaults(self):
        if self._profiles:
            return self.list()
        self.register(ConfigProfile(name="local", environment="local", values={
            "debug": True,
            "live_execution_enabled": False,
            "config_mode": "runtime_safe",
        }))
        self.register(ConfigProfile(name="production", environment="production", values={
            "debug": False,
            "live_execution_enabled": False,
            "config_mode": "production_safe",
        }))
        return self.list()

environment_profile_registry = EnvironmentProfileRegistry()
