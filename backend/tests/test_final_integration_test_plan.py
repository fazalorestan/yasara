from app.final_integration_v1.consolidated_test_plan import ConsolidatedTestPlanBuilderV1

def test_consolidated_test_plan():
    plan = ConsolidatedTestPlanBuilderV1().build()
    assert any(g.name == "full" for g in plan.groups)
