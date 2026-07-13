from app.platform_core.desktop_app.project_health_engine import DesktopProjectHealthEngine

def test_health(): assert DesktopProjectHealthEngine().health()['project_health']=='green'
