from app.platform_core.strategy_engine.strategy_contract import StrategyContractService

def test_v500_alpha41_a_contract(): assert StrategyContractService().contract()['execution_allowed'] is False
