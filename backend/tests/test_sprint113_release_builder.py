from app.release_pro_v1.release_builder import ProfessionalReleaseBuilderV1

def test_release_builder_plan():
    plan = ProfessionalReleaseBuilderV1().plan()
    assert plan.version == "1.0.0-pro"
    assert any(a.name == "source" for a in plan.artifacts)
