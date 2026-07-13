from pydantic import BaseModel

class WatchlistRowV1(BaseModel):
    symbol: str
    exchange: str
    price: float
    change_percent: float = 0

class WatchlistViewBuilderV1:
    def sort_by_change(self, rows: list[WatchlistRowV1], descending: bool = True) -> list[WatchlistRowV1]:
        return sorted(rows, key=lambda r: r.change_percent, reverse=descending)
