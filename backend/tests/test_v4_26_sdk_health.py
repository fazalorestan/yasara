from app.platform_core.sdk_health import SDKHealthReporter

def test_v426_sdk_health():
    h = SDKHealthReporter()
    h.set("p", "healthy")
    assert h.get("p")["state"] == "healthy"
