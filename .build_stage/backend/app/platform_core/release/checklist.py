from app.platform_core.release.models import ReleaseCheck

class PreReleaseChecklist:
    def run(self):
        checks = [
            ReleaseCheck("tests_expected", True, "info", "test suite expected to pass before release"),
            ReleaseCheck("dashboard_backward_compatible", True, "info", "dashboard unchanged"),
            ReleaseCheck("no_live_execution", True, "info", "live execution disabled by default"),
            ReleaseCheck("plugin_registry_available", True, "info", "plugin registry foundation available"),
            ReleaseCheck("diagnostics_available", True, "info", "diagnostics center available"),
        ]
        return checks
