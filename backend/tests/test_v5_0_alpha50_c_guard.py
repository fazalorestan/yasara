from app.platform_core.windows_packaging_enablement.execute_guard import PackagingExecuteGuard

def test_guard(): assert PackagingExecuteGuard().guard()['requires_user_flag']=='--execute'
