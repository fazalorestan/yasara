class NotificationChannelRegistryV47:
    def __init__(self):
        self.channels = {
            "desktop": {"enabled": True, "ready": True, "mode": "local_stub"},
            "telegram": {"enabled": False, "ready": True, "mode": "connector_ready"},
            "discord": {"enabled": False, "ready": True, "mode": "connector_ready"},
            "email": {"enabled": False, "ready": True, "mode": "connector_ready"},
            "push": {"enabled": False, "ready": True, "mode": "connector_ready"},
        }

    def status(self):
        return {"ready": True, "channels": self.channels, "live_trading_enabled": False}

    def dispatch(self, alert):
        deliveries = []
        for channel in alert.channels:
            meta = self.channels.get(channel, {"enabled": False, "ready": False, "mode": "unknown"})
            deliveries.append({
                "channel": channel,
                "accepted": bool(meta.get("ready")),
                "sent": bool(meta.get("enabled")),
                "mode": meta.get("mode"),
                "status": "queued" if meta.get("ready") else "unsupported",
            })
        return deliveries
