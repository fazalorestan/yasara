from app.platform_core.startup.self_test import StartupSelfTest

def test_v500_alpha20_startup_self_test():
    assert StartupSelfTest().run()['ready'] is True
