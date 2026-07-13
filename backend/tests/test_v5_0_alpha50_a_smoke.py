from app.platform_core.windows_real_exe.smoke_test import WindowsRealExeSmokeTestContract

def test_smoke(): assert WindowsRealExeSmokeTestContract().smoke()['requires_real_exe'] is True
