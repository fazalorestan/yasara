class StrategyBacktestContract:
    def contract(self):
        return {'ready': True, 'interface': 'strategy_backtest_contract', 'methods': ['prepare','simulate','metrics','report'], 'real_execution_enabled': False, 'broker_connection_enabled': False, 'execution_allowed': False}
strategy_backtest_contract = StrategyBacktestContract()
