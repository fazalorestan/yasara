class ManualAutoTradingToggleContract:
    def contract(self):
        return {
            'ready': True,
            'control': 'manual_checkbox_toggle',
            'label': 'Enable Auto Trading',
            'user_can_enable': True,
            'user_can_disable': True,
            'safety_can_disable': True,
            'system_can_enable_automatically': False,
            'default_auto_trading_enabled': False,
            'default_signal_only_mode': True,
            'requires_user_confirmation_to_enable': True
        }
manual_auto_trading_toggle_contract = ManualAutoTradingToggleContract()
