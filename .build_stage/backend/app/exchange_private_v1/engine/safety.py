from app.exchange_private_v1.domain.models import PrivateOrderRequest

class PrivateExchangeSafetyGateV1:
    def validate_order(self, request: PrivateOrderRequest) -> list[str]:
        errors = []
        if request.quantity <= 0:
            errors.append("Quantity must be positive.")
        if request.order_type == "LIMIT" and request.price is None:
            errors.append("Limit order requires price.")
        if not request.dry_run:
            errors.append("Live private exchange order placement is disabled in Sprint 12.")
        if request.credential_ref is None:
            errors.append("Credential reference is required.")
        return errors
