from app.platform_core.release_candidate.manual_trading_toggle import manual_auto_trading_toggle_contract

class AutoTradingToggleDashboardContract:
    def dashboard(self):
        toggle = manual_auto_trading_toggle_contract.contract()
        return {
            'ready': True,
            'component': 'auto_trading_toggle',
            'type': 'checkbox_or_toggle_switch',
            'label': toggle['label'],
            'states': ['on', 'off_signal_only', 'disabled_by_safety', 'emergency_stop'],
            'default_state': 'off_signal_only',
            'requires_manual_reenable_after_safety': True,
            'system_can_enable_automatically': False
        }
auto_trading_toggle_dashboard_contract = AutoTradingToggleDashboardContract()
