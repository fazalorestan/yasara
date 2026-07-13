from app.platform_core.licensing.ui.countdown import DemoCountdownContract
def test_v500_alpha13_countdown_bad():
    assert DemoCountdownContract().remaining_days("bad") == 0
