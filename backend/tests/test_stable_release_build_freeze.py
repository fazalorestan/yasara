from app.stable_release_v1.build_freeze import BuildFreezeBuilderV1

def test_build_freeze():
    freeze = BuildFreezeBuilderV1().build()
    assert freeze.frozen is True
    assert "critical_hotfix" in freeze.allowed_changes
