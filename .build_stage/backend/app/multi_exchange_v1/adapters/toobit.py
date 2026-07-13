import uuid
from app.multi_exchange_v1.adapters.base import BaseExchangeAdapterV1
from app.multi_exchange_v1.clients.public_http import PublicHTTPClientV1
from app.multi_exchange_v1.domain.models import (
    ExchangeAdapterStatus,
    ExchangeCapability,
    ExchangeDescriptor,
    SupportedExchange,
    UnifiedOrderBook,
    UnifiedPrivateOrderRequest,
    UnifiedPrivateOrderResult,
    UnifiedTicker,
)
from app.multi_exchange_v1.parsers import PublicMarketDataParserV1
from app.multi_exchange_v1.symbols import SymbolMapperV1

class ToobitAdapterV1(BaseExchangeAdapterV1):
    exchange = SupportedExchange.TOOBIT

    def __init__(self, client: PublicHTTPClientV1 | None = None):
        self.client = client or PublicHTTPClientV1()
        self.symbols = SymbolMapperV1()
        self.parser = PublicMarketDataParserV1()

    def descriptor(self) -> ExchangeDescriptor:
        return ExchangeDescriptor(
            exchange=self.exchange,
            display_name="Toobit",
            status=ExchangeAdapterStatus.SCAFFOLD,
            base_url="https://api.toobit.com",
            futures_supported=True,
            spot_supported=True,
            capabilities=[
                ExchangeCapability.MARKET_DATA,
                ExchangeCapability.TICKER,
                ExchangeCapability.ORDER_BOOK,
                ExchangeCapability.DRY_RUN_PRIVATE,
            ],
            live_trading_enabled=False,
            notes="Toobit public market data scaffold added. Live trading remains disabled.",
        )

    async def ticker(self, symbol: str) -> UnifiedTicker:
        mapped = self.symbols.to_exchange_symbol(self.exchange, symbol)
        payload = await self.client.get_json("https://api.toobit.com/api/v1/ticker/24hr", {"symbol": mapped})
        return self.parser.ticker_from_payload(self.exchange, symbol, payload)

    async def order_book(self, symbol: str, limit: int = 20) -> UnifiedOrderBook:
        mapped = self.symbols.to_exchange_symbol(self.exchange, symbol)
        payload = await self.client.get_json("https://api.toobit.com/api/v1/depth", {"symbol": mapped, "limit": limit})
        return self.parser.order_book_from_payload(self.exchange, symbol, payload)

    async def place_order_dry_run(self, request: UnifiedPrivateOrderRequest) -> UnifiedPrivateOrderResult:
        if not request.dry_run:
            return UnifiedPrivateOrderResult(
                accepted=False,
                exchange=self.exchange,
                symbol=request.symbol,
                side=request.side,
                quantity=request.quantity,
                dry_run=False,
                message="Toobit live trading is disabled in Sprint 26.",
            )
        return UnifiedPrivateOrderResult(
            accepted=True,
            exchange=self.exchange,
            symbol=request.symbol,
            side=request.side,
            quantity=request.quantity,
            dry_run=True,
            exchange_order_id=f"toobit_dryrun_{uuid.uuid4().hex}",
            message="Toobit order accepted in dry-run mode. No live order was sent.",
        )
