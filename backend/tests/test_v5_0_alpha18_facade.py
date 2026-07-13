from app.v500_alpha18_exchange_sdk.service import ExchangeSDKFacadeV500Alpha18
def test_v500_alpha18_facade():
    f = ExchangeSDKFacadeV500Alpha18()
    assert f.summary().ready is True
    assert f.readiness()["ready"] is True
