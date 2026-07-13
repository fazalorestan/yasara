from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.symbols import SymbolMapperV1

def test_symbol_mapper_to_exchange_symbol():
    mapper = SymbolMapperV1()
    assert mapper.to_exchange_symbol(SupportedExchange.BITUNIX, "BTC/USDT") == "BTCUSDT"
    assert mapper.to_exchange_symbol(SupportedExchange.TOOBIT, "eth-usdt") == "ETHUSDT"

def test_symbol_mapper_from_exchange_symbol():
    mapper = SymbolMapperV1()
    assert mapper.from_exchange_symbol(SupportedExchange.BITUNIX, "BTCUSDT") == "BTC/USDT"
