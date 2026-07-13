from app.rc1_v1.regression_plan import RegressionPlanBuilderV1

def test_rc1_regression_plan():
    plan = RegressionPlanBuilderV1().build()
    assert any(s.name == "full_pytest" for s in plan.suites)
