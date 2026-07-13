from app.enterprise_v1.plugin_sdk import PluginSDKManifestV1, PluginSDKValidatorV1

def test_plugin_sdk_validator():
    assert PluginSDKValidatorV1().validate(PluginSDKManifestV1(plugin_id="p1", name="Demo")) is True
