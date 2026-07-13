from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.symbol_registry import SymbolRegistryV1

def test_symbol_registry_defaults():
    registry = SymbolRegistryV1()
    item = registry.get(SupportedExchange.BITUNIX, "BTC/USDT")
    assert item.exchange_symbol == "BTCUSDT"
    assert item.base_asset == "BTC"

def test_symbol_registry_list_by_exchange():
    registry = SymbolRegistryV1()
    items = registry.list(SupportedExchange.TOOBIT)
    assert len(items) >= 3
