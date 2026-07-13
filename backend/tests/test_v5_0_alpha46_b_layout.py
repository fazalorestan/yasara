from app.platform_core.desktop_app.layout_engine import DesktopLayoutEngine

def test_layout(): assert 'workspace' in DesktopLayoutEngine().layout()['regions']
