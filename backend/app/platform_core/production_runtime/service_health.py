class RuntimeServiceHealthContract:
    def health(self):
        return {
            "ready": True,
            "services_healthy": True,
            "degraded_services": [],
            "failed_services": [],
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

runtime_service_health_contract = RuntimeServiceHealthContract()
