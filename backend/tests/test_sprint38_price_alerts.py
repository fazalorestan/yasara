from app.market_tools_v1.alerts import PriceAlertEngineV1, PriceAlertOperator, PriceAlertRuleV1

def test_price_alert_above_triggered():
    rule = PriceAlertRuleV1(alert_id="a1", symbol="BTC/USDT", operator=PriceAlertOperator.ABOVE, target_price=100)
    assert PriceAlertEngineV1().evaluate(rule, 101).triggered is True

def test_price_alert_below_not_triggered():
    rule = PriceAlertRuleV1(alert_id="a2", symbol="BTC/USDT", operator=PriceAlertOperator.BELOW, target_price=90)
    assert PriceAlertEngineV1().evaluate(rule, 100).triggered is False
