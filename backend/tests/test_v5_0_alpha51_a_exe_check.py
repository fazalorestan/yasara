from app.platform_core.windows_exe_smoke_build.exe_existence_check import WindowsExeExistenceCheck

def test_exe_check(): assert WindowsExeExistenceCheck().check()['required_for_smoke'] is True
