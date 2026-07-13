from app.v426_platform_contracts_sdk.models import PlatformContractsSDKSummaryV426

def test_v426_summary():
    s = PlatformContractsSDKSummaryV426()
    assert s.ready is True
    assert s.no_new_trading_features is True
