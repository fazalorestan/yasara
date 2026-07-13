from app.platform_core.alert_engine.notification import AlertNotificationContract

def test_v500_alpha28_notify_contract(): assert AlertNotificationContract().send_contract({'ready':True})['sent'] is False
