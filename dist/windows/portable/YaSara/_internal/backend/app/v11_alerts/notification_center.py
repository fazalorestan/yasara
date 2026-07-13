from app.v11_alerts.models import AlertEventV11, NotificationChannelV11, NotificationDeliveryV11


class NotificationCenterV11:
    def __init__(self):
        self.deliveries: list[NotificationDeliveryV11] = []

    def deliver(self, event: AlertEventV11, channels: list[NotificationChannelV11] | None = None) -> list[NotificationDeliveryV11]:
        channels = channels or [NotificationChannelV11.DASHBOARD, NotificationChannelV11.LOG]
        results: list[NotificationDeliveryV11] = []
        for channel in channels:
            delivery = NotificationDeliveryV11(
                channel=channel,
                delivered=True,
                message=f"{event.severity.value.upper()}: {event.message}",
            )
            self.deliveries.append(delivery)
            results.append(delivery)
        return results

    def recent(self, limit: int = 50) -> list[NotificationDeliveryV11]:
        return self.deliveries[-limit:]
