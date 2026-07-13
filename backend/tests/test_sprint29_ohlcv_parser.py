from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.ohlcv import OHLCVParserV1

def test_ohlcv_parser_array_rows():
    payload = {"data": [[1710000000000, "1", "2", "0.5", "1.5", "100"]]}
    rows = OHLCVParserV1().parse_rows(SupportedExchange.BITUNIX, "BTC/USDT", "1h", payload)
    assert len(rows) == 1
    assert rows[0].close == 1.5
    assert rows[0].volume == 100

def test_ohlcv_parser_dict_rows():
    payload = {"data": [{"open": "1", "high": "2", "low": "0.5", "close": "1.5", "volume": "100"}]}
    rows = OHLCVParserV1().parse_rows(SupportedExchange.TOOBIT, "ETH/USDT", "4h", payload)
    assert rows[0].symbol == "ETH/USDT"
    assert rows[0].timeframe == "4h"
