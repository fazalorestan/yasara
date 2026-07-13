class ProjectStateRegistry:
    def snapshot(self):
        return {
            "ready": True,
            "project": "YaSara OS",
            "current_version": "v5.0-alpha.44",
            "current_sprint": "v5.0-alpha.44",
            "current_package": "A",
            "last_completed_sprint": "v5.0-alpha.43",
            "last_known_tests_passed": 4128,
            "project_progress_percent": 78.0,
            "windows_progress_percent": 86.0,
            "android_progress_percent": 30.0,
            "ios_progress_percent": 25.0,
            "web_progress_percent": 45.0,
            "real_execution_enabled": False,
            "real_broker_connection_enabled": False,
        }
project_state_registry = ProjectStateRegistry()
