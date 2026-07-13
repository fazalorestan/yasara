from app.platform_core.indicators.sandbox.manifest_validator import IndicatorManifestValidator

def test_v500_alpha3_manifest_validator():
    v = IndicatorManifestValidator()
    assert v.validate({"name":"x","version":"v1","display_name":"X","capabilities":[]})["valid"] is True
    assert v.validate({"name":"x"})["valid"] is False
