from app.v11_exchange_connectivity.models import ExchangeConnectivityHealthV11, ExchangeConnectivityStateV11
from app.v11_exchange_connectivity.profiles import ExchangeProfileRegistryV11


class ExchangeConnectivityHealthServiceV11:
    def __init__(self, profiles: ExchangeProfileRegistryV11 | None = None):
        self.profiles = profiles or ExchangeProfileRegistryV11()

    def check_exchange(self, exchange: str) -> ExchangeConnectivityHealthV11:
        profile = self.profiles.get(exchange)
        if profile is None or not profile.enabled:
            return ExchangeConnectivityHealthV11(
                exchange=exchange.lower(),
                state=ExchangeConnectivityStateV11.OFFLINE,
                message="unsupported_or_disabled",
            )
        return ExchangeConnectivityHealthV11(
            exchange=profile.exchange,
            state=ExchangeConnectivityStateV11.HEALTHY,
            latency_ms=1.0,
            message="offline_safe_health_stub",
        )

    def check_all(self) -> list[ExchangeConnectivityHealthV11]:
        return [self.check_exchange(exchange) for exchange in self.profiles.enabled_exchange_ids()]
