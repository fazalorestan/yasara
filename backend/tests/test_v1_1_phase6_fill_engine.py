from app.v11_paper_trading.fill_engine import PaperFillEngineV11
from app.v11_paper_trading.models import PaperOrderRequestV11, PaperOrderSideV11

def test_paper_fill_engine():
    request = PaperOrderRequestV11(exchange="binance", symbol="BTCUSDT", side=PaperOrderSideV11.BUY, quantity=1)
    assert PaperFillEngineV11().resolve_fill_price(request, 50000) == 50000
