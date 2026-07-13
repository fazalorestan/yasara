from app.platform_core.exchanges.sdk.service import ExchangeSDKLifecycleService
def test_v500_alpha18_service_register_enable():
    s = ExchangeSDKLifecycleService()
    assert s.register("bitunix")["ready"] is True
    assert s.enable("bitunix")["state"] == "ready"
