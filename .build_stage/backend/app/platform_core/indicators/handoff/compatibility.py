class IndicatorCompatibilityMatrix:
    def matrix(self):
        return {
            "ready": True,
            "indicator": "yasara",
            "frontend_safe": True,
            "backend_safe": True,
            "dashboard_unchanged": True,
            "api_backward_compatible": True,
            "runtime_version": "v1.0",
            "settings_version": "v1.0",
            "source_language": "pine_script_v6_archive",
            "execution_allowed": False,
            "mode": "analysis_only",
        }

indicator_compatibility_matrix = IndicatorCompatibilityMatrix()
