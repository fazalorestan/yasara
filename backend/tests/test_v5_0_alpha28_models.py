from app.platform_core.alert_engine.models import AlertRule, AlertEvent

def test_v500_alpha28_models():
    r=AlertRule('r','Rule','x'); e=AlertEvent('r','BTCUSDT','msg','info'); assert r.enabled is True and e.acknowledged is False
