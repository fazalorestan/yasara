class OrderLifecycleService:
    def lifecycle(self):
        return {
            "ready": True,
            "order_id": "dry-order-001",
            "states": ["created", "validated", "routed", "dry_executed", "journaled"],
            "current_state": "journaled",
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

order_lifecycle_service = OrderLifecycleService()
