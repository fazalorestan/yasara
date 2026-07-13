from app.platform_core.strategy_engine.scenario_runner import StrategyScenarioRunner

def test_v500_alpha41_d_scenarios(): assert StrategyScenarioRunner().run()['count']==2
