class SafetyTogglePolicy:
    def apply_failure(self, failed_module):
        return {
            'ready': True,
            'failed_module': failed_module,
            'auto_trading_enabled': False,
            'signal_only_mode': True,
            'manual_reenable_required': True,
            'dashboard_warning': f'Auto Trading Disabled by Safety System: {failed_module}',
            'telegram_alert_required': True,
            'log_required': True,
            'system_can_enable_automatically': False
        }
safety_toggle_policy = SafetyTogglePolicy()
