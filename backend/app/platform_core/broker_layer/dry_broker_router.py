class DryBrokerRouterService:
    def route(self):
        return {"ready": True, "route": "paper.broker", "routed": True, "real_broker_connection": False, "real_order_submit": False, "execution_allowed": False}
dry_broker_router_service = DryBrokerRouterService()
