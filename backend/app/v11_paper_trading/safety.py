from app.v11_paper_trading.models import PaperOrderRequestV11


class PaperTradingSafetyGuardV11:
    def __init__(self, max_quantity: float = 1000000.0):
        self.max_quantity = max_quantity

    def validate_order(self, request: PaperOrderRequestV11) -> tuple[bool, str]:
        if request.quantity <= 0:
            return False, "quantity_must_be_positive"
        if request.quantity > self.max_quantity:
            return False, "quantity_exceeds_paper_limit"
        if request.order_type.value == "limit" and (request.price is None or request.price <= 0):
            return False, "limit_order_requires_positive_price"
        return True, "ok"
