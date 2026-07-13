from app.platform_core.production_runtime.runtime_safety import RuntimeSafetyPolicy

def test_safety(): assert RuntimeSafetyPolicy().policy()['real_execution_enabled'] is False
