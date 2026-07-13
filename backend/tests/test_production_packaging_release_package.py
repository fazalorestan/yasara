from app.production_packaging_v1.release_package import ReleasePackageBuilderV1

def test_release_package_ready():
    summary = ReleasePackageBuilderV1().build()
    assert summary.ready is True
    assert "installer" in summary.sections
