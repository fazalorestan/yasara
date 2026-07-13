class WindowsMainWindowContract:
    def contract(self):
        return {
            "ready": True,
            "window_title": "YaSara OS",
            "default_width": 1280,
            "default_height": 800,
            "min_width": 1024,
            "min_height": 700,
            "live_dashboard_default": True,
            "hardcoded_dashboard": False,
        }

windows_main_window_contract = WindowsMainWindowContract()
