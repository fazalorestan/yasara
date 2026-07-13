from app.v11_exchange_connectivity.health import ExchangeConnectivityHealthServiceV11
from app.v11_exchange_connectivity.models import ExchangeConnectivitySummaryV11
from app.v11_exchange_connectivity.profiles import ExchangeProfileRegistryV11
from app.v11_exchange_connectivity.rate_profiles import ExchangeRateLimitProfileBuilderV11
from app.v11_exchange_connectivity.router import ExchangeConnectivityRouterV11


class ExchangeConnectivityServiceV11:
    def __init__(self):
        self.profiles = ExchangeProfileRegistryV11()
        self.health = ExchangeConnectivityHealthServiceV11(self.profiles)
        self.router = ExchangeConnectivityRouterV11()
        self.rate_profiles = ExchangeRateLimitProfileBuilderV11()

    def summary(self) -> ExchangeConnectivitySummaryV11:
        exchanges = self.profiles.enabled_exchange_ids()
        health = self.health.check_all()
        return ExchangeConnectivitySummaryV11(
            ready=bool(exchanges) and all(h.state.value == "healthy" for h in health),
            exchanges=exchanges,
            live_trading_enabled=False,
        )

    def diagnostics(self) -> dict:
        return {
            "summary": self.summary().model_dump(),
            "health": [h.model_dump() for h in self.health.check_all()],
            "rate_limits": [r.model_dump() for r in self.rate_profiles.build()],
            "sample_request": self.router.market_request("/api/v3/ticker/price", "binance"),
        }
