from app.v11_alerts.models import AlertEventV11, AlertRuleTypeV11, AlertSourceV11, AlertSeverityV11, AlertRuleV11


class AlertRuleEngineV11:
    def evaluate_market_price(self, rule: AlertRuleV11, symbol: str, price: float) -> AlertEventV11 | None:
        if not rule.enabled or not rule.symbol:
            return None
        if rule.symbol.upper() != symbol.upper():
            return None
        if rule.rule_type == AlertRuleTypeV11.PRICE_ABOVE and rule.threshold is not None and price > rule.threshold:
            return AlertEventV11(
                source=AlertSourceV11.MARKET,
                severity=rule.severity,
                message=f"{symbol} price above {rule.threshold}",
                symbol=symbol.upper(),
                payload={"price": price, "threshold": rule.threshold, "rule_id": rule.rule_id},
            )
        if rule.rule_type == AlertRuleTypeV11.PRICE_BELOW and rule.threshold is not None and price < rule.threshold:
            return AlertEventV11(
                source=AlertSourceV11.MARKET,
                severity=rule.severity,
                message=f"{symbol} price below {rule.threshold}",
                symbol=symbol.upper(),
                payload={"price": price, "threshold": rule.threshold, "rule_id": rule.rule_id},
            )
        return None

    def risk_block(self, message: str, symbol: str | None = None, payload: dict | None = None) -> AlertEventV11:
        return AlertEventV11(
            source=AlertSourceV11.RISK,
            severity=AlertSeverityV11.CRITICAL,
            message=message,
            symbol=symbol,
            payload=payload or {},
        )

    def ai_signal(self, symbol: str, score: float, direction: str) -> AlertEventV11:
        severity = AlertSeverityV11.WARNING if score >= 0.7 else AlertSeverityV11.INFO
        return AlertEventV11(
            source=AlertSourceV11.AI,
            severity=severity,
            message=f"AI signal {direction} for {symbol} with score {score}",
            symbol=symbol.upper(),
            payload={"score": score, "direction": direction},
        )
