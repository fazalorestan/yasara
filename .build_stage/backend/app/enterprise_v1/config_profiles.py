from pydantic import BaseModel, Field

class ConfigProfileV1(BaseModel):
    profile_id: str
    name: str
    settings: dict = Field(default_factory=dict)

class ConfigProfileServiceV1:
    def merge(self, base: ConfigProfileV1, override: ConfigProfileV1) -> ConfigProfileV1:
        merged = base.settings.copy()
        merged.update(override.settings)
        return ConfigProfileV1(profile_id=base.profile_id, name=base.name, settings=merged)
