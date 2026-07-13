class BrokerConnectionStatusService:
    def status(self):
        return {
            "ready": True,
            "connected": False,
            "connection_mode": "dry",
            "real_broker_connection_enabled": False,
            "last_check": 0,
            "execution_allowed": False,
        }

broker_connection_status_service = BrokerConnectionStatusService()
