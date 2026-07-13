from app.platform_core.indicators.lifecycle.audit import IndicatorLifecycleAuditPublisher

def test_v500_alpha4_audit():
    r = IndicatorLifecycleAuditPublisher().publish("yasara", "snapshot", "enabled")
    assert r["ready"] is True
    assert r["event"]["name"] == "IndicatorLifecycleChanged"
