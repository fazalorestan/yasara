from app.platform_core.desktop_gui.ci_panel import CIPanelContract

def test_ci(): assert CIPanelContract().panel()['tests_failed'] == 0
