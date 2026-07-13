from datetime import datetime, timezone
class BuildStateRegistry:
    def snapshot(self):
        return {
            "ready": True,
            "last_build_time": datetime.now(timezone.utc).isoformat(),
            "last_build_status": "registry_initialized",
            "windows_exe_available": False,
            "android_build_available": False,
            "ios_build_available": False,
            "web_build_available": False,
        }
build_state_registry = BuildStateRegistry()
