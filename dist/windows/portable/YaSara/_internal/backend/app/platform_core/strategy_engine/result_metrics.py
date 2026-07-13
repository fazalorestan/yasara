class StrategyResultMetricsService:
    def metrics(self):
        return {'ready': True, 'total_trades': 0, 'win_rate': 0.0, 'pnl': 0.0, 'max_drawdown': 0.0, 'sharpe': 0.0, 'execution_allowed': False}
strategy_result_metrics_service = StrategyResultMetricsService()
