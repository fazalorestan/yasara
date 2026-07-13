class OrderRouterContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "order_router_contract",
            "methods": ["route", "dry_route", "validate_route", "report"],
            "broker_connection_enabled": False,
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

    def dry_route(self, order: dict | None = None):
        order = order or {"symbol": "BTCUSDT", "side": "hold", "quantity": 0.0}
        return {
            "ready": True,
            "order": order,
            "route": "dry_run_broker_adapter",
            "routed": True,
            "executed": False,
            "execution_allowed": False,
        }

order_router_contract_service = OrderRouterContractService()
