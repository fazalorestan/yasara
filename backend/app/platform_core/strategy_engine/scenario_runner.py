class StrategyScenarioRunner:
    def run(self):
        return {'ready': True, 'scenarios': [{'scenario_id':'base','status':'simulated'}, {'scenario_id':'risk_off','status':'simulated'}], 'count': 2, 'execution_allowed': False}
strategy_scenario_runner = StrategyScenarioRunner()
