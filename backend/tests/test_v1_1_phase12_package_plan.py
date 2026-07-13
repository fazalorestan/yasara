from app.v11_final_release.service import FinalReleaseServiceV11

def test_final_release_package_plan():
    plan = FinalReleaseServiceV11().package_plan()
    assert plan["ready"] is True
    assert plan["version"] == "1.1.0"
    assert any("build_v1_1_final_package.bat" in command for command in plan["commands"])
