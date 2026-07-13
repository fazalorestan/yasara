from app.v11_alerts.models import AlertRuleTypeV11, AlertRuleV11
from app.v11_alerts.store import AlertStoreV11

def test_alert_store():
    store = AlertStoreV11()
    rule = store.add_rule(AlertRuleV11(name="test", rule_type=AlertRuleTypeV11.PRICE_ABOVE, symbol="BTCUSDT", threshold=1))
    assert store.list_rules()[0].rule_id == rule.rule_id
