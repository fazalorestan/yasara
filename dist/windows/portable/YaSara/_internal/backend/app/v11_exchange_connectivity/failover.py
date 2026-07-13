from app.v11_exchange_connectivity.health import ExchangeConnectivityHealthServiceV11
from app.v11_exchange_connectivity.models import ExchangeConnectivityStateV11, ExchangeFailoverResultV11
from app.v11_exchange_connectivity.profiles import ExchangeProfileRegistryV11


class ExchangeFailoverRouterV11:
    def __init__(self, profiles: ExchangeProfileRegistryV11 | None = None, health: ExchangeConnectivityHealthServiceV11 | None = None):
        self.profiles = profiles or ExchangeProfileRegistryV11()
        self.health = health or ExchangeConnectivityHealthServiceV11(self.profiles)

    def choose(self, preferred: str | None = None) -> ExchangeFailoverResultV11:
        candidates = self.profiles.enabled_exchange_ids()
        healthy = [h.exchange for h in self.health.check_all() if h.state == ExchangeConnectivityStateV11.HEALTHY]
        if preferred and preferred.lower() in healthy:
            return ExchangeFailoverResultV11(selected_exchange=preferred.lower(), fallback_used=False, candidates=candidates)
        if healthy:
            return ExchangeFailoverResultV11(selected_exchange=healthy[0], fallback_used=bool(preferred), candidates=candidates)
        return ExchangeFailoverResultV11(selected_exchange=candidates[0], fallback_used=True, candidates=candidates)
