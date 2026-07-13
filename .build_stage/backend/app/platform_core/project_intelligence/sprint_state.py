class SprintStateRegistry:
    def snapshot(self):
        return {
            "ready": True,
            "current_sprint": "v5.0-alpha.44",
            "current_package": "A",
            "next_package": "B",
            "completed_modules": ["AI Intelligence Layer", "Strategy Engine", "Execution Engine", "Broker Layer"],
            "active_modules": ["Project Intelligence Center"],
            "remaining_modules": ["Live Dashboard Backend", "Build Intelligence", "Desktop Dashboard", "Dashboard Automation"],
        }
sprint_state_registry = SprintStateRegistry()
