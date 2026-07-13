from app.platform_core.desktop_launcher.smoke_test_runner import DesktopSmokeTestRunnerContract

def test_smoke(): assert DesktopSmokeTestRunnerContract().run()['smoke_test_passed'] is True
