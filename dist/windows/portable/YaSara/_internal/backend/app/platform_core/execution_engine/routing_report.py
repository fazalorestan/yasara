from app.platform_core.execution_engine.idempotency import execution_idempotency_guard
from app.platform_core.execution_engine.order_router_contract import order_router_contract_service
from app.platform_core.execution_engine.order_validator import order_validator_service
from app.platform_core.execution_engine.pre_trade_checks import pre_trade_check_service
from app.platform_core.execution_engine.routing_safety import order_routing_safety_policy

class OrderRoutingReport:
    def report(self):
        order = {"symbol": "BTCUSDT", "side": "hold", "quantity": 0.0, "order_type": "market"}
        return {
            "ready": True,
            "validation": order_validator_service.validate(order),
            "router_contract": order_router_contract_service.contract(),
            "dry_route": order_router_contract_service.dry_route(order),
            "pre_trade_checks": pre_trade_check_service.run(),
            "idempotency": execution_idempotency_guard.check(),
            "safety": order_routing_safety_policy.policy(),
            "real_execution_enabled": False,
            "broker_connection_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

order_routing_report = OrderRoutingReport()
