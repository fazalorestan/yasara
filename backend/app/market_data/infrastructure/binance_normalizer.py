from app.market_data.domain.events import MarketEvent, MarketEventType
from app.market_data.domain.models import Candle, ExchangeCode
from app.market_data.infrastructure.utils import ms_to_dt, slash_symbol, to_float, to_int

class BinanceStreamNormalizer:
    def kline_event(self, raw: dict) -> MarketEvent:
        k = raw.get("k", {})
        symbol = slash_symbol(k.get("s", raw.get("s", "")))
        candle = Candle(
            exchange=ExchangeCode.BINANCE_FUTURES,
            symbol=symbol,
            timeframe=k.get("i", ""),
            open_time=ms_to_dt(k.get("t", 0)),
            close_time=ms_to_dt(k.get("T", 0)),
            open=to_float(k.get("o")),
            high=to_float(k.get("h")),
            low=to_float(k.get("l")),
            close=to_float(k.get("c")),
            volume=to_float(k.get("v")),
            quote_volume=to_float(k.get("q")),
            trades=to_int(k.get("n")),
            is_closed=bool(k.get("x")),
        )
        return MarketEvent(
            event_type=MarketEventType.KLINE,
            exchange=ExchangeCode.BINANCE_FUTURES.value,
            symbol=symbol,
            payload={"candle": candle.model_dump(mode="json"), "raw": raw},
        )

    def ticker_event(self, raw: dict) -> MarketEvent:
        symbol = slash_symbol(raw.get("s", ""))
        return MarketEvent(
            event_type=MarketEventType.TICKER,
            exchange=ExchangeCode.BINANCE_FUTURES.value,
            symbol=symbol,
            payload={
                "last_price": to_float(raw.get("c")),
                "price_change_percent": to_float(raw.get("P")),
                "volume": to_float(raw.get("v")),
                "quote_volume": to_float(raw.get("q")),
                "raw": raw,
            },
        )

    def depth_event(self, raw: dict) -> MarketEvent:
        symbol = slash_symbol(raw.get("s", ""))
        return MarketEvent(
            event_type=MarketEventType.DEPTH,
            exchange=ExchangeCode.BINANCE_FUTURES.value,
            symbol=symbol,
            payload={"bids": raw.get("b", []), "asks": raw.get("a", []), "raw": raw},
        )
