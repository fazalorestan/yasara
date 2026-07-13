from pydantic import BaseModel

class EventSubscriptionV1(BaseModel):
    event_type: str
    handler_name: str
    active: bool = True

class EventSubscriptionRegistryV1:
    def __init__(self):
        self.subscriptions: list[EventSubscriptionV1] = []

    def subscribe(self, subscription: EventSubscriptionV1) -> EventSubscriptionV1:
        self.subscriptions.append(subscription)
        return subscription

    def handlers_for(self, event_type: str) -> list[str]:
        return [s.handler_name for s in self.subscriptions if s.event_type == event_type and s.active]
