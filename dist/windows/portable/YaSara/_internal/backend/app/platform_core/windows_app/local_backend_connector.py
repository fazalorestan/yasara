class WindowsLocalBackendConnector:
    def connector(self):
        return {
            "ready": True,
            "backend_url": "http://127.0.0.1:8000",
            "health_endpoint": "/api/v1/v5-0-alpha-47/production-readiness/summary",
            "critical_review_endpoint": "/api/v1/v5-0-alpha-47/critical-review/summary",
            "dashboard_endpoint": "/api/v1/v5-0-alpha-47/build-dashboard/report",
            "connection_mode": "local_loopback",
            "external_network_required": False,
        }

windows_local_backend_connector = WindowsLocalBackendConnector()
