from app.platform_core.exchanges.service import exchange_connector_framework_service
from app.v500_alpha16_exchange_connector.models import ExchangeConnectorSummaryV500Alpha16

class ExchangeConnectorFacadeV500Alpha16:
    def summary(self):
        return ExchangeConnectorSummaryV500Alpha16()

    def list(self):
        return exchange_connector_framework_service.list_exchanges()

    def exchange(self, exchange_id: str = "binance"):
        return exchange_connector_framework_service.exchange(exchange_id)

    def capabilities(self, exchange_id: str | None = None):
        return exchange_connector_framework_service.capabilities(exchange_id)

    def metadata(self, exchange_id: str | None = None):
        return exchange_connector_framework_service.metadata(exchange_id)

    def health(self):
        return exchange_connector_framework_service.health()

    def connector_contract(self):
        return exchange_connector_framework_service.connector_contract()

    def readiness(self):
        return exchange_connector_framework_service.readiness()
