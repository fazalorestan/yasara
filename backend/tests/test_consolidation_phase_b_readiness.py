from app.consolidation_v1.phase_b_readiness import ConsolidationPhaseBReadinessBuilderV1

def test_phase_b_readiness():
    report = ConsolidationPhaseBReadinessBuilderV1().build()
    assert report.ready is True
    assert "package_manifest" in report.checks
