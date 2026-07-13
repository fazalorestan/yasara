class DesktopNotificationCenter:
    def notifications(self):
        return {
            "ready": True,
            "enabled": True,
            "channels": ["system", "build", "test", "health"],
            "pending": 0,
            "crash_notifications_enabled": True,
        }

desktop_notification_center = DesktopNotificationCenter()
