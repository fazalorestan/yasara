from app.platform_core.production_runtime.session_manager import RuntimeSessionManager

def test_session(): assert RuntimeSessionManager().session()['active'] is True
