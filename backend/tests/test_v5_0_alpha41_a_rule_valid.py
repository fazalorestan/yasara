from app.platform_core.strategy_engine.rule_contract import StrategyRuleContractService

def test_v500_alpha41_a_rule_valid(): assert StrategyRuleContractService().validate()['valid'] is True
