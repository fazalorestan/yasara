from app.platform_core.broker_layer.order_validation import broker_order_validation_service
from app.platform_core.broker_layer.orders import broker_order_contract_service
from app.platform_core.broker_layer.safety import broker_execution_safety_contract

class BrokerOrderPreviewService:
    def preview(self, order: dict | None = None):
        order = order or broker_order_contract_service.sample_order()
        normalized = broker_order_contract_service.normalize(order)["order"]
        validation = broker_order_validation_service.validate(normalized)
        safety = broker_execution_safety_contract.can_execute()
        notional = normalized["quantity"] * (normalized["price"] or 0.0)
        return {"ready": validation["ready"], "normalized_order": normalized, "validation": validation, "notional": notional, "dry_run": True, "execution_allowed": safety["allowed"]}

broker_order_preview_service = BrokerOrderPreviewService()
