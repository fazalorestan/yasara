from app.platform_core.api_search.search import api_endpoint_search_service
from app.platform_core.api_search.visibility import runtime_api_visibility_report
from app.platform_core.startup.self_test import startup_self_test

class LauncherSwaggerSearchReadinessGate:
    def run(self):
        startup = startup_self_test.run()
        search = api_endpoint_search_service.find("exchange")
        visibility = runtime_api_visibility_report.report()
        ready = startup["ready"] and search["ready"] and visibility["ready"]
        return {"ready": ready, "score": 100.0 if ready else 0.0, "startup": startup, "search": search, "visibility": visibility, "execution_allowed": False}

launcher_swagger_search_readiness_gate = LauncherSwaggerSearchReadinessGate()
