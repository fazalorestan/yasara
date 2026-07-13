class DesktopStatusBarContract:
    def status_bar(self):
        return {
            "ready": True,
            "fields": ["build_id", "tests", "health", "mode", "backend"],
            "shows_signal_only": True,
            "shows_auto_trading": True,
            "shows_backend_status": True,
        }

desktop_status_bar_contract = DesktopStatusBarContract()
