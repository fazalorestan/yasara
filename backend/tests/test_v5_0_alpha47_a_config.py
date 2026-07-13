from app.platform_core.build_pipeline.config_loader import BuildConfigurationLoader

def test_config(): assert BuildConfigurationLoader().config()['hardcoded_api_keys_allowed'] is False
