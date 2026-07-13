from app.platform_core.desktop_app.test_statistics_engine import DesktopTestStatisticsEngine

def test_tests(): assert DesktopTestStatisticsEngine().statistics()['failed'] == 0
