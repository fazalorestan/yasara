from app.platform_core.strategy_engine.rule_contract import StrategyRuleContractService

def test_v500_alpha41_a_rules(): assert len(StrategyRuleContractService().rules()['rules'])==2
