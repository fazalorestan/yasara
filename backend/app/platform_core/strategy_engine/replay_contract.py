class StrategyReplayContract:
    def replay_plan(self):
        return {'ready': True, 'mode': 'contract_only', 'data_source': 'simulated', 'replay_enabled': True, 'real_market_connection': False, 'execution_allowed': False}
strategy_replay_contract = StrategyReplayContract()
