from app.platform_core.desktop_app.dashboard_validation import DesktopDashboardValidationService

def test_validation(): assert DesktopDashboardValidationService().validate()["validated"] is True
