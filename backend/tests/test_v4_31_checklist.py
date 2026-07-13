from app.platform_core.release.checklist import PreReleaseChecklist

def test_v431_checklist():
    checks = PreReleaseChecklist().run()
    assert checks
    assert all(c.passed for c in checks)
