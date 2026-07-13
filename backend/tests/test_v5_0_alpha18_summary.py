from app.v500_alpha18_exchange_sdk.models import ExchangeSDKSummaryV500Alpha18
def test_v500_alpha18_summary():
    s = ExchangeSDKSummaryV500Alpha18()
    assert s.ready is True
    assert s.sdk_version == "1.0"
