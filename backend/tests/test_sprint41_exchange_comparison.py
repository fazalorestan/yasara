from app.market_tools_v1.comparison import ExchangeComparisonEngineV1, ExchangePriceItemV1
from app.multi_exchange_v1.domain.models import SupportedExchange

def test_exchange_comparison_price_range():
    items = [
        ExchangePriceItemV1(exchange=SupportedExchange.BITUNIX, symbol="BTC/USDT", price=100),
        ExchangePriceItemV1(exchange=SupportedExchange.TOOBIT, symbol="BTC/USDT", price=105),
    ]
    result = ExchangeComparisonEngineV1().compare_prices(items)
    assert result.price_range == 5
    assert result.lowest_price_exchange == SupportedExchange.BITUNIX
