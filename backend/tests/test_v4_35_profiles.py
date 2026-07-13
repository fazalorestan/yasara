from app.platform_core.config_center.profiles import EnvironmentProfileRegistry

def test_v435_profiles():
    r = EnvironmentProfileRegistry()
    profiles = r.seed_defaults()
    assert "local" in profiles
    assert profiles["production"]["values"]["live_execution_enabled"] is False
