class BrokerOrderValidationService:
    def validate(self, order: dict):
        errors = []
        if not order.get("symbol"):
            errors.append("missing_symbol")
        if order.get("side") not in ["buy", "sell"]:
            errors.append("invalid_side")
        if order.get("type") not in ["market", "limit"]:
            errors.append("invalid_type")
        if float(order.get("quantity", 0.0)) <= 0:
            errors.append("invalid_quantity")
        if order.get("type") == "limit" and float(order.get("price", 0.0)) <= 0:
            errors.append("invalid_price")
        return {"ready": True, "valid": len(errors) == 0, "errors": errors, "execution_allowed": False}

broker_order_validation_service = BrokerOrderValidationService()
