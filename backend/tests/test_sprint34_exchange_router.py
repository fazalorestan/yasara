from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.router_engine import ExchangeRouterEngineV1

def test_exchange_router_prefers_requested_exchange():
    decision = ExchangeRouterEngineV1().choose("BTC/USDT", SupportedExchange.TOOBIT)
    assert decision.selected_exchange == SupportedExchange.TOOBIT
    assert decision.reason == "preferred_exchange_available"

def test_exchange_router_has_available_exchanges():
    decision = ExchangeRouterEngineV1().choose("ETH/USDT")
    assert len(decision.available_exchanges) >= 1
