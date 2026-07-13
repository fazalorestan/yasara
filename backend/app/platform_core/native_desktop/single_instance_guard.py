class WindowsSingleInstanceGuard:
    def policy(self):
        return {
            "ready": True,
            "enabled": True,
            "mutex_name": "YaSaraOS.Desktop.Singleton",
            "second_instance_action": "focus_existing_window",
            "parallel_backend_instances_allowed": False,
        }

windows_single_instance_guard = WindowsSingleInstanceGuard()
