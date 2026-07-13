from app.enterprise_v1.event_subscription_registry import EventSubscriptionRegistryV1, EventSubscriptionV1

def test_event_subscription_registry():
    registry = EventSubscriptionRegistryV1()
    registry.subscribe(EventSubscriptionV1(event_type="risk", handler_name="h1"))
    assert registry.handlers_for("risk") == ["h1"]
