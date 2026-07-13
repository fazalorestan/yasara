class StrategyCapitalAllocationContract:
    def capital_plan(self):
        return {"ready": True, "total_capital": 0.0, "reserved_capital": 0.0, "deployable_capital": 0.0, "currency": "USDT", "execution_allowed": False}
strategy_capital_allocation_contract = StrategyCapitalAllocationContract()
