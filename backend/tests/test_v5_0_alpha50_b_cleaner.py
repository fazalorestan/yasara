from app.platform_core.windows_exe_build.dist_cleaner import WindowsDistCleaner

def test_cleaner(): assert WindowsDistCleaner().plan()['dry_run'] is True
