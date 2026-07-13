from app.v11_exchange_connectivity.failover import ExchangeFailoverRouterV11
from app.v11_exchange_connectivity.rest_client import ExchangeRestClientV11


class ExchangeConnectivityRouterV11:
    def __init__(self):
        self.failover = ExchangeFailoverRouterV11()
        self.rest = ExchangeRestClientV11()

    def market_request(self, path: str, preferred_exchange: str | None = None):
        selected = self.failover.choose(preferred_exchange)
        request = self.rest.build_request(selected.selected_exchange, path, method="GET", signed=False)
        return {
            "selected": selected.model_dump(),
            "request": request.model_dump(),
        }
