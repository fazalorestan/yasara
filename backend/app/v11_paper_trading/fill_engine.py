from app.v11_paper_trading.models import PaperOrderRequestV11


class PaperFillEngineV11:
    def resolve_fill_price(self, request: PaperOrderRequestV11, market_price: float | None = None) -> float:
        if request.order_type.value == "limit" and request.price:
            return request.price
        if market_price and market_price > 0:
            return market_price
        if request.price and request.price > 0:
            return request.price
        return 100.0
