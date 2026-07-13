class BrokerCapabilityService:
    def capabilities(self):
        return {
            "ready": True,
            "supports_market_orders": True,
            "supports_limit_orders": True,
            "supports_real_orders": False,
            "supports_paper_orders": True,
            "supports_account_read": False,
            "execution_allowed": False,
        }

broker_capability_service = BrokerCapabilityService()
