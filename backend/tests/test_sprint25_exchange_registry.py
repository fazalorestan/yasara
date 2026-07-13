from app.multi_exchange_v1.registry import exchange_registry_v1
from app.multi_exchange_v1.domain.models import SupportedExchange

def test_bitunix_and_toobit_registered():
    descriptors = exchange_registry_v1.descriptors()
    exchanges = {d.exchange for d in descriptors}
    assert SupportedExchange.BITUNIX in exchanges
    assert SupportedExchange.TOOBIT in exchanges
