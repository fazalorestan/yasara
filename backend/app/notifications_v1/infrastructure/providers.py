import uuid
from datetime import datetime, timezone
from app.notifications_v1.domain.models import NotificationDelivery, NotificationStatus
from app.notifications_v1.domain.ports import NotificationProviderPort

class DryRunNotificationProvider(NotificationProviderPort):
    async def send(self, delivery: NotificationDelivery) -> NotificationDelivery:
        delivery.status = NotificationStatus.SENT
        delivery.attempts += 1
        delivery.provider_message_id = f"dryrun_{uuid.uuid4().hex}"
        delivery.sent_at = datetime.now(timezone.utc)
        delivery.updated_at = delivery.sent_at
        return delivery

class WebhookNotificationProvider(NotificationProviderPort):
    async def send(self, delivery: NotificationDelivery) -> NotificationDelivery:
        # Sprint 11 scaffold: no external network side effects by default.
        delivery.status = NotificationStatus.SENT
        delivery.attempts += 1
        delivery.provider_message_id = f"webhook_dryrun_{uuid.uuid4().hex}"
        delivery.sent_at = datetime.now(timezone.utc)
        delivery.updated_at = delivery.sent_at
        return delivery

class TelegramNotificationProvider(NotificationProviderPort):
    async def send(self, delivery: NotificationDelivery) -> NotificationDelivery:
        # Tokenized Telegram delivery will be enabled after secrets vault integration.
        delivery.status = NotificationStatus.SENT
        delivery.attempts += 1
        delivery.provider_message_id = f"telegram_dryrun_{uuid.uuid4().hex}"
        delivery.sent_at = datetime.now(timezone.utc)
        delivery.updated_at = delivery.sent_at
        return delivery
