from pydantic import BaseModel

class PortfolioAssetInputV1(BaseModel):
    symbol: str
    expected_return: float
    risk_score: float

class PortfolioWeightV1(BaseModel):
    symbol: str
    weight: float

class PortfolioOptimizerV1:
    def optimize(self, assets: list[PortfolioAssetInputV1]) -> list[PortfolioWeightV1]:
        if not assets:
            return []
        raw = []
        for asset in assets:
            score = max(0.01, asset.expected_return / max(1, asset.risk_score))
            raw.append((asset.symbol, score))
        total = sum(score for _, score in raw) or 1
        return [PortfolioWeightV1(symbol=symbol, weight=score / total) for symbol, score in raw]
