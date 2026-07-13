class StrategyRuleContractService:
    def rules(self):
        return {
            "ready": True,
            "rules": [
                {"rule_id": "risk.max_position", "enabled": True},
                {"rule_id": "execution.disabled", "enabled": True},
            ],
            "execution_allowed": False,
        }

    def validate(self):
        rules = self.rules()["rules"]
        return {"ready": True, "valid": len(rules) > 0, "execution_allowed": False}

strategy_rule_contract_service = StrategyRuleContractService()
