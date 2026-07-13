from app.platform_core.desktop_app.ui_quality_gate import DesktopUIQualityGate

def test_quality(): assert DesktopUIQualityGate().evaluate()["score"] >= 9.5
