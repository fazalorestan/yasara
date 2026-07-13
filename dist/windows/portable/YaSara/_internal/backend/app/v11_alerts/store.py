from app.v11_alerts.models import AlertEventV11, AlertRuleV11


class AlertStoreV11:
    def __init__(self):
        self.rules: list[AlertRuleV11] = []
        self.events: list[AlertEventV11] = []

    def add_rule(self, rule: AlertRuleV11) -> AlertRuleV11:
        self.rules.append(rule)
        return rule

    def add_event(self, event: AlertEventV11) -> AlertEventV11:
        self.events.append(event)
        return event

    def list_rules(self) -> list[AlertRuleV11]:
        return self.rules

    def recent_events(self, limit: int = 50) -> list[AlertEventV11]:
        return self.events[-limit:]
