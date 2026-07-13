from app.platform_core.release_registry.build_history import build_history_registry

class BuildTimelineProvider:
    def timeline(self):
        history = build_history_registry.history()
        return {
            "ready": True,
            "latest_build_id": history["latest_build_id"],
            "events": history["history"],
            "last_successful_build": history["last_successful_build"],
            "last_failed_build": history["last_failed_build"],
            "source": "build_history_registry",
            "hardcoded_dashboard": False,
        }

build_timeline_provider = BuildTimelineProvider()
