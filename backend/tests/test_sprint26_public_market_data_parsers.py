from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.parsers import PublicMarketDataParserV1

def test_ticker_parser_common_payload():
    payload = {"data": {"lastPrice": "61000.5", "priceChangePercent": "2.1", "volume": "123"}}
    ticker = PublicMarketDataParserV1().ticker_from_payload(SupportedExchange.BITUNIX, "BTC/USDT", payload)
    assert ticker.price == 61000.5
    assert ticker.change_percent == 2.1
    assert ticker.volume == 123

def test_order_book_parser_common_payload():
    payload = {"data": {"bids": [["60000", "1.5"]], "asks": [["60100", "2"]]}}
    book = PublicMarketDataParserV1().order_book_from_payload(SupportedExchange.TOOBIT, "BTC/USDT", payload)
    assert book.bids[0] == [60000.0, 1.5]
    assert book.asks[0] == [60100.0, 2.0]
