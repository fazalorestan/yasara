class StrategyContractService:
    def contract(self):
        return {
            "ready": True,
            "interface": "strategy_contract",
            "methods": ["metadata", "prepare", "evaluate", "dry_run", "report"],
            "real_execution_enabled": False,
            "auto_trading_enabled": False,
            "execution_allowed": False,
        }

    def dry_run(self, strategy_id: str = "trend.following"):
        return {"ready": True, "strategy_id": strategy_id, "evaluated": True, "signal": "hold", "executed": False, "execution_allowed": False}

strategy_contract_service = StrategyContractService()
