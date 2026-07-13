from app.final_closeout_v1.actual_test_baseline import ActualTestBaselineBuilderV1

def test_actual_test_baseline():
    baseline = ActualTestBaselineBuilderV1().build()
    assert baseline.confirmed_passed_tests >= 285
    assert baseline.failed_tests == 0
