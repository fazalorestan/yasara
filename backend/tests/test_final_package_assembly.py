from app.final_package_v1.package_assembly import PackageAssemblyPlanBuilderV1

def test_package_assembly():
    plan = PackageAssemblyPlanBuilderV1().build()
    assert plan.package_name == "YaSara_Professional_v1.0"
    assert any(i.name == "backend" for i in plan.items)
