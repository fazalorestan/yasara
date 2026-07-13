from app.consolidation_v1.readiness import ConsolidationReadinessBuilderV1

def test_consolidation_readiness():
    report = ConsolidationReadinessBuilderV1().build()
    assert report.ready is True
    assert "tests_confirmed" in report.checks
