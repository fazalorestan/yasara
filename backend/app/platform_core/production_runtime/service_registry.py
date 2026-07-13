class RuntimeServiceRegistry:
    def services(self):
        return {
            "ready": True,
            "services": [
                {"id": "pic", "name": "Project Intelligence Center", "required": True},
                {"id": "strategy", "name": "Strategy Engine", "required": True},
                {"id": "execution", "name": "Execution Engine", "required": False, "personal_only": True},
                {"id": "broker", "name": "Broker Layer", "required": True, "real_connection_enabled": False},
                {"id": "dashboard", "name": "Live Dashboard", "required": True},
            ],
            "count": 5,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }

runtime_service_registry = RuntimeServiceRegistry()
