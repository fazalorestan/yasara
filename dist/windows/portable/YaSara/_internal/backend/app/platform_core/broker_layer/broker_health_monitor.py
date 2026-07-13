class BrokerHealthMonitorService:
    def health(self):
        return {
            "ready": True,
            "broker_id": "paper.broker",
            "status": "dry_healthy",
            "real_connection": False,
            "real_execution_enabled": False,
            "execution_allowed": False,
        }

broker_health_monitor_service = BrokerHealthMonitorService()
