from pydantic import BaseModel, Field

class OrderBookLevelViewV1(BaseModel):
    price: float
    quantity: float
    total: float

class OrderBookViewV1(BaseModel):
    bids: list[OrderBookLevelViewV1] = Field(default_factory=list)
    asks: list[OrderBookLevelViewV1] = Field(default_factory=list)

class OrderBookViewBuilderV1:
    def build(self, bids: list[list[float]], asks: list[list[float]]) -> OrderBookViewV1:
        return OrderBookViewV1(
            bids=[OrderBookLevelViewV1(price=p, quantity=q, total=p*q) for p, q in bids],
            asks=[OrderBookLevelViewV1(price=p, quantity=q, total=p*q) for p, q in asks],
        )
