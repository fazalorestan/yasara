from app.platform_core.strategy_engine.allocation_safety import strategy_allocation_safety_policy
from app.platform_core.strategy_engine.capital_allocation import strategy_capital_allocation_contract
from app.platform_core.strategy_engine.exposure_controller import strategy_exposure_controller
from app.platform_core.strategy_engine.portfolio_allocation import strategy_portfolio_allocation_engine
from app.platform_core.strategy_engine.portfolio_balancer import strategy_portfolio_balancer
from app.platform_core.strategy_engine.position_sizing import strategy_position_sizing_contract
class StrategyAllocationReport:
    def report(self):
        return {"ready": True, "allocation": strategy_portfolio_allocation_engine.allocation(), "position_sizing": strategy_position_sizing_contract.size(), "capital_plan": strategy_capital_allocation_contract.capital_plan(), "exposure": strategy_exposure_controller.exposure(), "rebalance_plan": strategy_portfolio_balancer.rebalance_plan(), "safety": strategy_allocation_safety_policy.policy(), "real_execution_enabled": False, "broker_connection_enabled": False, "auto_trading_enabled": False, "execution_allowed": False}
strategy_allocation_report = StrategyAllocationReport()
