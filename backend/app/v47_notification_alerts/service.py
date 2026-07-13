from app.v42_signal_engine.service import MultiLayerSignalEngineServiceV42
from app.v43_risk_engine.service import AdvancedRiskEngineServiceV43
from app.v47_notification_alerts.channels import NotificationChannelRegistryV47
from app.v47_notification_alerts.models import AlertEventV47, AlertRuleV47, NotificationAlertSummaryV47, SignalAlertRequestV47
from app.v47_notification_alerts.store import NotificationAlertStoreV47


class NotificationAlertEngineServiceV47:
    def __init__(self):
        self.store = NotificationAlertStoreV47()
        self.channels = NotificationChannelRegistryV47()
        self.signal = MultiLayerSignalEngineServiceV42()
        self.risk = AdvancedRiskEngineServiceV43()

    def summary(self):
        return NotificationAlertSummaryV47()

    def channel_status(self):
        return self.channels.status()

    def add_rule(self, rule: AlertRuleV47):
        return {"ready": True, "rule": self.store.add_rule(rule), "live_trading_enabled": False}

    def rules(self):
        return {"ready": True, "items": self.store.rules(), "live_trading_enabled": False}

    def create_alert(self, alert: AlertEventV47):
        item = self.store.add_alert(alert)
        deliveries = self.channels.dispatch(alert)
        return {
            "ready": True,
            "alert": item,
            "deliveries": deliveries,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def alerts(self):
        return {"ready": True, "items": self.store.alerts(), "live_trading_enabled": False}

    def signal_alert_preview(self, request: SignalAlertRequestV47):
        signal = self.signal.quick(symbol=request.symbol, exchange=request.exchange, timeframe=request.timeframe)
        confidence = signal["signal"]["confidence"]
        should_alert = confidence >= request.min_confidence and signal["signal"]["action"] != "wait"
        severity = "critical" if confidence >= 85 else "warning" if confidence >= 70 else "info"
        alert = None

        if should_alert:
            alert = AlertEventV47(
                id=f"signal-{request.symbol}-{len(self.store.alerts())+1}",
                title=f"YaSara Signal {signal['signal']['action'].upper()} {request.symbol}",
                message=f"Signal confidence={confidence}, risk={signal['signal']['risk']}, action={signal['signal']['action']}",
                severity=severity,
                source="signal",
                channels=["desktop"],
            )
            result = self.create_alert(alert)
        else:
            result = {"ready": True, "alert": None, "deliveries": [], "reason": "signal_did_not_pass_alert_threshold"}

        return {
            "ready": True,
            "signal": signal["signal"],
            "should_alert": should_alert,
            "result": result,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }

    def risk_alert_preview(self, symbol="BTCUSDT", exchange="binance", timeframe="1m"):
        risk = self.risk.signal_risk(symbol=symbol, exchange=exchange, timeframe=timeframe)
        risk_label = risk["risk"]["guards"]["risk_label"]
        should_alert = risk_label == "high" or not risk["risk"]["guards"]["allowed"]

        if should_alert:
            result = self.create_alert(AlertEventV47(
                id=f"risk-{symbol}-{len(self.store.alerts())+1}",
                title=f"YaSara Risk Alert {symbol}",
                message=f"Risk label={risk_label}; allowed={risk['risk']['guards']['allowed']}",
                severity="critical" if risk_label == "high" else "warning",
                source="risk",
                channels=["desktop"],
            ))
        else:
            result = {"ready": True, "alert": None, "deliveries": [], "reason": "risk_ok"}

        return {
            "ready": True,
            "risk": risk["risk"]["guards"],
            "should_alert": should_alert,
            "result": result,
            "real_order_execution_enabled": False,
            "live_trading_enabled": False,
        }
