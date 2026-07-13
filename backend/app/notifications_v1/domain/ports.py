from abc import ABC, abstractmethod
from app.notifications_v1.domain.models import NotificationDelivery

class NotificationProviderPort(ABC):
    @abstractmethod
    async def send(self, delivery: NotificationDelivery) -> NotificationDelivery:
        raise NotImplementedError
