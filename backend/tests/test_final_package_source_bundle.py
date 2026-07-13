from app.final_package_v1.source_bundle_plan import SourceBundlePlanBuilderV1

def test_source_bundle_plan():
    plan = SourceBundlePlanBuilderV1().build()
    assert "backend/app/**" in plan.include
    assert "backend/.venv/**" in plan.exclude
