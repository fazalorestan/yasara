import uuid
from datetime import datetime, timezone
from app.notifications_v1.domain.models import (
    DeliveryReport,
    NotificationBatch,
    NotificationChannel,
    NotificationDelivery,
    NotificationMessage,
    NotificationRecipient,
    NotificationStatus,
)
from app.notifications_v1.engine.rate_limiter import NotificationRateLimiterV1
from app.notifications_v1.infrastructure.providers import DryRunNotificationProvider, TelegramNotificationProvider, WebhookNotificationProvider

class NotificationQueueV1:
    def __init__(self):
        self.deliveries: list[NotificationDelivery] = []
        self.rate_limiter = NotificationRateLimiterV1()
        self.providers = {
            NotificationChannel.TELEGRAM: TelegramNotificationProvider(),
            NotificationChannel.WEBHOOK: WebhookNotificationProvider(),
            NotificationChannel.EMAIL: DryRunNotificationProvider(),
            NotificationChannel.DISCORD: DryRunNotificationProvider(),
            NotificationChannel.DESKTOP: DryRunNotificationProvider(),
        }

    def enqueue(self, message: NotificationMessage, recipients: list[NotificationRecipient]) -> NotificationBatch:
        deliveries = []
        skipped = 0
        for recipient in recipients:
            if not recipient.enabled:
                skipped += 1
                continue
            delivery = NotificationDelivery(
                delivery_id=uuid.uuid4().hex,
                recipient=recipient,
                message=message,
            )
            self.deliveries.append(delivery)
            deliveries.append(delivery)
        return NotificationBatch(deliveries=deliveries, queued=len(deliveries), skipped=skipped)

    async def process_once(self) -> DeliveryReport:
        for delivery in self.deliveries:
            if delivery.status not in {NotificationStatus.QUEUED, NotificationStatus.RETRYING}:
                continue
            key = f"{delivery.recipient.channel}:{delivery.recipient.target}"
            if not self.rate_limiter.allow(key):
                delivery.status = NotificationStatus.RETRYING
                delivery.last_error = "Rate limited."
                delivery.updated_at = datetime.now(timezone.utc)
                continue
            provider = self.providers.get(delivery.recipient.channel, DryRunNotificationProvider())
            try:
                await provider.send(delivery)
            except Exception as exc:
                delivery.attempts += 1
                delivery.last_error = str(exc)
                delivery.updated_at = datetime.now(timezone.utc)
                delivery.status = NotificationStatus.RETRYING if delivery.attempts < delivery.max_attempts else NotificationStatus.FAILED
        return self.report()

    def report(self) -> DeliveryReport:
        counts = {status: 0 for status in NotificationStatus}
        for delivery in self.deliveries:
            counts[delivery.status] += 1
        return DeliveryReport(
            total=len(self.deliveries),
            queued=counts[NotificationStatus.QUEUED],
            sent=counts[NotificationStatus.SENT],
            failed=counts[NotificationStatus.FAILED],
            retrying=counts[NotificationStatus.RETRYING],
            cancelled=counts[NotificationStatus.CANCELLED],
        )

    def history(self) -> list[NotificationDelivery]:
        return list(self.deliveries)
