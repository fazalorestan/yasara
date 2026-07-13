from app.platform_core.production_runtime.crash_guard import RuntimeCrashGuardContract

def test_crash(): assert RuntimeCrashGuardContract().contract()['crash_detected'] is False
