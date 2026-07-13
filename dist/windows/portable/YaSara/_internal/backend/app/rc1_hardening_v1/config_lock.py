from pydantic import BaseModel, Field

class ConfigLockItemV1(BaseModel):
    key: str
    locked: bool = True

class ConfigLockManifestV1(BaseModel):
    items: list[ConfigLockItemV1] = Field(default_factory=list)

class ConfigLockBuilderV1:
    def build(self) -> ConfigLockManifestV1:
        return ConfigLockManifestV1(items=[
            ConfigLockItemV1(key="LIVE_TRADING_ENABLED"),
            ConfigLockItemV1(key="TELEMETRY_ENABLED"),
            ConfigLockItemV1(key="SECRET_STORAGE_MODE"),
            ConfigLockItemV1(key="DATABASE_URL", locked=False),
        ])
