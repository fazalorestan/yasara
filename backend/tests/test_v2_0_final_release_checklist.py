from app.v20_final_release.service import V20FinalReleaseService

def test_v2_0_final_release_checklist():
    checklist = V20FinalReleaseService().checklist()
    assert checklist["ready"] is True
    assert all(item["passed"] for item in checklist["items"])
