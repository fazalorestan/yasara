from app.v11_alerts.models import AlertRuleV11, AlertRuleTypeV11, AlertSeverityV11, AlertsSnapshotV11
from app.v11_alerts.notification_center import NotificationCenterV11
from app.v11_alerts.rule_engine import AlertRuleEngineV11
from app.v11_alerts.store import AlertStoreV11


class AlertsNotificationServiceV11:
    def __init__(self):
        self.store = AlertStoreV11()
        self.engine = AlertRuleEngineV11()
        self.notifications = NotificationCenterV11()

    def create_price_rule(self, symbol: str, above: float | None = None, below: float | None = None) -> AlertRuleV11:
        if above is not None:
            rule = AlertRuleV11(
                name=f"{symbol} above {above}",
                rule_type=AlertRuleTypeV11.PRICE_ABOVE,
                symbol=symbol.upper(),
                threshold=above,
                severity=AlertSeverityV11.WARNING,
            )
        else:
            rule = AlertRuleV11(
                name=f"{symbol} below {below}",
                rule_type=AlertRuleTypeV11.PRICE_BELOW,
                symbol=symbol.upper(),
                threshold=below,
                severity=AlertSeverityV11.WARNING,
            )
        return self.store.add_rule(rule)

    def evaluate_price(self, symbol: str, price: float):
        events = []
        for rule in self.store.list_rules():
            event = self.engine.evaluate_market_price(rule, symbol, price)
            if event:
                self.store.add_event(event)
                self.notifications.deliver(event)
                events.append(event)
        return events

    def emit_risk_block(self, message: str, symbol: str | None = None):
        event = self.engine.risk_block(message, symbol)
        self.store.add_event(event)
        self.notifications.deliver(event)
        return event

    def demo(self) -> AlertsSnapshotV11:
        self.create_price_rule("BTCUSDT", above=50000)
        self.evaluate_price("BTCUSDT", 51000)
        self.emit_risk_block("Paper order blocked by risk guard", "BTCUSDT")
        return self.snapshot()

    def snapshot(self) -> AlertsSnapshotV11:
        return AlertsSnapshotV11(
            ready=True,
            rules=self.store.list_rules(),
            events=self.store.recent_events(),
            deliveries=self.notifications.recent(),
        )
