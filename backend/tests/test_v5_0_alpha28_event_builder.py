from app.platform_core.alert_engine.events import AlertEventBuilder

def test_v500_alpha28_event_builder(): assert AlertEventBuilder().build('r','BTCUSDT','m','info')['ready'] is True
