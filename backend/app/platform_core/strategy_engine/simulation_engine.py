class StrategySimulationEngine:
    def simulate(self):
        return {'ready': True, 'strategy_id': 'trend.following', 'symbol': 'BTCUSDT', 'trades': [], 'pnl': 0.0, 'mode': 'simulation_only', 'execution_allowed': False}
strategy_simulation_engine = StrategySimulationEngine()
