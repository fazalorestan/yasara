import time
from datetime import datetime, timezone
from app.market_data.domain.models import (
    Candle,
    ExchangeCode,
    ExchangeHealth,
    FundingRate,
    MarketSymbol,
    OpenInterest,
    OrderBook,
    OrderBookLevel,
    SymbolStatus,
    Ticker,
)
from app.market_data.domain.ports import MarketDataExchangePort
from app.market_data.infrastructure.cache import AsyncTTLCache
from app.market_data.infrastructure.http_client import AsyncExchangeHttpClient
from app.market_data.infrastructure.utils import compact_symbol, ms_to_dt, slash_symbol, to_float, to_int

class BinanceFuturesAdapter(MarketDataExchangePort):
    def __init__(self, base_url: str = "https://fapi.binance.com"):
        self.exchange = ExchangeCode.BINANCE_FUTURES
        self.http = AsyncExchangeHttpClient(base_url=base_url)
        self.cache = AsyncTTLCache(default_ttl_seconds=60)

    async def health(self) -> ExchangeHealth:
        start = time.perf_counter()
        try:
            await self.http.request("GET", "/fapi/v1/ping")
            server_time = await self._server_time()
            latency_ms = (time.perf_counter() - start) * 1000
            drift = (server_time - datetime.now(timezone.utc)).total_seconds() * 1000
            return ExchangeHealth(
                exchange=self.exchange,
                rest_available=True,
                websocket_available=True,
                latency_ms=latency_ms,
                server_time=server_time,
                clock_drift_ms=drift,
            )
        except Exception as exc:
            return ExchangeHealth(exchange=self.exchange, rest_available=False, websocket_available=False, message=str(exc))

    async def _server_time(self) -> datetime:
        data = await self.http.request("GET", "/fapi/v1/time")
        return ms_to_dt(data["serverTime"])

    async def symbols(self, force_refresh: bool = False) -> list[MarketSymbol]:
        cached = await self.cache.get("symbols")
        if cached is not None and not force_refresh:
            return cached
        data = await self.http.request("GET", "/fapi/v1/exchangeInfo")
        out: list[MarketSymbol] = []
        for item in data.get("symbols", []):
            if item.get("quoteAsset") != "USDT":
                continue
            filters = {f.get("filterType", ""): f for f in item.get("filters", [])}
            lot = filters.get("LOT_SIZE", {})
            price = filters.get("PRICE_FILTER", {})
            min_notional = filters.get("MIN_NOTIONAL", {})
            out.append(MarketSymbol(
                exchange=self.exchange,
                symbol=f"{item.get('baseAsset')}/{item.get('quoteAsset')}",
                base_asset=item.get("baseAsset", ""),
                quote_asset=item.get("quoteAsset", ""),
                status=SymbolStatus.TRADING if item.get("status") == "TRADING" else SymbolStatus.UNKNOWN,
                price_precision=to_int(item.get("pricePrecision"), 8),
                quantity_precision=to_int(item.get("quantityPrecision"), 8),
                tick_size=to_float(price.get("tickSize")),
                step_size=to_float(lot.get("stepSize")),
                min_quantity=to_float(lot.get("minQty")),
                min_notional=to_float(min_notional.get("notional")),
                raw=item,
            ))
        await self.cache.set("symbols", out, ttl_seconds=3600)
        return out

    async def ticker(self, symbol: str) -> Ticker:
        data = await self.http.request("GET", "/fapi/v1/ticker/24hr", params={"symbol": compact_symbol(symbol)})
        return Ticker(
            exchange=self.exchange,
            symbol=slash_symbol(data.get("symbol", symbol)),
            last_price=to_float(data.get("lastPrice")),
            bid_price=to_float(data.get("bidPrice")),
            ask_price=to_float(data.get("askPrice")),
            high_24h=to_float(data.get("highPrice")),
            low_24h=to_float(data.get("lowPrice")),
            volume_24h=to_float(data.get("volume")),
            quote_volume_24h=to_float(data.get("quoteVolume")),
            price_change_percent_24h=to_float(data.get("priceChangePercent")),
        )

    async def candles(self, symbol: str, timeframe: str, limit: int = 500, start_time: datetime | None = None) -> list[Candle]:
        params = {"symbol": compact_symbol(symbol), "interval": timeframe, "limit": min(limit, 1500)}
        if start_time:
            params["startTime"] = int(start_time.timestamp() * 1000)
        data = await self.http.request("GET", "/fapi/v1/klines", params=params)
        return [
            Candle(
                exchange=self.exchange,
                symbol=slash_symbol(symbol),
                timeframe=timeframe,
                open_time=ms_to_dt(row[0]),
                close_time=ms_to_dt(row[6]),
                open=to_float(row[1]),
                high=to_float(row[2]),
                low=to_float(row[3]),
                close=to_float(row[4]),
                volume=to_float(row[5]),
                quote_volume=to_float(row[7]),
                trades=to_int(row[8]),
                is_closed=True,
            )
            for row in data
        ]

    async def order_book(self, symbol: str, limit: int = 100) -> OrderBook:
        data = await self.http.request("GET", "/fapi/v1/depth", params={"symbol": compact_symbol(symbol), "limit": min(limit, 1000)})
        return OrderBook(
            exchange=self.exchange,
            symbol=slash_symbol(symbol),
            bids=[OrderBookLevel(price=to_float(x[0]), quantity=to_float(x[1])) for x in data.get("bids", [])],
            asks=[OrderBookLevel(price=to_float(x[0]), quantity=to_float(x[1])) for x in data.get("asks", [])],
            last_update_id=data.get("lastUpdateId"),
        )

    async def funding_rate(self, symbol: str) -> FundingRate:
        data = await self.http.request("GET", "/fapi/v1/premiumIndex", params={"symbol": compact_symbol(symbol)})
        return FundingRate(
            exchange=self.exchange,
            symbol=slash_symbol(symbol),
            funding_rate=to_float(data.get("lastFundingRate")),
            next_funding_time=ms_to_dt(data["nextFundingTime"]) if data.get("nextFundingTime") else None,
        )

    async def open_interest(self, symbol: str) -> OpenInterest:
        data = await self.http.request("GET", "/fapi/v1/openInterest", params={"symbol": compact_symbol(symbol)})
        return OpenInterest(exchange=self.exchange, symbol=slash_symbol(symbol), open_interest=to_float(data.get("openInterest")))

    async def close(self) -> None:
        await self.http.close()
