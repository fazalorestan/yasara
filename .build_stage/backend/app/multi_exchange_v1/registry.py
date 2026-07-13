from app.multi_exchange_v1.adapters.bitunix import BitunixAdapterV1
from app.multi_exchange_v1.adapters.toobit import ToobitAdapterV1
from app.multi_exchange_v1.domain.models import SupportedExchange

class ExchangeRegistryV1:
    def __init__(self):
        self._adapters = {
            SupportedExchange.BITUNIX: BitunixAdapterV1(),
            SupportedExchange.TOOBIT: ToobitAdapterV1(),
        }

    def list_adapters(self):
        return list(self._adapters.values())

    def get(self, exchange: SupportedExchange):
        return self._adapters.get(exchange)

    def descriptors(self):
        return [adapter.descriptor() for adapter in self.list_adapters()]

exchange_registry_v1 = ExchangeRegistryV1()
