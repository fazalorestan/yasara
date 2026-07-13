from app.platform_core.windows_app.main_window_contract import WindowsMainWindowContract

def test_window(): assert WindowsMainWindowContract().contract()['live_dashboard_default'] is True
