from app.platform_core.windows_exe_smoke_build.build_attempt import WindowsExeBuildAttemptContract

def test_attempt(): assert WindowsExeBuildAttemptContract().attempt()['requires_execute_flag'] is True
