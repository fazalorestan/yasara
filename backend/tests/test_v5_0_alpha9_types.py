from app.platform_core.licensing.types import license_types
def test_v500_alpha9_types():
    assert "demo" in license_types.all()
    assert "enterprise" in license_types.all()
