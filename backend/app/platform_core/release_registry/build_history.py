class BuildHistoryRegistry:
    def history(self):
        return {
            "ready": True,
            "latest_build_id": "2026.47.C.001",
            "history": [
                {"build_id": "2026.47.A.001", "status": "passed"},
                {"build_id": "2026.47.B.001", "status": "passed"},
                {"build_id": "2026.47.C.001", "status": "foundation_ready"},
            ],
            "last_successful_build": "2026.47.B.001",
            "last_failed_build": None,
        }

build_history_registry = BuildHistoryRegistry()
