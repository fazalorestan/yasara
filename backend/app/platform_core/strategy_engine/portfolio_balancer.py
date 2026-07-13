class StrategyPortfolioBalancer:
    def rebalance_plan(self):
        return {"ready": True, "actions": [], "rebalance_required": False, "mode": "dry_run", "executed": False, "execution_allowed": False}
strategy_portfolio_balancer = StrategyPortfolioBalancer()
