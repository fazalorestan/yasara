from app.platform_core.desktop_gui.health_panel import HealthPanelContract

def test_health(): assert HealthPanelContract().panel()['quality_signal']=='green'
