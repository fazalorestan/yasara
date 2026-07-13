from app.v426_platform_contracts_sdk.service import PlatformContractsSDKServiceV426

def test_v426_service():
    s = PlatformContractsSDKServiceV426()
    assert s.summary().ready is True
    assert s.standard_response()["ready"] is True
    assert s.capabilities()["ready"] is True
