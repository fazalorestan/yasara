class TradingControlStateContract:
    def state(self, auto_trading_enabled=False, disabled_by_safety=False):
        if disabled_by_safety:
            return {
                'auto_trading_enabled': False,
                'signal_only_mode': True,
                'disabled_by_safety': True,
                'manual_reenable_required': True,
                'allow_new_order': False,
                'status': 'disabled_by_safety'
            }
        auto = bool(auto_trading_enabled)
        return {
            'auto_trading_enabled': auto,
            'signal_only_mode': not auto,
            'disabled_by_safety': False,
            'manual_reenable_required': False,
            'allow_new_order': auto,
            'status': 'auto_trading_on' if auto else 'signal_only'
        }
trading_control_state_contract = TradingControlStateContract()
