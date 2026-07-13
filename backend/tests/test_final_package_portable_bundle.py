from app.final_package_v1.portable_bundle_plan import PortableBundlePlanBuilderV1

def test_portable_bundle_plan():
    plan = PortableBundlePlanBuilderV1().build()
    assert plan.include_runtime is True
