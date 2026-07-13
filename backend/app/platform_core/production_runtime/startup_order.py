class RuntimeStartupOrderPlanner:
    def plan(self):
        return {
            "ready": True,
            "startup_order": ["runtime", "pic", "dashboard", "strategy", "execution", "broker"],
            "commercial_startup_order": ["runtime", "pic", "dashboard", "strategy", "broker"],
            "commercial_execution_engine_enabled": False,
            "real_execution_enabled": False,
        }

runtime_startup_order_planner = RuntimeStartupOrderPlanner()
