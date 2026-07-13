from app.platform_core.desktop_app.config_loader import DesktopConfigLoader

def test_config(): assert DesktopConfigLoader().config()['commercial_execution_engine_enabled'] is False
