from app.platform_core.production_runtime.runtime_mode import RuntimeModeResolver

def test_personal(): assert RuntimeModeResolver().resolve('personal')['execution_engine_enabled'] is True
