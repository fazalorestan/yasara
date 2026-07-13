from pydantic import BaseModel

class LatencySampleV1(BaseModel):
    exchange: str
    latency_ms: float

class LatencyReportV1(BaseModel):
    exchange: str
    average_ms: float
    max_ms: float
    level: str

class LatencyMonitorV1:
    def report(self, exchange: str, samples: list[LatencySampleV1]) -> LatencyReportV1:
        values = [s.latency_ms for s in samples if s.exchange == exchange]
        if not values:
            return LatencyReportV1(exchange=exchange, average_ms=0, max_ms=0, level="unknown")
        avg = sum(values) / len(values)
        max_latency = max(values)
        level = "high" if avg >= 1000 else "medium" if avg >= 300 else "low"
        return LatencyReportV1(exchange=exchange, average_ms=avg, max_ms=max_latency, level=level)
