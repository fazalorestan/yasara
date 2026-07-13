from app.platform_core.release_candidate.safety_toggle_policy import SafetyTogglePolicy

def test_safety_policy():
 r=SafetyTogglePolicy().apply_failure('database'); assert r['auto_trading_enabled'] is False and r['manual_reenable_required'] is True
