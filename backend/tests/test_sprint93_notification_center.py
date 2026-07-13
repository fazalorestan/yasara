from app.desktop_ui_v1.notification_center import NotificationCenterViewV1, NotificationViewItemV1

def test_notification_center_critical():
    items = [NotificationViewItemV1(title="Risk", body="High", severity="critical")]
    assert len(NotificationCenterViewV1().critical(items)) == 1
