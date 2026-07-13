from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.failover import ExchangeFailoverEngineV1

def test_exchange_failover_skips_unhealthy():
    result = ExchangeFailoverEngineV1().choose("BTC/USDT", unhealthy=[SupportedExchange.BITUNIX])
    assert result.selected_exchange == SupportedExchange.TOOBIT
