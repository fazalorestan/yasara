from app.platform_core.licensing.trial import trial_policy
def test_v500_alpha9_trial_policy():
    p = trial_policy.policy()
    assert p["default_days"] == 30
    assert p["short_days"] == 14
    assert p["auto_trading_enabled"] is False
