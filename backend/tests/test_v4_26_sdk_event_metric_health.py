from app.platform_core.sdk.platform_sdk import PlatformSDK

def test_v426_sdk_event_metric_health():
    sdk = PlatformSDK()
    event = sdk.publish_event("TestEvent", {"x": 1})
    assert event.name == "TestEvent"
    assert sdk.increment_metric("test_metric") >= 1
    assert sdk.health("test_health", True)["ready"] is True
