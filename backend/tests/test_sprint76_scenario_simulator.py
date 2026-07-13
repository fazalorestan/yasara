from app.ai_trading_v1.scenario_simulator import ScenarioInputV1, ScenarioSimulatorV1

def test_scenario_simulator():
    result = ScenarioSimulatorV1().simulate(ScenarioInputV1(current_equity=10000, price_change_percent=10, exposure=1000))
    assert result.estimated_pnl == 100
    assert result.estimated_equity == 10100
