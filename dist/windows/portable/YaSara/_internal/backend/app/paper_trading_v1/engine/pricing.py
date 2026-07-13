from app.paper_trading_v1.domain.models import PaperOrderRequest, PaperOrderSide

class PaperPricingEngineV1:
    def fill_price(self, request: PaperOrderRequest, market_price: float, slippage_rate: float = 0.0002) -> float:
        base = request.price if request.price is not None else market_price
        if request.side == PaperOrderSide.BUY:
            return base * (1 + slippage_rate)
        return base * (1 - slippage_rate)
