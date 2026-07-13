import pytest
from app.notifications_v1.domain.models import NotificationChannel, NotificationMessage, NotificationRecipient, NotificationType
from app.notifications_v1.engine.queue import NotificationQueueV1

@pytest.mark.asyncio
async def test_notification_queue_sends_dryrun():
    queue = NotificationQueueV1()
    message = NotificationMessage(notification_type=NotificationType.SYSTEM, title="Test", body="Hello")
    recipient = NotificationRecipient(channel=NotificationChannel.EMAIL, target="test@example.com")
    batch = queue.enqueue(message, [recipient])
    assert batch.queued == 1
    report = await queue.process_once()
    assert report.sent == 1
    assert queue.history()[0].provider_message_id.startswith("dryrun_")
