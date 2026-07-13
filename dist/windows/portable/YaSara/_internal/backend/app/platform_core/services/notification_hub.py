from app.platform_core.kernel.event_bus import PlatformEvent, event_bus
class NotificationHub:
    def request(self, channel, message, payload=None):
        return event_bus.publish(PlatformEvent(name='NotificationRequested', source='notification_hub', payload={'channel':channel,'message':message,'payload':payload or {}}))
notification_hub=NotificationHub()
