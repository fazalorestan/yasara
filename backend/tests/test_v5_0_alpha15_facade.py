from app.v500_alpha15_market_data.service import MarketDataFacadeV500Alpha15
def test_v500_alpha15_facade():
    f = MarketDataFacadeV500Alpha15()
    assert f.summary().ready is True
    assert f.readiness()["ready"] is True
