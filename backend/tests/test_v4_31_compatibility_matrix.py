from app.platform_core.release.compatibility_matrix import CompatibilityMatrix

def test_v431_compatibility_matrix():
    m = CompatibilityMatrix().matrix()
    assert m["ready"] is True
    assert not m["breaking_changes"]
