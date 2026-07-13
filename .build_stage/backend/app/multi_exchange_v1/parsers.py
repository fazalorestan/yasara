from app.multi_exchange_v1.domain.models import SupportedExchange, UnifiedOrderBook, UnifiedTicker

class PublicMarketDataParserV1:
    def ticker_from_payload(self, exchange: SupportedExchange, symbol: str, payload: dict) -> UnifiedTicker:
        data = payload.get("data", payload)
        if isinstance(data, list) and data:
            data = data[0]
        if not isinstance(data, dict):
            data = {}

        price = data.get("lastPrice") or data.get("last") or data.get("price") or data.get("close") or data.get("c") or 0
        change = data.get("priceChangePercent") or data.get("changePercent") or data.get("change") or data.get("P") or 0
        volume = data.get("volume") or data.get("vol") or data.get("v") or 0

        return UnifiedTicker(
            exchange=exchange,
            symbol=symbol,
            price=float(price or 0),
            change_percent=float(change or 0),
            volume=float(volume or 0),
            raw=payload,
        )

    def order_book_from_payload(self, exchange: SupportedExchange, symbol: str, payload: dict) -> UnifiedOrderBook:
        data = payload.get("data", payload)
        if not isinstance(data, dict):
            data = {}
        return UnifiedOrderBook(
            exchange=exchange,
            symbol=symbol,
            bids=self._levels(data.get("bids") or data.get("b") or []),
            asks=self._levels(data.get("asks") or data.get("a") or []),
            raw=payload,
        )

    def _levels(self, rows) -> list[list[float]]:
        levels = []
        for row in rows or []:
            if isinstance(row, dict):
                price = row.get("price") or row.get("p") or row.get("0")
                qty = row.get("quantity") or row.get("qty") or row.get("size") or row.get("q") or row.get("1")
            else:
                price = row[0] if len(row) > 0 else 0
                qty = row[1] if len(row) > 1 else 0
            levels.append([float(price or 0), float(qty or 0)])
        return levels
