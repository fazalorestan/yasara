from app.v11_paper_trading.service import PaperTradingServiceV11

def test_paper_trading_demo_snapshot():
    snapshot = PaperTradingServiceV11().demo()
    assert snapshot.ready is True
    assert len(snapshot.orders) == 2
