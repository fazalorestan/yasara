from app.enterprise_v1.config_profiles import ConfigProfileServiceV1, ConfigProfileV1

def test_config_profile_merge():
    merged = ConfigProfileServiceV1().merge(ConfigProfileV1(profile_id="p", name="base", settings={"a": 1}), ConfigProfileV1(profile_id="o", name="override", settings={"b": 2}))
    assert merged.settings["a"] == 1 and merged.settings["b"] == 2
