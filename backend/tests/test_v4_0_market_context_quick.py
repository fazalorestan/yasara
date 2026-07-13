from app.v40_market_context.models import MarketContextRequestV40
from app.v40_market_context.service import MarketContextServiceV40

def test_v40_context():
    data = MarketContextServiceV40().context(MarketContextRequestV40(timeframes=['1m','5m']))
    assert data["ready"] is True
    assert "market_context" in data
    assert data["live_trading_enabled"] is False
