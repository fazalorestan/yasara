from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.router_engine import ExchangeRouterEngineV1
from app.multi_exchange_v1.symbol_registry import symbol_registry_v1

def test_extras_symbol_registry_model():
    assert symbol_registry_v1.get(SupportedExchange.BITUNIX, "BTC/USDT") is not None

def test_extras_route_model():
    decision = ExchangeRouterEngineV1().choose("BTC/USDT")
    assert decision.selected_exchange in {SupportedExchange.BITUNIX, SupportedExchange.TOOBIT}
