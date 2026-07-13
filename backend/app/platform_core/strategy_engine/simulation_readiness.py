from app.platform_core.strategy_engine.simulation_report import strategy_simulation_report
class StrategySimulationReadinessGate:
    def run(self):
        report = strategy_simulation_report.report()
        ready = report['ready'] and report['safety']['simulation_only'] and report['execution_allowed'] is False
        return {'ready': ready, 'checks': {'report_ready': report['ready'], 'simulation_only': report['safety']['simulation_only'], 'real_capital_at_risk': False, 'real_execution_allowed': False, 'broker_connection_allowed': False, 'auto_trading_allowed': False}, 'execution_allowed': False}
strategy_simulation_readiness_gate = StrategySimulationReadinessGate()
