from app.platform_core.windows_exe_build.build_log import WindowsBuildLogContract

def test_log(): assert WindowsBuildLogContract().log()['captures_return_code'] is True
