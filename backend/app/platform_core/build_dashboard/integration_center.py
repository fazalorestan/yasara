from app.platform_core.build_pipeline.build_dashboard_provider import build_dashboard_provider
from app.platform_core.ci_pipeline.ci_dashboard_provider import ci_dashboard_provider
from app.platform_core.release_registry.release_dashboard_provider import release_dashboard_provider

class BuildDashboardIntegrationCenter:
    def dashboard(self):
        return {
            "ready": True,
            "build": build_dashboard_provider.dashboard(),
            "ci": ci_dashboard_provider.dashboard(),
            "release": release_dashboard_provider.dashboard(),
            "source": "build_ci_release_registries",
            "hardcoded_dashboard": False,
        }

build_dashboard_integration_center = BuildDashboardIntegrationCenter()
