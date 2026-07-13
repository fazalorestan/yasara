from app.final_package_v1.docs_bundle_plan import DocsBundlePlanBuilderV1

def test_docs_bundle_plan():
    plan = DocsBundlePlanBuilderV1().build()
    assert "docs/SECURITY.md" in plan.docs
