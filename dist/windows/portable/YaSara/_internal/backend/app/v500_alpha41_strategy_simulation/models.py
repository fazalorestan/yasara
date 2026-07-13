from pydantic import BaseModel
class StrategySimulationSummaryV500Alpha41(BaseModel):
    ready: bool = True
    phase: str = 'v5_0_alpha_41_strategy_engine_package_d'
    scope: str = 'strategy_backtest_simulation_contract'
    backtest_contract: bool = True
    simulation_engine: bool = True
    scenario_runner: bool = True
    result_metrics: bool = True
    replay_contract: bool = True
    simulation_safety_policy: bool = True
    real_execution_enabled: bool = False
    broker_connection_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
