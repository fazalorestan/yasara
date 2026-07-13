from app.platform_core.alert_engine.notification import AlertNotificationContract

def test_v500_alpha28_channels(): assert AlertNotificationContract().channels()['ready'] is True
