class ModuleStateRegistry:
    def snapshot(self):
        return {
            "ready": True,
            "completed_modules": ["AI Intelligence Layer", "Strategy Engine", "Execution Engine", "Broker Layer"],
            "active_modules": ["Project Intelligence Center"],
            "remaining_modules": ["Live Dashboard Backend", "Build Intelligence", "Desktop Dashboard", "Dashboard Automation"],
            "completed_files": 0,
            "remaining_files": 0,
        }
module_state_registry = ModuleStateRegistry()
