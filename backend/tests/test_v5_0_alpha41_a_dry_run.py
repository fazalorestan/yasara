from app.platform_core.strategy_engine.strategy_contract import StrategyContractService

def test_v500_alpha41_a_dry_run(): assert StrategyContractService().dry_run()['executed'] is False
