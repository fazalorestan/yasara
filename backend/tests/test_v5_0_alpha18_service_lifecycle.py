from app.platform_core.exchanges.sdk.service import ExchangeSDKLifecycleService
def test_v500_alpha18_service_lifecycle():
    assert ExchangeSDKLifecycleService().lifecycle()["ready"] is True
