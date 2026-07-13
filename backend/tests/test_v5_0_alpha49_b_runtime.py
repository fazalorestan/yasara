from app.platform_core.desktop_gui.runtime_panel import RuntimePanelContract

def test_runtime(): assert RuntimePanelContract().panel()['auto_trading_enabled'] is False
