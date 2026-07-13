class BrokerOrderValidator:
    def validate(self, payload: dict):
        errors = []
        for key in ["symbol", "side", "order_type", "quantity"]:
            if key not in payload:
                errors.append(f"missing_{key}")
        if payload.get("side") and payload.get("side") not in ["buy", "sell"]:
            errors.append("invalid_side")
        if payload.get("order_type") and payload.get("order_type") not in ["market", "limit"]:
            errors.append("unsupported_order_type")
        try:
            if "quantity" in payload and float(payload["quantity"]) <= 0:
                errors.append("invalid_quantity")
        except Exception:
            errors.append("invalid_quantity")
        if payload.get("order_type") == "limit" and payload.get("price") is None:
            errors.append("missing_price_for_limit_order")
        return {"valid": len(errors) == 0, "errors": errors}
broker_order_validator = BrokerOrderValidator()
