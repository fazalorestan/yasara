from app.platform_core.strategy_engine.backtest_contract import strategy_backtest_contract
from app.platform_core.strategy_engine.replay_contract import strategy_replay_contract
from app.platform_core.strategy_engine.result_metrics import strategy_result_metrics_service
from app.platform_core.strategy_engine.scenario_runner import strategy_scenario_runner
from app.platform_core.strategy_engine.simulation_engine import strategy_simulation_engine
from app.platform_core.strategy_engine.simulation_readiness import strategy_simulation_readiness_gate
from app.platform_core.strategy_engine.simulation_report import strategy_simulation_report
from app.platform_core.strategy_engine.simulation_safety import strategy_simulation_safety_policy
from app.v500_alpha41_strategy_simulation.models import StrategySimulationSummaryV500Alpha41
class StrategySimulationFacadeV500Alpha41:
    def summary(self): return StrategySimulationSummaryV500Alpha41()
    def backtest_contract(self): return strategy_backtest_contract.contract()
    def simulate(self): return strategy_simulation_engine.simulate()
    def scenarios(self): return strategy_scenario_runner.run()
    def metrics(self): return strategy_result_metrics_service.metrics()
    def replay(self): return strategy_replay_contract.replay_plan()
    def safety(self): return strategy_simulation_safety_policy.policy()
    def report(self): return strategy_simulation_report.report()
    def readiness(self): return strategy_simulation_readiness_gate.run()
    def contract(self): return {'ready': True, 'strategy_engine': 'package_d_backtest_simulation', 'execution_allowed': False}
strategy_simulation_facade_v500_alpha41 = StrategySimulationFacadeV500Alpha41()
