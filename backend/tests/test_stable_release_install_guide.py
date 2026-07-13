from app.stable_release_v1.install_guide import StableInstallGuideBuilderV1

def test_install_guide():
    guide = StableInstallGuideBuilderV1().build()
    assert any("pytest" in step.command for step in guide.steps)
