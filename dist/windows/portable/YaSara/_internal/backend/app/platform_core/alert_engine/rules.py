class AlertRuleRegistry:
    def default_rules(self):
        return [
            {"rule_id": "scanner_high_score", "name": "Scanner High Score", "condition": "score>=80", "severity": "warning", "enabled": True},
            {"rule_id": "risk_blocked", "name": "Risk Blocked", "condition": "risk_allowed=false", "severity": "critical", "enabled": True},
            {"rule_id": "portfolio_exposure", "name": "Portfolio Exposure", "condition": "exposure>60", "severity": "warning", "enabled": True},
        ]

alert_rule_registry = AlertRuleRegistry()
