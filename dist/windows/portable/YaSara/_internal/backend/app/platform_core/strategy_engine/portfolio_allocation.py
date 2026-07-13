class StrategyPortfolioAllocationEngine:
    def allocation(self):
        return {"ready": True, "portfolio_id": "sim.portfolio", "allocations": [{"symbol": "BTCUSDT", "weight": 0.0}, {"symbol": "ETHUSDT", "weight": 0.0}], "mode": "advisory_only", "execution_allowed": False}
strategy_portfolio_allocation_engine = StrategyPortfolioAllocationEngine()
