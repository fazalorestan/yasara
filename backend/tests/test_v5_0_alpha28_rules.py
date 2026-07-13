from app.platform_core.alert_engine.rules import AlertRuleRegistry

def test_v500_alpha28_rules(): assert len(AlertRuleRegistry().default_rules()) >= 3
