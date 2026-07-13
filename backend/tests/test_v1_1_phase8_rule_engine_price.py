from app.v11_alerts.models import AlertRuleTypeV11, AlertRuleV11
from app.v11_alerts.rule_engine import AlertRuleEngineV11

def test_price_alert_rule_engine():
    rule = AlertRuleV11(name="BTC above", rule_type=AlertRuleTypeV11.PRICE_ABOVE, symbol="BTCUSDT", threshold=50000)
    event = AlertRuleEngineV11().evaluate_market_price(rule, "BTCUSDT", 51000)
    assert event is not None
    assert event.source.value == "market"
