from app.platform_core.windows_builder.smoke_test import WindowsBuildSmokeTestContract

def test_smoke():
 assert WindowsBuildSmokeTestContract().run()['smoke_test_passed'] is True
