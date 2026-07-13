from pydantic import BaseModel
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.router_engine import ExchangeRouterEngineV1

class FailoverDecisionV1(BaseModel):
    selected_exchange: SupportedExchange | None
    skipped: list[SupportedExchange]
    reason: str

class ExchangeFailoverEngineV1:
    def __init__(self):
        self.router = ExchangeRouterEngineV1()

    def choose(self, symbol: str, unhealthy: list[SupportedExchange] | None = None) -> FailoverDecisionV1:
        unhealthy = unhealthy or []
        available = [e for e in self.router.available_for_symbol(symbol) if e not in unhealthy]
        if not available:
            return FailoverDecisionV1(selected_exchange=None, skipped=unhealthy, reason="no_healthy_exchange")
        return FailoverDecisionV1(selected_exchange=available[0], skipped=unhealthy, reason="healthy_exchange_selected")
