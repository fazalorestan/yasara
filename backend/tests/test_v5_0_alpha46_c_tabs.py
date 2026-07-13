from app.platform_core.desktop_app.tab_manager import DesktopTabManager

def test_tabs(): assert DesktopTabManager().tabs()['default_tab']=='dashboard'
