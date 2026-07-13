from app.notifications_v1.domain.models import NotificationMessage, NotificationRecipient
from app.notifications_v1.engine.queue import NotificationQueueV1
from app.notifications_v1.engine.templates import NotificationTemplateEngineV1

class NotificationServiceV1:
    def __init__(self):
        self.queue = NotificationQueueV1()
        self.templates = NotificationTemplateEngineV1()

    async def enqueue(self, message: NotificationMessage, recipients: list[NotificationRecipient]):
        return self.queue.enqueue(message, recipients)

    async def process(self):
        return await self.queue.process_once()

    async def report(self):
        return self.queue.report()

    async def history(self):
        return self.queue.history()

    async def send_signal(self, symbol: str, direction: str, confidence: float, recipients: list[NotificationRecipient], reasons: list[str] | None = None):
        message = self.templates.signal_template(symbol, direction, confidence, reasons)
        batch = self.queue.enqueue(message, recipients)
        await self.queue.process_once()
        return batch

notification_service_v1 = NotificationServiceV1()
