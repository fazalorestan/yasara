class DesktopWindowStatePersistence:
    def state(self):
        return {
            "ready": True,
            "persistence_enabled": True,
            "persisted_fields": ["width", "height", "position", "active_workspace", "open_tabs"],
            "destructive_write_allowed": False,
            "backup_before_write_required": True,
        }

desktop_window_state_persistence = DesktopWindowStatePersistence()
