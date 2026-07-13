from app.platform_core.versioning import VersionCompatibilityChecker

def test_v426_version_compatibility():
    result = VersionCompatibilityChecker().check("p")
    assert result["compatible"] is True
    assert result["core_version"] == "v4.26"
