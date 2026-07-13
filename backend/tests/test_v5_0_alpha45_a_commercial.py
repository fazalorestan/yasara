from app.platform_core.production_runtime.runtime_mode import RuntimeModeResolver

def test_commercial(): assert RuntimeModeResolver().resolve('commercial')['execution_engine_enabled'] is False
