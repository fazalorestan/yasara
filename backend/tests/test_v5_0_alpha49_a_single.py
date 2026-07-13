from app.platform_core.native_desktop.single_instance_guard import WindowsSingleInstanceGuard

def test_single(): assert WindowsSingleInstanceGuard().policy()['enabled'] is True
