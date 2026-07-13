from pydantic import BaseModel

class VolatilityResultV1(BaseModel):
    volatility_percent: float
    level: str

class VolatilityMonitorV1:
    def calculate(self, closes: list[float]) -> VolatilityResultV1:
        if len(closes) < 2:
            return VolatilityResultV1(volatility_percent=0, level="low")
        mean = sum(closes) / len(closes)
        variance = sum((x - mean) ** 2 for x in closes) / len(closes)
        vol = (variance ** 0.5) / mean * 100 if mean else 0
        level = "high" if vol >= 5 else "medium" if vol >= 2 else "low"
        return VolatilityResultV1(volatility_percent=vol, level=level)
