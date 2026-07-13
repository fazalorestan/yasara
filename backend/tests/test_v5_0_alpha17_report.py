from app.platform_core.api_health.report import APIHealthReportBuilder

def test_v500_alpha17_report():
    r = APIHealthReportBuilder().build()
    assert r['ready'] is True
    assert r['execution_allowed'] is False
