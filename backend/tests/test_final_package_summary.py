from app.final_package_v1.package_summary import FinalPackageSummaryBuilderV1

def test_final_package_summary():
    summary = FinalPackageSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.previous_confirmed_tests >= 284
