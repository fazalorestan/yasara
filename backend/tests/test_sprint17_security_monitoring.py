from app.production_ai_v1.engine.monitoring import ProductionMonitoringEngineV1
from app.production_ai_v1.engine.security_checklist import SecurityChecklistEngineV1

def test_security_checklist_passes():
    report = SecurityChecklistEngineV1().run()
    assert report.passed is True
    assert any(i.key == "live_trading_disabled" for i in report.items)

def test_monitoring_report_ok():
    report = ProductionMonitoringEngineV1().report()
    assert report.status == "ok"
    assert any(m.key == "live_trading_enabled" for m in report.metrics)
