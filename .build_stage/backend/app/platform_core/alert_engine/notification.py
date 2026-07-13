class AlertNotificationContract:
    def channels(self):
        return {"ready": True, "channels": [{"channel": "in_app", "enabled": True, "dry_run": True}, {"channel": "email", "enabled": False, "dry_run": True}, {"channel": "webhook", "enabled": False, "dry_run": True}]}

    def send_contract(self, event: dict):
        return {"ready": True, "sent": False, "dry_run": True, "event": event, "reason": "notification_delivery_disabled"}

alert_notification_contract = AlertNotificationContract()
