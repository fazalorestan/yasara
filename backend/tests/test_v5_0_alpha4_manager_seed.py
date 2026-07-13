from app.platform_core.indicators.lifecycle.manager import IndicatorLifecycleStateManager

def test_v500_alpha4_manager_seed():
    m = IndicatorLifecycleStateManager()
    states = m.seed_defaults()
    assert states["yasara"]["state"] == "enabled"
