class NativeMainWindowHost:
    def configuration(self):
        return {
            "ready": True,
            "title": "YaSara OS",
            "width": 1280,
            "height": 800,
            "min_width": 1024,
            "min_height": 700,
            "dashboard_default_view": True,
            "developer_tools_enabled": False,
            "signal_only_default": True,
            "auto_trading_enabled_default": False,
        }

native_main_window_host = NativeMainWindowHost()
