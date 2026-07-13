from pydantic import BaseModel

class MarketContextInputV1(BaseModel):
    regime: str
    volatility_level: str
    liquidity_level: str

class MarketContextResultV1(BaseModel):
    context: str
    caution: bool

class MarketContextAIV1:
    def classify(self, item: MarketContextInputV1) -> MarketContextResultV1:
        caution = item.volatility_level == "high" or item.liquidity_level == "low"
        context = f"{item.regime}:{item.volatility_level}:{item.liquidity_level}"
        return MarketContextResultV1(context=context, caution=caution)
