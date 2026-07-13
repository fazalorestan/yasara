from app.final_export_v1.version_seal import VersionSealBuilderV1

def test_version_seal():
    seal = VersionSealBuilderV1().build()
    assert seal.sealed is True
    assert seal.version == "1.0.0"
