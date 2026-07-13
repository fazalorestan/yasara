from app.consolidation_v1.package_manifest import FinalPackageManifestBuilderV1

def test_phase_b_package_manifest():
    manifest = FinalPackageManifestBuilderV1().build()
    assert manifest.package_name == "yasara_v1_0_professional"
    assert any(section.name == "backend" for section in manifest.sections)
