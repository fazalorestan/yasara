from datetime import datetime, timezone
from pydantic import BaseModel, Field
from app.multi_exchange_v1.domain.models import SupportedExchange
from app.multi_exchange_v1.registry import exchange_registry_v1

class ExchangeHealthItemV1(BaseModel):
    exchange: SupportedExchange
    status: str
    live_trading_enabled: bool
    capabilities: list[str] = Field(default_factory=list)
    checked_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ExchangeHealthReportV1(BaseModel):
    status: str
    exchanges: list[ExchangeHealthItemV1] = Field(default_factory=list)
    generated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class ExchangeHealthEngineV1:
    def report(self) -> ExchangeHealthReportV1:
        items = []
        for descriptor in exchange_registry_v1.descriptors():
            items.append(
                ExchangeHealthItemV1(
                    exchange=descriptor.exchange,
                    status=descriptor.status,
                    live_trading_enabled=descriptor.live_trading_enabled,
                    capabilities=[str(c) for c in descriptor.capabilities],
                )
            )
        return ExchangeHealthReportV1(status="ok", exchanges=items)
