from datetime import datetime, timezone
from app.multi_exchange_v1.domain.models import SupportedExchange, UnifiedKline

class OHLCVParserV1:
    def parse_rows(self, exchange: SupportedExchange, symbol: str, timeframe: str, payload: dict) -> list[UnifiedKline]:
        rows = payload.get("data", payload.get("rows", payload.get("klines", [])))
        if isinstance(rows, dict):
            rows = rows.get("items", [])
        result: list[UnifiedKline] = []
        for row in rows or []:
            result.append(self._parse_row(exchange, symbol, timeframe, row))
        return result

    def _parse_row(self, exchange: SupportedExchange, symbol: str, timeframe: str, row) -> UnifiedKline:
        if isinstance(row, dict):
            ts = row.get("openTime") or row.get("time") or row.get("t")
            open_ = row.get("open") or row.get("o")
            high = row.get("high") or row.get("h")
            low = row.get("low") or row.get("l")
            close = row.get("close") or row.get("c")
            volume = row.get("volume") or row.get("v") or 0
        else:
            ts = row[0] if len(row) > 0 else None
            open_ = row[1] if len(row) > 1 else 0
            high = row[2] if len(row) > 2 else 0
            low = row[3] if len(row) > 3 else 0
            close = row[4] if len(row) > 4 else 0
            volume = row[5] if len(row) > 5 else 0

        open_time = datetime.now(timezone.utc)
        if isinstance(ts, (int, float)):
            open_time = datetime.fromtimestamp(ts / 1000 if ts > 10_000_000_000 else ts, tz=timezone.utc)

        return UnifiedKline(
            exchange=exchange,
            symbol=symbol,
            timeframe=timeframe,
            open_time=open_time,
            open=float(open_ or 0),
            high=float(high or 0),
            low=float(low or 0),
            close=float(close or 0),
            volume=float(volume or 0),
            raw=row if isinstance(row, dict) else {"row": row},
        )
