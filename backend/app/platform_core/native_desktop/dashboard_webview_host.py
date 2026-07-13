class DashboardWebViewHost:
    def configuration(self):
        return {
            "ready": True,
            "url": "http://127.0.0.1:8000/api/v1/v5-0-alpha-47/build-dashboard/report",
            "health_url": "http://127.0.0.1:8000/api/v1/v5-0-alpha-48/windows-builder/readiness",
            "local_content_only": True,
            "external_navigation_allowed": False,
            "hardcoded_dashboard_data": False,
        }

dashboard_webview_host = DashboardWebViewHost()
