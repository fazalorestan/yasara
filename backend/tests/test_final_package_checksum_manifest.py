from app.final_package_v1.checksum_manifest import ChecksumManifestBuilderV1

def test_checksum_manifest():
    manifest = ChecksumManifestBuilderV1().build()
    assert all(i.algorithm == "sha256" for i in manifest.items)
