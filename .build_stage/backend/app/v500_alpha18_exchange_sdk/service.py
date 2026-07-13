from app.platform_core.exchanges.sdk.service import exchange_sdk_lifecycle_service
from app.v500_alpha18_exchange_sdk.models import ExchangeSDKSummaryV500Alpha18

class ExchangeSDKFacadeV500Alpha18:
    def summary(self):
        return ExchangeSDKSummaryV500Alpha18()

    def lifecycle(self):
        return exchange_sdk_lifecycle_service.lifecycle()

    def register(self, exchange_id: str = "binance"):
        return exchange_sdk_lifecycle_service.register(exchange_id)

    def enable(self, exchange_id: str = "binance"):
        return exchange_sdk_lifecycle_service.enable(exchange_id)

    def connectors(self):
        return exchange_sdk_lifecycle_service.connectors()

    def health(self):
        return exchange_sdk_lifecycle_service.health()

    def negotiate(self, exchange_id: str = "binance"):
        return exchange_sdk_lifecycle_service.negotiate(exchange_id)

    def sandbox(self):
        return exchange_sdk_lifecycle_service.sandbox()

    def events(self):
        return exchange_sdk_lifecycle_service.events()

    def readiness(self):
        return exchange_sdk_lifecycle_service.readiness()
