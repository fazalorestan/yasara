class DesktopBackendProcessSupervisor:
    def policy(self):
        return {
            "ready": True,
            "command": "python -m uvicorn app.main:app --host 127.0.0.1 --port 8000",
            "working_directory": "backend",
            "loopback_only": True,
            "restart_on_crash": True,
            "max_restart_attempts": 3,
            "fail_closed": True,
            "allow_order_when_backend_unhealthy": False,
        }

desktop_backend_process_supervisor = DesktopBackendProcessSupervisor()
