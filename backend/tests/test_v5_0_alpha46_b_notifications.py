from app.platform_core.desktop_app.notification_center import DesktopNotificationCenter

def test_notifications(): assert DesktopNotificationCenter().notifications()['enabled'] is True
