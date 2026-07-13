from app.platform_core.strategy_engine.backtest_contract import strategy_backtest_contract
from app.platform_core.strategy_engine.replay_contract import strategy_replay_contract
from app.platform_core.strategy_engine.result_metrics import strategy_result_metrics_service
from app.platform_core.strategy_engine.scenario_runner import strategy_scenario_runner
from app.platform_core.strategy_engine.simulation_engine import strategy_simulation_engine
from app.platform_core.strategy_engine.simulation_safety import strategy_simulation_safety_policy
class StrategySimulationReport:
    def report(self):
        return {'ready': True, 'backtest_contract': strategy_backtest_contract.contract(), 'simulation': strategy_simulation_engine.simulate(), 'scenarios': strategy_scenario_runner.run(), 'metrics': strategy_result_metrics_service.metrics(), 'replay': strategy_replay_contract.replay_plan(), 'safety': strategy_simulation_safety_policy.policy(), 'real_execution_enabled': False, 'broker_connection_enabled': False, 'auto_trading_enabled': False, 'execution_allowed': False}
strategy_simulation_report = StrategySimulationReport()
