class CriticalReviewFacade:
    def summary(self):
        return {
            "ready": True,
            "scope": "critical_review_only",
            "adds_user_feature": False,
            "fail_closed_required": True,
            "signal_only_supported": True,
            "auto_trading_independent": True,
        }

    def trading_mode(self, auto_trading_enabled=False, signal_only_mode=True):
        auto = bool(auto_trading_enabled)
        signal_only = bool(signal_only_mode)
        if signal_only:
            auto = False
        return {
            "auto_trading_enabled": auto,
            "signal_only_mode": signal_only,
            "allow_new_order": auto and not signal_only,
        }

    def correlation_health(self, payload):
        valid = bool(payload) and payload.get("valid") is True
        if not valid:
            return {
                "ready": False,
                "valid": False,
                "allow_new_order": False,
                "auto_trading_enabled": False,
                "signal_only_mode": True,
                "dashboard_warning": "CORRELATION_ENGINE_INVALID_DATA",
                "telegram_alert_required": True,
                "log_required": True,
            }
        return {
            "ready": True,
            "valid": True,
            "allow_new_order": True,
            "auto_trading_enabled": True,
            "signal_only_mode": False,
            "dashboard_warning": None,
            "telegram_alert_required": False,
            "log_required": True,
        }

    def fail_closed(self, module_health):
        critical = ("risk_engine", "correlation_engine", "position_manager", "exchange", "database")
        failed = [m for m in critical if module_health.get(m) is not True]
        if failed:
            return {
                "auto_trading_enabled": False,
                "signal_only_mode": True,
                "allow_new_order": False,
                "notification_required": True,
                "dashboard_warning": "CRITICAL_MODULE_FAILURE: " + ",".join(failed),
                "telegram_alert_required": True,
                "log_required": True,
                "failed_modules": failed,
            }
        return {
            "auto_trading_enabled": True,
            "signal_only_mode": False,
            "allow_new_order": True,
            "notification_required": False,
            "dashboard_warning": None,
            "telegram_alert_required": False,
            "log_required": True,
            "failed_modules": [],
        }

critical_review_facade = CriticalReviewFacade()
