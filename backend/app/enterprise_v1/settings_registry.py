from pydantic import BaseModel, Field

class SettingDefinitionV1(BaseModel):
    key: str
    default: str | int | float | bool
    description: str = ""

class SettingsRegistryV1:
    def __init__(self):
        self.settings: dict[str, SettingDefinitionV1] = {}

    def register(self, setting: SettingDefinitionV1) -> SettingDefinitionV1:
        self.settings[setting.key] = setting
        return setting

    def get(self, key: str):
        return self.settings.get(key)
