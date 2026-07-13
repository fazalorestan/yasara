from pydantic import BaseModel, Field

class HistoricalSeriesV1(BaseModel):
    key: str
    rows: list[dict] = Field(default_factory=list)

class HistoricalCacheV1:
    def __init__(self):
        self.series: dict[str, HistoricalSeriesV1] = {}

    def put(self, key: str, rows: list[dict]) -> HistoricalSeriesV1:
        item = HistoricalSeriesV1(key=key, rows=rows)
        self.series[key] = item
        return item

    def get(self, key: str) -> HistoricalSeriesV1 | None:
        return self.series.get(key)

    def append(self, key: str, rows: list[dict]) -> HistoricalSeriesV1:
        current = self.series.get(key) or HistoricalSeriesV1(key=key)
        current.rows.extend(rows)
        self.series[key] = current
        return current
