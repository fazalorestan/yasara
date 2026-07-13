from pydantic import BaseModel

class ScenarioInputV1(BaseModel):
    current_equity: float
    price_change_percent: float
    exposure: float

class ScenarioResultV1(BaseModel):
    estimated_pnl: float
    estimated_equity: float

class ScenarioSimulatorV1:
    def simulate(self, item: ScenarioInputV1) -> ScenarioResultV1:
        pnl = item.exposure * item.price_change_percent / 100
        return ScenarioResultV1(estimated_pnl=pnl, estimated_equity=item.current_equity + pnl)
