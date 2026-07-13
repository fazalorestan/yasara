class StrategySimulationSafetyPolicy:
    def policy(self):
        return {'ready': True, 'simulation_only': True, 'real_execution_enabled': False, 'broker_connection_enabled': False, 'auto_trading_enabled': False, 'real_capital_at_risk': False, 'execution_allowed': False}
    def can_execute_real_order(self):
        return {'ready': True, 'allowed': False, 'reason': 'simulation_mode_only'}
strategy_simulation_safety_policy = StrategySimulationSafetyPolicy()
