from app.enterprise_v1.settings_registry import SettingDefinitionV1, SettingsRegistryV1

def test_settings_registry():
    registry = SettingsRegistryV1()
    registry.register(SettingDefinitionV1(key="theme", default="dark"))
    assert registry.get("theme").default == "dark"
