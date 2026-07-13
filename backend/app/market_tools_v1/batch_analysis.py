from pydantic import BaseModel, Field
from app.market_tools_v1.regime import MarketRegimeDetectorV1
from app.market_tools_v1.volatility import VolatilityMonitorV1

class BatchSymbolAnalysisInputV1(BaseModel):
    symbol: str
    closes: list[float] = Field(default_factory=list)

class BatchSymbolAnalysisResultV1(BaseModel):
    symbol: str
    regime: str
    volatility_level: str

class BatchMarketAnalyzerV1:
    def __init__(self):
        self.regime = MarketRegimeDetectorV1()
        self.volatility = VolatilityMonitorV1()

    def analyze(self, items: list[BatchSymbolAnalysisInputV1]) -> list[BatchSymbolAnalysisResultV1]:
        result = []
        for item in items:
            regime = self.regime.detect(item.closes)
            vol = self.volatility.calculate(item.closes)
            result.append(BatchSymbolAnalysisResultV1(symbol=item.symbol, regime=regime.regime, volatility_level=vol.level))
        return result
