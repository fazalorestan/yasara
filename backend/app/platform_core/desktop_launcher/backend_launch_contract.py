class BackendLaunchContract:
    def contract(self):
        return {
            "ready": True,
            "command": "python -m uvicorn app.main:app --host 127.0.0.1 --port 8000",
            "working_directory": "backend",
            "loopback_only": True,
            "wait_for_health": True,
            "health_timeout_seconds": 20,
            "fail_closed_on_error": True,
            "allow_orders_before_health": False,
        }

backend_launch_contract = BackendLaunchContract()
