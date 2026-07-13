from app.enterprise_v1.enterprise_summary import EnterpriseSummaryBuilderV1

def test_enterprise_summary():
    summary = EnterpriseSummaryBuilderV1().build()
    assert summary.ready is True
    assert "enterprise_v1" in summary.modules
