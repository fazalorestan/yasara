from app.platform_core.desktop_gui.build_panel import BuildPanelContract

def test_build(): assert BuildPanelContract().panel()['final_exe_generated'] is False
